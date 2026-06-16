# 🇿🇦 SA-Finance-Lakehouse

A production-style data engineering project that simulates the data platform of a South African retail bank.

The project demonstrates data ingestion, storage, transformation, analytics, and workflow automation using Python, PostgreSQL, SQL, and Apache Airflow.

---

## Business Problem

Banks generate large volumes of customer, account, and transaction data every day.

Business teams need reliable reporting to answer questions such as:

* Who are the highest spending customers?
* Which customers have become inactive?
* Which provinces generate the most revenue?
* Which transactions appear suspicious?
* How many transactions occur daily?

This project builds an end-to-end data platform that transforms raw banking data into business insights.

---

## Project Goals

* Generate realistic banking datasets
* Load data into PostgreSQL
* Perform analytical transformations using SQL
* Build business-focused reporting queries
* Detect potentially fraudulent activity
* Automate workflows using Apache Airflow
* Demonstrate data engineering best practices

---

## Architecture

Raw Data
→ Python Ingestion
→ PostgreSQL
→ SQL Transformations
→ Analytics Layer
→ Airflow Automation
→ Business Reports

---

## Planned Dataset

### Customers

* customer_id
* customer_name
* province
* join_date

### Accounts

* account_id
* customer_id
* account_type
* open_date

### Transactions

* transaction_id
* account_id
* amount
* transaction_type
* merchant
* transaction_date

---

## Planned Analytics

### Top Spenders

Identify high-value customers for premium banking and marketing initiatives.

### Dormant Accounts

Identify customers at risk of churn.

### Province Revenue

Measure regional performance and customer activity.

### Fraud Detection

Flag suspicious transaction patterns for investigation.

### Daily Transaction Monitoring

Track operational activity and transaction trends.

---

## Technology Stack

* Python
* PostgreSQL
* SQL
* Pandas
* SQLAlchemy
* Apache Airflow
* Faker
* Git
* GitHub

---

## Project Structure

SA-Finance-Lakehouse/

data/
├── raw/
└── processed/

notebooks/

sql/
├── staging/
└── marts/

src/

airflow/
└── dags/

screenshots/

README.md
requirements.txt
.gitignore

---

## Future Enhancements

* Dockerized deployment
* Star schema warehouse design
* FastAPI analytics API
* Spark processing layer
* Data quality framework
* CI/CD pipeline

---

## Status

🚧 In Development

Current Phase:
Dataset Generation and Core Data Modeling
