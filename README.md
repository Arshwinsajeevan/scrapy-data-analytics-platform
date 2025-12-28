# Web Data Aggregation & Analytics Platform

A Python-based data platform that extracts, stores, cleans, and analyzes structured web data from multiple public sources. Built using Scrapy, SQLite, and Pandas, this project demonstrates a complete data engineering workflow including web crawling, ETL processing, database storage, and analytics reporting.

## 🚀 Features
- Multi-source web scraping using Scrapy
- Structured data extraction with pagination handling
- Data storage in SQLite relational database
- ETL pipeline using Pandas and Regex
- Statistical & text-based analytics
- Automated report generation (CSV + Charts)
- Clean, scalable project architecture
- Version control using Git

## 🛠 Tech Stack
- Python
- Scrapy
- Pandas
- SQLite
- Matplotlib
- Regex
- Git & GitHub

## 📂 Project Structure
```bash
web-data-aggregator/
│
├── analytics/
├── data/
│ ├── raw/
│ ├── processed/
│ └── reports/
├── database/
├── scrapy_project/
└── README.md


## 📊 Reports Generated
- Average book price
- Rating distribution
- Top quoted authors
- Most frequent tags
- Price distribution graphs
- Text length analysis
- Trend summaries

Reports are stored in:
data/reports/


## ⚙️ How to Run
pip install -r requirements.txt
scrapy crawl books_spider
scrapy crawl quotes_spider
python analytics/books_analysis.py
python analytics/quotes_analysis.py
🎯 Outcome
This project demonstrates real-world data workflow capabilities aligned with enterprise data roles including:

Data aggregation

Data cleaning

Database handling

Analytics & reporting

Independent problem solving