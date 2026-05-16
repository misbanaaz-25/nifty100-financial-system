import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    "postgresql://postgres:admin123@localhost:5432/nifty100_dw"
)

clean_folder = "data/clean"

print("Loading companies...")
df = pd.read_csv(f"{clean_folder}/companies.csv")
df.to_sql("companies", engine, if_exists="replace", index=False)
print(f"Companies: {len(df)} rows loaded")

print("\nLoading balancesheet...")
df = pd.read_csv(f"{clean_folder}/balancesheet.csv")
df.to_sql("balancesheet", engine, if_exists="replace", index=False)
print(f"Balancesheet: {len(df)} rows loaded")

print("\nLoading profitandloss...")
df = pd.read_csv(f"{clean_folder}/profitandloss.csv")
df.to_sql("profitandloss", engine, if_exists="replace", index=False)
print(f"Profitandloss: {len(df)} rows loaded")

print("\nLoading cashflow...")
df = pd.read_csv(f"{clean_folder}/cashflow.csv")
df.to_sql("cashflow", engine, if_exists="replace", index=False)
print(f"Cashflow: {len(df)} rows loaded")

print("\nLoading analysis...")
df = pd.read_csv(f"{clean_folder}/analysis.csv")
df.to_sql("analysis", engine, if_exists="replace", index=False)
print(f"Analysis: {len(df)} rows loaded")

print("\nLoading prosandcons...")
try:
    df = pd.read_csv(f"{clean_folder}/prosandcons.csv", encoding='utf-8')
    df.to_sql("prosandcons", engine, if_exists="replace", index=False)
    print(f"Prosandcons: {len(df)} rows loaded")
except Exception as e:
    print(f"Prosandcons skip - Error: {e}")

print("\nLoading documents...")
try:
    df = pd.read_csv(f"{clean_folder}/documents.csv", encoding='utf-8')
    df.to_sql("documents", engine, if_exists="replace", index=False)
    print(f"Documents: {len(df)} rows loaded")
except Exception as e:
    print(f"Documents skip - Error: {e}")

print("\nSaara data PostgreSQL mein load ho gaya!")