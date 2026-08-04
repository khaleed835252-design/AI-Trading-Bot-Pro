import pandas as pd

def calculate_indicators(df):

    # ==========================
    # EMA
    # ==========================

    df["EMA20"] = df["Close"].ewm(span=20).mean()

    df["EMA50"] = df["Close"].ewm(span=50).mean()

    df["EMA200"] = df["Close"].ewm(span=200).mean()

    # ==========================
    # RSI
    # ==========================

    delta = df["Close"].diff()

    gain = delta.where(delta > 0, 0)

    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(14).mean()

    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss

    df["RSI"] = 100 - (100 / (1 + rs))

    # ==========================
    # MACD
    # ==========================

    ema12 = df["Close"].ewm(span=12).mean()

    ema26 = df["Close"].ewm(span=26).mean()

    df["MACD"] = ema12 - ema26

    df["MACD_SIGNAL"] = df["MACD"].ewm(span=9).mean()

    # ==========================
    # ATR
    # ==========================

    high_low = df["High"] - df["Low"]

    high_close = (df["High"] - df["Close"].shift()).abs()

    low_close = (df["Low"] - df["Close"].shift()).abs()

    tr = pd.concat(
        [high_low, high_close, low_close],
        axis=1
    ).max(axis=1)

    df["ATR"] = tr.rolling(14).mean()

    # ==========================
    # Bollinger Bands
    # ==========================

    df["BB_MID"] = df["Close"].rolling(20).mean()

    std = df["Close"].rolling(20).std()

    df["BB_UPPER"] = df["BB_MID"] + (std * 2)

    df["BB_LOWER"] = df["BB_MID"] - (std * 2)

    return df