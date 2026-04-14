import yfinance as yf
import json
import os
from datetime import datetime, timezone

os.makedirs("data", exist_ok=True)

tickers = {
    "Gold":        "GC=F",
    "Silver":      "SI=F",
    "Crude Oil":   "CL=F",
    "Natural Gas": "NG=F",
    "Copper":      "HG=F",
    "Platinum":    "PL=F"
}

commodities = []
for name, ticker in tickers.items():
    try:
        t = yf.Ticker(ticker)
        price = round(t.fast_info['last_price'], 2)
        change = round(t.fast_info['last_price'] - t.fast_info['previous_close'], 2)
        pct = round((change / t.fast_info['previous_close']) * 100, 2)
        commodities.append({
            "name":    name,
            "ticker":  ticker,
            "price":   price,
            "change":  change,
            "pct":     pct
        })
        print(f"{name}: ${price}")
    except Exception as e:
        print(f"Error fetching {name}: {e}")

data = {
    "commodities": commodities,
    "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
}

with open("data/gold.json", "w") as f:
    json.dump(data, f)

print(f"Done: {data}")
