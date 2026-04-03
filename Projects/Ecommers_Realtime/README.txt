🛒 End-to-End Real-Time E-Commerce Analytics Pipeline
======================================================

📌 PROJECT OVERVIEW
--------------------
This project demonstrates a complete real-time data engineering and analytics pipeline for a
simulated E-Commerce platform. It generates live transaction data — orders, payments, and
reviews — using Python, stores it in a normalized MySQL database, and visualizes key performance
indicators (KPIs) in real-time using a Power BI live dashboard.

It also includes an Exploratory Data Analysis (EDA) component using Python (Pandas, Matplotlib
& Seaborn) to uncover deep business insights from the streaming data.

Goal: Simulate a real-world e-commerce backend and analytics stack that mirrors what you'd find
in production environments — from ingestion to insight.


🛠️ TECH STACK & TOOLS
-----------------------
Layer                    | Technology
-------------------------|------------------------------------------
Language                 | Python 3.x
Data Generation          | Faker
Data Processing          | pandas, sqlalchemy
Visualization (EDA)      | matplotlib, seaborn
Database Connectivity    | mysql-connector-python
Database                 | MySQL
BI & Dashboard           | Power BI Desktop (DirectQuery Mode)
ODBC Driver              | MariaDB ODBC Connector 3.1 (64-bit)


🏗️ ARCHITECTURE WORKFLOW
--------------------------

┌─────────────────────┐
│   Python (Faker)    │  ← Simulates live e-commerce events
│  data_streamer.py   │    (customers, orders, payments, reviews)
└────────┬────────────┘
         │ Real-time INSERT
         ▼
┌─────────────────────┐
│    MySQL Database   │  ← Normalized relational schema
│  ecom_realtime_db   │    (ecom_realtime_db)
└────────┬────────────┘
         │
    ┌────┴─────┐
    │          │
    ▼          ▼
┌────────┐  ┌──────────────────┐
│ Python │  │    Power BI      │
│  EDA   │  │  Live Dashboard  │
│Jupyter │  │ (DirectQuery,    │
│Notebook│  │  5-sec refresh)  │
└────────┘  └──────────────────┘

Step-by-Step Flow:
1. Live Data Generation   — A Python script uses Faker to continuously generate realistic
                            e-commerce events (customers, products, orders, payments, reviews).
2. Database Insertion     — The script cleans and pushes this data into a relational MySQL
                            database in real-time.
3. Exploratory Data       — Jupyter Notebooks connect directly to MySQL via SQLAlchemy for
   Analysis (EDA)           live in-depth analysis.
4. Real-Time Dashboard    — Power BI connects via DirectQuery (MariaDB ODBC driver) with a
                            5-second auto page refresh to display live KPIs.


📁 PROJECT STRUCTURE
---------------------
ecommerce-realtime-pipeline/
├── database_schema.sql       # SQL script to set up MySQL DB & tables
├── data_streamer.py          # Main script for live data generation & insertion
├── eda_analysis.ipynb        # Jupyter Notebook for EDA & insights
├── dashboard.pbix            # Power BI Dashboard file
└── README.md                 # Project documentation


🚀 HOW TO RUN THE PROJECT
--------------------------

Prerequisites:
  - Python 3.x installed
  - MySQL Server running locally
  - Power BI Desktop installed
  - MariaDB ODBC 3.1 Driver (64-bit) installed

------------------------------
Step 1 — Database Setup
------------------------------
1. Open your MySQL environment (e.g., MySQL Workbench).
2. Run the SQL script to create the database and tables:

   SOURCE database_schema.sql;

This will create the ecom_realtime_db database and all required normalized tables.

------------------------------
Step 2 — Install Python Dependencies
------------------------------
Run the following command in your terminal:

   pip install mysql-connector-python faker pandas sqlalchemy matplotlib seaborn

------------------------------
Step 3 — Configure & Run the Data Streamer
------------------------------
1. Open data_streamer.py and update your MySQL credentials:

   DB_HOST     = "localhost"
   DB_USER     = "your_username"       # Update this
   DB_PASSWORD = "your_password"       # Update this
   DB_NAME     = "ecom_realtime_db"

2. Start the live data stream:

   python data_streamer.py

NOTE: Keep this script running in the background to simulate a live environment.
It will continuously insert new records into MySQL.

------------------------------
Step 4 — Power BI Real-Time Dashboard Setup
------------------------------
1. Download and install the MariaDB ODBC 3.1 Driver (64-bit) for Windows.
   Link: https://mariadb.com/downloads/connectors/
2. Restart Power BI Desktop after installation.
3. Click Get Data → More... → MariaDB.
4. Enter connection details:
     Server:   localhost
     Database: ecom_realtime_db
5. CRITICAL: Select DirectQuery as the Data Connectivity mode.
6. Load the required tables and verify relationships in the Model view.
7. Design your dashboard with the KPI visuals.
8. Enable live refresh:
     Go to Format pane → Page refresh → ON
     Set interval to 5 Seconds

------------------------------
Step 5 — Run the EDA Notebook
------------------------------
Open the Jupyter Notebook for exploratory analysis:

   jupyter notebook EDA_Ecommers.ipynb

The notebook connects to MySQL live and generates analytical visualizations
using Matplotlib & Seaborn.


📊 KEY BUSINESS KPIs TRACKED
------------------------------
KPI                        | Description
---------------------------|------------------------------------------------------
💰 Live Revenue Tracking   | Total revenue generated, updating dynamically in real-time
✅ Payment Success Rate     | Monitoring failed vs. successful transactions live
🏆 Top Selling Products    | Most popular items ranked by quantity sold
🧾 Average Order Value      | Average amount spent per order over time
   (AOV)                   |


🤝 CONTRIBUTING
----------------
Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch:   git checkout -b feature/your-feature
3. Commit your changes:          git commit -m 'Add some feature'
4. Push to the branch:           git push origin feature/your-feature
5. Open a Pull Request


======================================================
Built with ❤️ for Data Engineering & Analytics enthusiasts
If you found this project helpful, please consider giving it a ⭐
======================================================
