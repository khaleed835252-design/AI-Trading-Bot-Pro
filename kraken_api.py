import krakenex
import pandas as pd

from config import API_KEY
from config import API_SECRET


class KrakenAPI:

    def __init__(self):

        self.api = krakenex.API(
            API_KEY,
            API_SECRET
        )

    def get_balance(self):

        result = self.api.query_private("Balance")

        if result["error"]:
            raise Exception(result["error"])

        return result["result"]

    def get_server_time(self):

        result = self.api.query_public("Time")

        return result["result"]

    def get_ticker(self, pair):

        result = self.api.query_public(

            "Ticker",

            {
                "pair": pair
            }

        )

        return result["result"]

    def get_ohlc(self, pair, interval=15):

        result = self.api.query_public(

            "OHLC",

            {
                "pair": pair,
                "interval": interval
            }

        )

        if result["error"]:

            raise Exception(result["error"])

        pair_name = list(result["result"].keys())[0]

        candles = result["result"][pair_name]

        df = pd.DataFrame(

            candles,

            columns=[
                "Time",
                "Open",
                "High",
                "Low",
                "Close",
                "VWAP",
                "Volume",
                "Trades",
            ],

        )

        numeric = [
            "Open",
            "High",
            "Low",
            "Close",
            "VWAP",
            "Volume"
        ]

        for col in numeric:

            df[col] = df[col].astype(float)

        return df