# 🇮🇳 Nifty 100 Financial Intelligence System

A full-stack financial intelligence system for India's top 100 Nifty companies.

## 🚀 Project Overview
This project builds a complete financial analytics platform covering:
- **Data Engineering** — Python ETL pipelines + PostgreSQL data warehouse
- **Power BI Dashboards** — 7 production-grade analytics dashboards
- **Django Web App** — Public website + REST API with Swagger documentation
- **ML Health Scoring** — Company health scores (EXCELLENT/GOOD/AVERAGE/WEAK/POOR)
- **Python Analytics** — 6 Jupyter notebooks with 20+ visualizations

## 🛠️ Tech Stack
| Category | Tool |
|---|---|
| ETL | Python, Pandas |
| Database | PostgreSQL 15 |
| BI Tool | Power BI Desktop |
| Web Framework | Django 4.2 + DRF |
| ML | Scikit-learn, Scipy |
| Notebooks | Jupyter |

## 📊 Dashboards
1. Executive Market Overview
2. Company Deep Dive
3. Sector Comparison
4. Health Scorecard
5. Growth Analytics
6. Debt & Leverage Monitor
7. Dividend & Shareholder Returns

## 🔌 API Endpoints
- `GET /api/companies/` — All companies
- `GET /api/data/` — Live PostgreSQL data
- `GET /api/docs/` — Swagger documentation

## 📓 Notebooks
1. Exploratory Data Analysis
2. Financial Health Scoring
3. Anomaly Detection
4. Sector Clustering
5. Peer Comparison Engine
6. Trend Analysis & Forecasting

## ⚙️ Setup
```bash
pip install -r requirements.txt
python etl/01_extract.py
python etl/02_clean.py
python etl/03_load.py
python manage.py runserver
```

## ⚠️ Disclaimer
Forecasts are model estimates only — not financial advice.
