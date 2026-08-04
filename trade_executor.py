from config import PAPER_MODE
from config import TRADE_AMOUNT_EUR

class TradeExecutor:

    def __init__(self, kraken):
        self.kraken = kraken

    def buy(self, pair):

        print("\n" + "=" * 60)
        print("EXECUTING BUY ORDER")
        print("=" * 60)

        print("Pair :", pair)
        print("Amount :", TRADE_AMOUNT_EUR, "EUR")

        if PAPER_MODE:

            print("\nPAPER MODE ENABLED")
            print("No real order sent.")
            print("=" * 60)

            return {
                "status": "paper",
                "pair": pair,
                "amount": TRADE_AMOUNT_EUR
            }

        try:

            order = self.kraken.buy_market(
                pair,
                TRADE_AMOUNT_EUR
            )

            print("REAL ORDER EXECUTED")
            print(order)

            return order

        except Exception as e:

            print("ORDER FAILED")
            print(e)

            return None