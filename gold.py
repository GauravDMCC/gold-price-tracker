import yfinance as yf
import json
import os
from datetime import datetime, timezone

# create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

gold = yf.Ticker("GC=F")
price = gold.fast_info['last_price']

data = {
    "price": round(price, 2),
    "symbol": "XAU/USD",
    "unit": "USD/oz",
    "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
}

with open("data/gold.json", "w") as f:
    json.dump(data, f)

print(f"Updated: {data}")
