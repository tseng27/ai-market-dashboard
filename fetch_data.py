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
    "USDJPY": "JPY=X"
}

result = {}

for name, symbol in symbols.items():
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="5d")

    if hist.empty:
        result[name] = "N/A"
    else:
        latest_price = hist["Close"].dropna().iloc[-1]
        result[name] = round(float(latest_price), 2)

taiwan_time = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M")

result["date"] = taiwan_time

ordered_result = {
    "date": result["date"],
    "BTC": result["BTC"],
    "ETH": result["ETH"],
    "SP500": result["SP500"],
    "NASDAQ": result["NASDAQ"],
    "TAIEX": result["TAIEX"],
    "GOLD": result["GOLD"],
    "OIL": result["OIL"],
    "USDJPY": result["USDJPY"]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(ordered_result, f, ensure_ascii=False, indent=2)

print("data.json updated successfully")
