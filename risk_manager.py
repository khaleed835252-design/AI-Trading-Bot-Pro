class RiskManager:

    def __init__(self):
        self.take_profit = 3.0
        self.stop_loss = -1.0

    def check_trade(self, entry_price, current_price):

        pnl = ((current_price - entry_price) / entry_price) * 100

        if pnl >= self.take_profit:
            return "SELL", pnl

        elif pnl <= self.stop_loss:
            return "SELL", pnl

        else:
            return "HOLD", pnl