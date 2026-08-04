# ==========================================
# scanner.py
# ==========================================

from kraken_api import KrakenAPI

kraken = KrakenAPI()


def best_trade(results):

    buy_list = []

    for trade in results:

        if trade["signal"] == "BUY":
            buy_list.append(trade)

    if len(buy_list) == 0:
        return None

    buy_list = sorted(
        buy_list,
        key=lambda x: x["rsi"],
        reverse=True
    )

    return buy_list[0]


def get_price(symbol):

    ticker = kraken.get_ticker(symbol)

    pair = list(ticker.keys())[0]

    return float(
        ticker[pair]["c"][0]
    )