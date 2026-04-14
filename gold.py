import yfinance as yf
import json
import os
from datetime import datetime, timezone

os.makedirs("data", exist_ok=True)

commodities = {
    "Gold":        "GC=F",
    "Silver":      "SI=F",
    "Crude Oil":   "CL=F",
    "Natural Gas": "NG=F",
    "Copper":      "HG=F",
    "Platinum":    "PL=F"
}

crypto = {
    "Bitcoin":      "BTC-USD",
    "Ethereum":     "ETH-USD",
    "Binance":      "BNB-USD",
    "Cardano":      "ADA-USD",
    "Solana":       "SOL-USD",
    "XRP":          "XRP-USD",
    "Polkadot":     "DOT-USD",
    "Avalanche":    "AVAX-USD",
    "Polygon":      "MATIC-USD",
    "Litecoin":     "LTC-USD",
    "Algorand":     "ALGO-USD",
    "Bitcoin Cash": "BCH-USD"
}

def fetch(tickers):
    results = []
    for name, ticker in tickers.items():
        try:
            t = yf.Ticker(ticker)
            price  = round(t.fast_info['last_price'], 4)
            change = round(t.fast_info['last_price'] - t.fast_info['previous_close'], 4)
            pct    = round((change / t.fast_info['previous_close']) * 100, 2)
            results.append({"name": name, "price": price, "change": change, "pct": pct})
        except Exception as e:
            print(f"Error {name}: {e}")
    return results

data = {
    "commodities": fetch(commodities),
    "crypto":      fetch(crypto),
    "updated":     datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
}

with open("data/gold.json", "w") as f:
    json.dump(data, f)

print("Done!")
