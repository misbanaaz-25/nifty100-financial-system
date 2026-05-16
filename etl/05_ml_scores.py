import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:admin123@localhost:5432/nifty100_dw"
)

# Load data
print("Loading data...")
companies = pd.read_sql("SELECT * FROM companies", engine)
profitloss = pd.read_sql("SELECT * FROM profitandloss", engine)
balancesheet = pd.read_sql("SELECT * FROM balancesheet", engine)
cashflow = pd.read_sql("SELECT * FROM cashflow", engine)

print(f"Companies: {len(companies)}")
print(f"Profit & Loss: {len(profitloss)}")
print(f"Balance Sheet: {len(balancesheet)}")
print(f"Cash Flow: {len(cashflow)}")

# Get company symbols
symbols = companies.iloc[:, 0].tolist()

scores = []

for symbol in symbols:
    try:
        # Simple scoring based on available data
        score = 50  # base score
        
        # Get company data
        pl = profitloss[profitloss.iloc[:, 0] == symbol]
        bs = balancesheet[balancesheet.iloc[:, 0] == symbol]
        cf = cashflow[cashflow.iloc[:, 0] == symbol]
        
        # Profitability score
        if len(pl) > 0:
            score += 10
        
        # Balance sheet score
        if len(bs) > 0:
            score += 10
            
        # Cash flow score
        if len(cf) > 0:
            score += 10
        
        # Cap score at 100
        score = min(score, 100)
        
        # Health label
        if score >= 85:
            label = 'EXCELLENT'
        elif score >= 70:
            label = 'GOOD'
        elif score >= 50:
            label = 'AVERAGE'
        elif score >= 35:
            label = 'WEAK'
        else:
            label = 'POOR'
        
        scores.append({
            'symbol': symbol,
            'overall_score': score,
            'health_label': label
        })
        
    except Exception as e:
        print(f"Error for {symbol}: {e}")

# Save to DataFrame
df_scores = pd.DataFrame(scores)
print(f"\nScores calculated: {len(df_scores)}")
print(df_scores['health_label'].value_counts())

# Save to PostgreSQL
df_scores.to_sql('ml_scores', engine, if_exists='replace', index=False)
print("\nML Scores saved to PostgreSQL!")

# Save to CSV
df_scores.to_csv('data/clean/ml_scores.csv', index=False)
print("ML Scores saved to CSV!")