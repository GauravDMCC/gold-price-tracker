import yfinance as yf
import json
from datetime import datetime

gold = yf.Ticker("GC=F")
price = gold.fast_info['last_price']

data = {
    "price": round(price, 2),
    "symbol": "XAU/USD",
    "unit": "USD/oz",
    "updated": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
}

with open("data/gold.json", "w") as f:
    json.dump(data, f)

print(f"Updated: {data}")
