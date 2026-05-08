# financial-modelling-bank-analysis-harshita
Financial Modelling and Banking Data Analysis project developed using Python, PostgreSQL, DBeaver, Pandas and Excel for banking dataset analytics and automation workflows.
# Financial Modelling & Banking Data Analysis

Developed by Harshita Chopra

This project focuses on financial modelling and banking data analytics using Python, PostgreSQL, DBeaver and Excel.

The project demonstrates practical implementation of:
- CSV data processing
- Financial statement analysis
- SQL database integration
- Python automation
- Banking analytics workflows

---

# Technologies Used

## Programming Language
- Python

## Database
- PostgreSQL

## Database Tool
- DBeaver

## Libraries
- Pandas
- NumPy
- psycopg2
- openpyxl

## IDE
- PyCharm

## Data Sources
- CSV Banking Datasets
- Excel Financial Data

---

# Project Objectives

- Analyse banking financial datasets
- Perform financial modelling
- Convert CSV data into SQL databases
- Execute SQL queries using PostgreSQL
- Automate analytics using Python
- Generate structured financial outputs

---

# Project Workflow

## Step 1 — CSV Dataset Collection

Banking datasets were collected in CSV format.

Example datasets:
- Union Bank Data
- Central Bank Data

---

## Step 2 — Database Creation

A PostgreSQL database was created for storing banking financial data.

Example SQL table creation:

```sql
CREATE TABLE central_bank_data (
    year DATE,
    "Equity Capital" BIGINT,
    "Reserves" BIGINT,
    "Deposits" BIGINT,
    "Borrowing" BIGINT,
    "Other Liabilities +" BIGINT,
    "Total Liabilities" BIGINT,
    "Fixed Assets +" BIGINT,
    "CWIP" BIGINT,
    "Investments" BIGINT,
    "Other Assets +" BIGINT,
    "Total Assets" BIGINT
);
```

---

## Step 3 — DBeaver Integration

DBeaver was used for:
- Database management
- SQL execution
- CSV import handling
- Table management
- Data verification

---

## Step 4 — Python Financial Modelling

Python scripts were created for:
- Reading CSV files
- Connecting PostgreSQL databases
- Data cleaning
- Financial calculations
- Analytics automation

Example:

```python
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="finance_db",
    user="postgres",
    password="YOUR_PASSWORD"
)

query = "SELECT * FROM central_bank_data;"
df = pd.read_sql(query, conn)

print(df)

conn.close()
```

---

# Financial Modelling Performed

- Balance Sheet Analysis
- Financial Ratio Analysis
- Trend Analysis
- Cash Flow Evaluation
- Banking Performance Analysis
- Asset & Liability Comparison

---

# Features

- CSV to SQL Workflow
- Banking Dataset Analytics
- Automated Financial Processing
- Python-SQL Integration
- Data Cleaning & Formatting
- Financial Reporting

---

# Files Included

## Python Scripts
- Financial modelling code
- SQL connection scripts
- Data processing programs

## CSV Files
- Banking datasets

## SQL Queries
- Table creation scripts
- Data operations

## Screenshots
- DBeaver workflow
- PostgreSQL setup
- PyCharm execution
- Excel outputs

## PDFs
- Project reports
- Presentation files

---

# Learning Outcomes

This project helped in learning:
- Financial analytics
- Database management
- SQL query execution
- Python automation
- Data processing workflows
- Banking sector analysis

---

# Future Improvements

Future enhancements may include:
- Power BI dashboards
- Automated ETL pipelines
- AI-based forecasting
- Interactive analytics dashboards
- Streamlit applications

---

# Author

Harshita Chopra

Aspiring Financial Analyst & Data Analytics Learner

LinkedIn:
Add LinkedIn Profile Here

GitHub:
Add GitHub Profile Here
