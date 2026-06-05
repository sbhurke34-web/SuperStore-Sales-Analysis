# Customer-Sales-Analysis-Using-Python-Tableau

A beginner-friendly data analytics project that analyzes customer sales performance using Python, Pandas, and Tableau. The project demonstrates how raw sales data can be cleaned, transformed, analyzed, and visualized to generate meaningful insights about customer purchasing behavior, regional sales performance, customer satisfaction, and sales trends.

This project focuses on sales analysis, customer behavior, regional performance evaluation, and data-driven visualization dashboards using Tableau.

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Tableau
* CSV Dataset

# Flow of Project

→ Data Cleaning & Preprocessing → Missing Value Treatment → Duplicate Data Handling → Data Type Correction → Outlier Detection & Treatment → Statistical Analysis & Aggregations → Data Visualization (Matplotlib & Seaborn) → Data Export (CSV) → Tableau Dashboard Creation → Sales Performance Insight Reporting

# Project Features

## 1. Data Extraction

* Imported customer sales dataset from CSV file
* Dataset includes:

  * Customer ID
  * Customer Name
  * Age
  * Sales
  * Order Date
  * Region
  * Rating

## 2. Data Cleaning & Preparation

* Handled missing values using median (numerical) and mode (categorical)
* Removed duplicate records
* Corrected incorrect data types
* Converted Order Date into DateTime format
* Standardized dataset for analysis

## 3. Feature Handling & Outlier Detection

* Applied IQR method to detect outliers in sales data
* Identified extreme sales transactions
* Prepared clean dataset for accurate analysis

## 4. Statistical Analysis

* Performed descriptive statistics on sales and customer age
* Analyzed:

  * Mean, Median, Min, Max
  * Sales distribution
  * Customer age distribution
  * Compared sales performance across regions and customers

## 5. Business Analytics

* Region-wise Sales Analysis
* Customer-wise Sales Analysis
* Customer Rating Analysis
* Monthly Sales Trend Analysis
* Identified top-performing customers and regions

## 6. Data Visualization (Matplotlib & Seaborn)

* Generated multiple plots including:

  * Histogram (Sales Distribution)
  * Scatter Plot (Age vs Sales)
  * Box Plot (Outlier Detection)
  * Bar Charts (Regional Sales Comparison)
  * Pie Chart (Region Distribution)
  * Line Plot (Monthly Sales Trend)
  * Heatmap (Correlation Analysis)
  * Rating Analysis Charts
  * Saved all visualizations into a structured folder (visualization/)

## 7. Data Export for Visualization Tools

* Cleaned dataset exported to CSV format
* File used for dashboard creation in Tableau

## 8. Tableau Dashboard Integration

* Imported dataset into Tableau
* Created interactive dashboards including:

  * Customer Sales Overview
  * Regional Sales Performance Dashboard
  * Monthly Sales Trend Analysis
  * Customer Distribution Dashboard
  * Customer Rating Analysis
  * Sales Distribution & Outlier Analysis
  * Customer-Region Heatmap Dashboard

## 9. Insight Generation

* The analysis provided insights such as:
* West region generated the highest sales performance
* Most sales transactions were concentrated below ₹1000
* Presence of high-value sales outliers significantly impacted sales distribution
* Customer ratings varied across different regions
* Customer age showed limited influence on sales performance
* Sales performance differed across regions and customers
* Monthly sales trends revealed variations in customer purchasing behavior

These insights help businesses understand customer purchasing patterns, identify high-performing regions, optimize sales strategies, and support data-driven decision making.

# Project Outcome

This project demonstrates a complete data analytics workflow including data cleaning, preprocessing, outlier detection, statistical analysis, visualization, and dashboard development. It showcases the ability to transform raw sales data into meaningful business insights and build interactive dashboards for data-driven decision making. 🚀📊
