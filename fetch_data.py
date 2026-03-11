import yfinance as yf
import json

data = {}

def price(symbol):
    try:
        t = yf.Ticker(symbol)
        return float(t.history(period="1d")["Close"].iloc[-1])
    except:
        return None

def history(symbol):
    try:
        t = yf.Ticker(symbol)
        h = t.history(period="30d")
        return list(h["Close"])
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

# Taiwan
data["TAIEX"] = price("^TWII")
data["TSMC"] = price("2330.TW")

data["TSMC_history"] = history("2330.TW")
data["TSMC_labels"] = list(range(len(data["TSMC_history"])))

# Commodities
data["GOLD"] = price("GC=F")
data["OIL"] = price("CL=F")

# Forex
data["USDJPY"] = price("JPY=X")

# Magnificent 7
data["AAPL"] = price("AAPL")
data["MSFT"] = price("MSFT")
data["NVDA"] = price("NVDA")
data["GOOGL"] = price("GOOGL")
data["AMZN"] = price("AMZN")
data["META"] = price("META")
data["TSLA"] = price("TSLA")

# ETF
data["SPY"] = price("SPY")
data["QQQ"] = price("QQQ")
data["DIA"] = price("DIA")

# Taiwan ETF
data["0050"] = price("0050.TW")
data["00878"] = price("00878.TW")

with open("data.json","w") as f:
    json.dump(data,f)
