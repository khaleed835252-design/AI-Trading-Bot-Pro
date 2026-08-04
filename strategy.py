def signal(df):

    last = df.iloc[-1]

    score = 0

    # ==========================
    # Trend
    # ==========================

    if last["EMA20"] > last["EMA50"]:
        score += 20

    if last["EMA50"] > last["EMA200"]:
        score += 20

    # ==========================
    # RSI
    # ==========================

    if 55 <= last["RSI"] <= 70:
        score += 15

    # ==========================
    # MACD
    # ==========================

    if last["MACD"] > last["MACD_SIGNAL"]:
        score += 15

    # ==========================
    # Bollinger Bands
    # ==========================

    if last["Close"] > last["BB_MID"]:
        score += 15

    # ==========================
    # Volume
    # ==========================

    avg_volume = df["Volume"].tail(20).mean()

    if last["Volume"] > avg_volume:
        score += 15

    # ==========================
    # ATR
    # ==========================

    atr_percent = (last["ATR"] / last["Close"]) * 100

    if 1 <= atr_percent <= 5:
        score += 10

    # ==========================
    # Final Decision
    # ==========================

    if score >= 80:
        return "BUY"

    elif score <= 30:
        return "SELL"

    else:
        return "WATCH"