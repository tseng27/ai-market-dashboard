import yfinance as yf
import json

data = {}

def price(symbol):
    try:
        t = yf.Ticker(symbol)
        hist = t.history(period="5d")
        if hist.empty:
            return None
        return float(hist["Close"].dropna().iloc[-1])
    except:
        return None

def history(symbol):
    try:
        t = yf.Ticker(symbol)
        h = t.history(period="30d")
        if h.empty:
            return []
        return [float(x) for x in h["Close"].dropna().tolist()]
    except:
        return []

# Crypto
data["BTC"] = price("BTC-USD")
data["ETH"] = price("ETH-USD")
data["BTC_history"] = history("BTC-USD")
data["BTC_labels"] = list(range(len(data["BTC_history"])))

# US Index
data["SP500"] = price("^GSPC")
data["NASDAQ"] = price("^IXIC")
data["DOW"] = price("^DJI")
data["SP500_history"] = history("^GSPC")
data["SP500_labels"] = list(range(len(data["SP500_history"])))

# Taiwan Market
data["TAIEX"] = price("^TWII")
data["TSMC"] = price("2330.TW")
data["TSMC_history"] = history("2330.TW")
data["TSMC_labels"] = list(range(len(data["TSMC_history"])))

# Commodities
data["GOLD"] = price("GC=F")
data["OIL"] = price("CL=F")
data["GOLD_history"] = history("GC=F")
data["GOLD_labels"] = list(range(len(data["GOLD_history"])))

# Forex
data["USDJPY"] = price("JPY=X")

# US ETF
data["SPY"] = price("SPY")
data["QQQ"] = price("QQQ")
data["DIA"] = price("DIA")

# Taiwan ETF
data["ETF0050"] = price("0050.TW")
data["ETF00878"] = price("00878.TW")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
