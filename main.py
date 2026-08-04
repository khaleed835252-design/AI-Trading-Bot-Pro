from ai_dataset import save_row
from risk_manager import RiskManager
from paper_trader import PaperTrader
from kraken_api import KrakenAPI
from indicators import calculate_indicators
from strategy import signal
import scanner
from scanner import best_trade

kraken = KrakenAPI()
paper = PaperTrader()
risk = RiskManager()

pairs = [
    "XXBTZEUR",   # Bitcoin
    "XETHZEUR",   # Ethereum
    "ADAEUR",     # Cardano
    "XRPEUR",     # XRP
    "DOGEEUR",    # Dogecoin
    "SOLEUR"      # Solana
]

results = []

print("=" * 70)
print("                AI TRADING BOT V1.0")
print("=" * 70)

print("\nConnecting to Kraken...\n")

try:

    balance = kraken.get_balance()

    print("Connected Successfully")

    if "ZEUR" in balance:
        print(f"EUR Balance : {balance['ZEUR']} EUR")

except Exception as e:

    print("Connection Error")
    print(e)
    quit()

print("\nScanning Market...\n")

for pair in pairs:

    try:

        df = kraken.get_ohlc(pair)

        df = calculate_indicators(df)

        trade_signal = signal(df)

        save_row(pair, df, trade_signal)

        last_price = df["Close"].iloc[-1]
        last_rsi = df["RSI"].iloc[-1]

        results.append({
            "symbol": pair,
            "price": last_price,
            "rsi": last_rsi,
            "signal": trade_signal
        })

        print(
            f"{pair:12}"
            f" Price: {last_price:10.2f}"
            f" RSI: {last_rsi:6.2f}"
            f" Signal: {trade_signal}"
        )

    except Exception as e:

        print(pair, "FAILED")
        print(e)

print("\n" + "=" * 70)

trade = best_trade(results)

print("\n" + "=" * 70)

if trade:

    print("\nBEST TRADE FOUND\n")

    print(f"Pair   : {trade['symbol']}")
    print(f"Price  : {trade['price']:.2f}")
    print(f"RSI    : {trade['rsi']:.2f}")
    print(f"Signal : {trade['signal']}")

    TRADE_AMOUNT = 20

    paper.buy(
        trade["symbol"],
        trade["price"],
        TRADE_AMOUNT
    )

    import time

    entry_price = trade["price"]

    while True:

        current_price = scanner.get_price(
            trade["symbol"]
        )

        status, profit = risk.check_trade(
            entry_price,
            current_price
        )

        print(
            f"Current Price: {current_price:.2f} | "
            f"PnL: {profit:.2f}% | "
            f"Status: {status}"
        )

        if status == "SELL":

            paper.sell(current_price)

            print()
            print("=" * 60)
            print("POSITION CLOSED")
            print(f"Exit Price : {current_price:.2f}")
            print(f"PnL : {profit:.2f}%")
            print("=" * 60)

            break

        time.sleep(30)

else:

    print("\nNo Trading Opportunity Found")

print("\n" + "=" * 70)