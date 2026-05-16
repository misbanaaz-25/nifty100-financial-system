import pandas as pd
import os

raw_folder = "data/raw"
clean_folder = "data/clean"

os.makedirs(clean_folder, exist_ok=True)

files = [
    "companies",
    "balancesheet",
    "profitandloss",
    "cashflow",
    "analysis",
    "prosandcons",
    "documents"
]

for file in files:
    print(f"\nCleaning {file}...")
    try:
        df = pd.read_csv(f"{raw_folder}/{file}.csv", header=2, encoding='utf-8')
        df.columns = df.columns.str.strip()
        df = df.dropna(how='all')
        df.to_csv(f"{clean_folder}/{file}.csv", index=False, encoding='utf-8')
        print(f"{file}: {len(df)} rows saved")
    except Exception as e:
        print(f"{file} - Error: {e}")

print("\nSaari files clean ho gayi!")