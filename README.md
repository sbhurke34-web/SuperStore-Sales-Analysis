Customer-Sales-Analysis-Using-Python-Tableau

A beginner-friendly data analytics project that analyzes customer sales data using Python, Pandas, and Tableau. The project demonstrates how raw sales data can be cleaned, transformed, analyzed, and visualized to generate meaningful insights about customer purchasing behavior, regional performance, sales trends, and customer satisfaction.

This project focuses on sales performance analysis, customer segmentation, regional comparison, and data-driven visualization dashboards using Tableau.

Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Tableau
CSV Dataset
Flow of Project

Data Collection → Data Cleaning & Preprocessing → Missing Value Handling → Duplicate Removal → Outlier Detection → Statistical Analysis & Aggregations → Data Visualization (Matplotlib & Seaborn) → Data Export (CSV) → Tableau Dashboard Creation → Business Insight Reporting

Project Features
1. Data Extraction

Imported customer sales dataset from a CSV file.

Dataset includes:

Customer ID
Customer Name
Age
Sales
Order Date
Region
Rating
2. Data Cleaning & Preparation
Identified and handled missing values
Filled numerical missing values using median
Filled categorical missing values using mode
Removed duplicate records
Corrected data types for numerical and date columns
Converted Order Date into DateTime format
Prepared a clean dataset for analysis
3. Feature Handling & Outlier Detection
Applied the IQR (Interquartile Range) method to detect outliers in Sales
Identified extreme sales transactions
Improved data quality for accurate analysis
Prepared a refined dataset for visualization
4. Statistical Analysis

Performed descriptive statistics on key variables.

Analyzed:

Mean, Median, Min, Max
Sales Distribution
Customer Age Distribution
Regional Sales Performance
Customer-wise Sales Performance
5. Business Analytics
Regional Performance Analysis

Compared sales across:

East Region
North Region
South Region
West Region
Customer Performance Analysis

Identified:

Top-performing customers
Highest sales contributors
Customer purchasing trends
Customer Rating Analysis

Evaluated customer satisfaction across different regions.

6. Data Visualization (Matplotlib & Seaborn)

Generated multiple visualizations including:

Histogram (Sales Distribution)
Box Plot (Sales Outlier Detection)
Scatter Plot (Age vs Sales)
Bar Chart (Sales by Region)
Horizontal Bar Chart (Rating by Region)
Pie Chart (Regional Distribution)
Line Chart (Sales Trend Analysis)
Heatmap (Correlation Analysis)
Customer Sales Comparison Charts

Saved all visualizations into a structured folder (visualization/).

7. Data Export for Visualization Tools
Exported cleaned dataset to CSV format
Prepared data for advanced dashboard creation in Tableau
8. Tableau Dashboard Integration

Imported the cleaned dataset into Tableau.

Created interactive dashboards including:

Customer Sales Overview Dashboard
Regional Sales Performance Dashboard
Monthly Sales Trend Analysis
Age vs Sales Relationship Analysis
Customer Rating Dashboard
Sales Distribution & Outlier Analysis
Customer-Region Heatmap Dashboard
9. Insight Generation

The analysis provided insights such as:

The West region generated the highest overall sales.
Most customer sales transactions were concentrated below ₹1000.
A small number of high-value transactions created significant sales outliers.
Customer age showed limited influence on sales performance.
Customer ratings varied across different regions.
Sales performance differed significantly among customers and regions.
Regional trends helped identify strong and weak market areas.

These insights support data-driven business decisions and sales strategy optimization.

Project Outcome

This project demonstrates a complete data analytics workflow including data cleaning, preprocessing, outlier detection, statistical analysis, visualization, and dashboard development. It showcases the ability to transform raw sales data into actionable business insights and build interactive Tableau dashboards for effective decision-making and performance monitoring. 🚀📊
