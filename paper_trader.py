from datetime import datetime


class PaperTrader:

    def __init__(self):

        self.balance = 1000.0
        self.position = None
        self.total_trades = 0
        self.total_profit = 0.0

    def buy(self, symbol, price, amount):

        if self.position is not None:

            print("\nTrade already open.\n")
            return False

        qty = amount / price

        self.position = {
            "symbol": symbol,
            "entry_price": price,
            "amount": amount,
            "qty": qty,
            "entry_time": datetime.now()
        }

        self.balance -= amount

        print()
        print("=" * 60)
        print("PAPER BUY EXECUTED")
        print("=" * 60)
        print(f"Time   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Pair   : {symbol}")
        print(f"Price  : {price:.2f}")
        print(f"Amount : {amount:.2f} EUR")
        print(f"Qty    : {qty:.6f}")
        print(f"Balance: {self.balance:.2f} EUR")
        print("=" * 60)

        return True

    def sell(self, price):

        if self.position is None:

            print("No open position.")
            return False

        value = self.position["qty"] * price

        profit = value - self.position["amount"]

        profit_percent = (
            (price - self.position["entry_price"])
            / self.position["entry_price"]
        ) * 100

        self.balance += value

        self.total_profit += profit

        self.total_trades += 1

        duration = datetime.now() - self.position["entry_time"]

        print()
        print("=" * 60)
        print("PAPER SELL EXECUTED")
        print("=" * 60)
        print(f"Time       : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Pair       : {self.position['symbol']}")
        print(f"Buy Price  : {self.position['entry_price']:.2f}")
        print(f"Sell Price : {price:.2f}")
        print(f"Profit EUR : {profit:.2f}")
        print(f"Profit %   : {profit_percent:.2f}%")
        print(f"Duration   : {duration}")
        print(f"Balance    : {self.balance:.2f} EUR")
        print(f"Trades     : {self.total_trades}")
        print(f"Total P/L  : {self.total_profit:.2f} EUR")
        print("=" * 60)

        self.position = None

        return True

    def has_position(self):

        return self.position is not None

    def get_position(self):

        return self.position

    def get_balance(self):

        return self.balance

    def get_statistics(self):

        return {
            "balance": self.balance,
            "trades": self.total_trades,
            "profit": self.total_profit
        }