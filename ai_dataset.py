import csv
import os
from datetime import datetime

FILE = "ai_dataset.csv"


def save_row(symbol, df, signal):

    last = df.iloc[-1]

    exists = os.path.isfile(FILE)

    with open(FILE, "a", newline="") as f:

        writer = csv.writer(f)

        if not exists:

            writer.writerow([
                "Time",
                "Pair",
                "Price",
                "EMA20",
                "EMA50",
                "EMA200",
                "RSI",
                "MACD",
                "MACD_SIGNAL",
                "ATR",
                "BB_UPPER",
                "BB_MID",
                "BB_LOWER",
                "Volume",
                "Signal",
                "Outcome"
            ])

        writer.writerow([
            datetime.now(),
            symbol,
            last["Close"],
            last["EMA20"],
            last["EMA50"],
            last["EMA200"],
            last["RSI"],
            last["MACD"],
            last["MACD_SIGNAL"],
            last["ATR"],
            last["BB_UPPER"],
            last["BB_MID"],
            last["BB_LOWER"],
            last["Volume"],
            signal
        ])