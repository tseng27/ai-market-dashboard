import json
from datetime import datetime, timezone, timedelta
import yfinance as yf

symbols = {
    "BTC": "BTC-USD",
    "ETH": "ETH-USD",

    "SP500": "^GSPC",
    "NASDAQ": "^IXIC",

    "TAIEX": "^TWII",

    "GOLD": "GC=F",
    "OIL": "CL=F",

    "USDJPY": "JPY=X",

    "NVDA": "NVDA",
    "AAPL": "AAPL",
    "MSFT": "MSFT",
    "GOOGL": "GOOGL",
    "AMZN": "AMZN",

    "TSMC": "2330.TW",
    "MEDIATEK": "2454.TW",
    "FOXCONN": "2317.TW",

    "SP500_F": "ES=F",
    "NASDAQ_F": "NQ=F"
}

result = {}

def get_latest_and_history(symbol):
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="1mo")

    if hist.empty:
        return "N/A", [], []

    close_series = hist["Close"].dropna()
    if close_series.empty:
        return "N/A", [], []

    latest_price = round(float(close_series.iloc[-1]), 2)

    labels = [d.strftime("%m-%d") for d in close_series.index]
    values = [round(float(v), 2) for v in close_series.tolist()]

    return latest_price, labels, values

for name, symbol in symbols.items():
    latest, labels, values = get_latest_and_history(symbol)
    result[name] = latest
    result[name + "_labels"] = labels
    result[name + "_history"] = values

taiwan_time = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M")
result["date"] = taiwan_time

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("market data with chart history updated")
