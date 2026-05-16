import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:admin123@localhost:5432/nifty100_dw"
)

# Sector mapping
sector_map = {
    'TCS': 'IT', 'INFY': 'IT', 'WIPRO': 'IT', 'HCLTECH': 'IT', 'TECHM': 'IT',
    'HDFCBANK': 'Banking', 'AXISBANK': 'Banking', 'SBIN': 'Banking',
    'BANKBARODA': 'Banking', 'PNB': 'Banking', 'CANBK': 'Banking',
    'BAJFINANCE': 'NBFC', 'BAJAJFINSV': 'NBFC', 'CHOLAFIN': 'NBFC',
    'ADANIGREEN': 'Energy', 'ADANIPOWER': 'Energy', 'ADANIENSOL': 'Energy',
    'ATGL': 'Energy', 'NTPC': 'Energy', 'POWERGRID': 'Energy',
    'APOLLOHOSP': 'Healthcare', 'SUNPHARMA': 'Pharma', 'DRREDDY': 'Pharma',
    'ASIANPAINT': 'Paint', 'PIDILITIND': 'Paint',
    'AMBUJACEM': 'Cement', 'SHREECEM': 'Cement',
    'RELIANCE': 'Energy', 'ONGC': 'Energy', 'IOC': 'Energy',
    'MARUTI': 'Auto', 'TATAMOTORS': 'Auto', 'BAJAJ-AUTO': 'Auto',
    'EICHERMOT': 'Auto', 'MOTHERSON': 'Auto',
    'SBILIFE': 'Insurance', 'HDFCLIFE': 'Insurance',
    'TITAN': 'Consumer', 'TATACONSUM': 'Consumer', 'NESTLEIND': 'Consumer',
    'HINDUNILVR': 'Consumer', 'ITC': 'Consumer',
    'ADANIPORTS': 'Ports', 'ADANIENT': 'Holding',
    'TATASTEEL': 'Metals', 'JSWSTEEL': 'Metals', 'HINDALCO': 'Metals',
    'COALINDIA': 'Mining', 'RECLTD': 'Finance', 'PFC': 'Finance',
    'NAUKRI': 'IT', 'LTIM': 'IT', 'LT': 'Infrastructure',
    'SIEMENS': 'Infrastructure', 'ABB': 'Infrastructure',
    'TATAPOWER': 'Energy', 'NHPC': 'Energy',
    'TORNTPHARM': 'Pharma', 'DIVISLAB': 'Pharma',
    'INDUSINDBK': 'Banking', 'KOTAKBANK': 'Banking', 'ICICIBANK': 'Banking',
    'TRENT': 'Retail', 'DMART': 'Retail',
    'BHARTIARTL': 'Telecom', 'BPCL': 'Energy', 'GRASIM': 'Cement',
    'SHRIRAMFIN': 'NBFC', 'SBICARD': 'NBFC',
    'TATASTEEL': 'Metals', 'VEDL': 'Metals',
    'ULTRACEMCO': 'Cement', 'TATAELXSI': 'IT',
}

# Load companies
df = pd.read_csv('data/clean/companies.csv')
print(f"Companies before: {len(df)}")
print(f"Columns: {list(df.columns)}")

# Add sector column
df['sector'] = df.iloc[:, 0].map(sector_map).fillna('Other')

# Save back
df.to_csv('data/clean/companies.csv', index=False)

# Update PostgreSQL
df.to_sql('companies', engine, if_exists='replace', index=False)

print(f"Companies after: {len(df)}")
print("Sectors added successfully!")
print(df[['sector']].value_counts())