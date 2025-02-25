# 📊 Sales Insights - Data Analysis using Tableau & SQL
This project presents Sales Insights for an India-based hardware company using Tableau & SQL, as part of my Data Science learning journey.

# 🛠 Project Overview
This data analysis project focuses on uncovering valuable insights from the company’s sales data. The goal is to enable data-driven decision-making by analyzing revenue, profit, customer behavior, and product performance.

# Key Highlights
✅ Extracted data from unstructured sources using SQL for ETL processing
✅ Performed data cleaning and designed a Star Schema data model in Tableau
✅ Developed an interactive Tableau dashboard to analyze sales trends
✅ Generated actionable insights to optimize business decisions

# ⚙️ Technologies Used
[Advanced Excel]
[SQL (MySQL, SQL Server)]
[Tableau & Power BI]
[Statistics for Data Analysis]

# 📊 Tableau Dashboard
🔗 View Tableau Dashboard [https://public.tableau.com/authoring/Salesdatasets/Dashboard-RevenueAnalysis#1]

# 📌 Problem Statements
The Sales Director wants to evaluate the company’s performance across different Indian states and offer strategic discounts based on insights.

# Key Questions Analyzed
📍 Q1: Revenue breakdown by cities?
📍 Q2: Revenue breakdown by years & months?
📍 Q3: Top 5 customers by revenue & sales quantity?
📍 Q4: Top 5 products by revenue?
📍 Q5: Net Profit & Profit Margin by market?

# 📋 Project Approach
1️⃣ Purpose: What? Why? Goals?
🔹 Unlock hidden sales insights to support strategic decision-making.
🔹 Automate reporting to reduce manual effort in data gathering.

2️⃣ Stakeholders: Who is Involved?
👨‍💼 Sales Director – Decision-making on pricing & discounts.
💻 I.T. Team – Infrastructure & data storage.
📞 Customer Service Team – Insights into customer behavior.
📊 Data & Analytics Team – Generating actionable insights.

3️⃣ End Result: What Do We Aim to Achieve?
✅ Automated dashboards with real-time sales insights.
✅ Enhanced data-driven decision-making.
✅ Reduced manual effort for sales analysts.

4️⃣ Success Metrics: How Do We Measure Success?
📊 Sales order insights updated with the latest data.
📉 10% cost savings on total spending via data-driven pricing.
⏳ 20% reduction in manual data gathering time for sales analysts.

# 🔧 Setup Process

Step 1: Download Data
📂 Download [db_dump.sql] or [db_dump.xlsx].

Step 2: Import Data
📥 Import the dataset into MySQL and perform ETL (Extract, Transform, Load) if needed.

Step 3: Install Tableau
📊 Download Tableau Public (Free) or Tableau Desktop (14-day trial).

Step 4: Connect Tableau to Database
🔗 Link Tableau to MySQL or Excel database.

Step 5: Save Project
💾 Save your Tableau work as .twb or .twbx.

🛢️ Data Analysis Using SQL
Basic Queries
🔹 Show all customer records:

'''SELECT * FROM customers;'''
🔹 Count total customers:

'''SELECT COUNT(*) FROM customers;'''
🔹 Transactions for Chennai market (Mark001):

SELECT * FROM transactions WHERE market_code='Mark001';
🔹 Distinct product codes sold in Chennai:

SELECT DISTINCT product_code FROM transactions WHERE market_code='Mark001';
Revenue & Profit Analysis Queries
🔹 Transactions in USD currency:

SELECT * FROM transactions WHERE currency="USD";
🔹 Transactions in 2020 (Joined with Date Table):

SELECT transactions.*, date.* 
FROM transactions 
INNER JOIN date 
ON transactions.order_date=date.date 
WHERE date.year=2020;
🔹 Total Revenue in 2020:

SELECT SUM(transactions.sales_amount) 
FROM transactions 
INNER JOIN date 
ON transactions.order_date=date.date 
WHERE date.year=2020 
AND (transactions.currency="INR" OR transactions.currency="USD");
🔹 Total Revenue in January 2020:

SELECT SUM(transactions.sales_amount) 
FROM transactions 
INNER JOIN date 
ON transactions.order_date=date.date 
WHERE date.year=2020 
AND date.month_name="January" 
AND (transactions.currency="INR" OR transactions.currency="USD");
🔹 Total Revenue in Chennai (2020):

SELECT SUM(transactions.sales_amount) 
FROM transactions 
INNER JOIN date 
ON transactions.order_date=date.date 
WHERE date.year=2020 
AND transactions.market_code="Mark001";
📊 Data Analysis Using Tableau
Tableau Public Dashboards
✅ Revenue & Profit Analysis
✅ Star Schema Data Model Implementation

🔹 Tableau Dashboard - Revenue Analysis (Screenshot or link here)
![Tableau Dashbpard Revenue Analysis](https://github.com/user-attachments/assets/e3204329-c4f0-4a43-91df-2d757e5c62cb)

🔹 Tableau Dashboard - Profit Analysis
![Tableau Dashbpard Profit Analysis](https://github.com/user-attachments/assets/290787c4-d9f5-4b43-aca8-58509cea119a)

🔗 Conclusion & Next Steps
This project successfully analyzed sales performance and identified growth opportunities for the company. The automated Tableau dashboard will help stakeholders make faster, data-driven decisions.
