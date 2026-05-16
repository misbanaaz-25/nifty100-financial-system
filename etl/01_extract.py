import pandas as pd
import os

# Yeh batata hai ki files kahan hain
raw_folder = "data/raw"
clean_folder = "data/clean"

# Clean folder banao agar nahi hai
os.makedirs(clean_folder, exist_ok=True)

# Saari 7 files ke naam
files = [
    "companies",
    "analysis",
    "balancesheet",
    "profitandloss",
    "cashflow",
    "prosandcons",
    "documents"
]

# Ek ek karke saari files padhega
for file in files:
    path = f"{raw_folder}/{file}.xlsx"
    df = pd.read_excel(path)
    
    print(f"\n--- {file.upper()} ---")
    print(f"Rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    
    # CSV ke roop mein save karo
    df.to_csv(f"{raw_folder}/{file}.csv", index=False)
    print(f"Saved: {raw_folder}/{file}.csv")

print("\nSaari files successfully read ho gayi!")