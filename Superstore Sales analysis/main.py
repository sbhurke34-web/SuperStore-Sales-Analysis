# ================== IMPORT LIBRARIES ==================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ================== OUTPUT FOLDER ==================
output_folder = "visualization"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ================== LOAD DATA ==================
df = pd.read_csv("C:\CODEING\Project\Superstore Sales\Superstore Sales Data Set.csv")

print("First 5 Rows:")
print(df.head())

print("\nShape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

# ================== MISSING VALUES ==================
print("\nMissing Values:")
print(df.isnull().sum())

# ================== DATA TYPE CORRECTION ==================

# Convert Age to numeric
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Convert Sales to numeric
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

# Convert Date
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

# ================== HANDLE MISSING VALUES ==================

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Sales'] = df['Sales'].fillna(df['Sales'].median())
df['Rating'] = df['Rating'].fillna(df['Rating'].median())

df['Region'] = df['Region'].fillna(df['Region'].mode()[0])
df['Customer_Name'] = df['Customer_Name'].fillna(df['Customer_Name'].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ================== DUPLICATE HANDLING ==================

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Shape After Removing Duplicates:", df.shape)

# ================== DATE EXTRACTION ==================

df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month
df['Day'] = df['Order_Date'].dt.day

# ================== OUTLIER DETECTION (IQR METHOD) ==================

Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['Sales'] < lower) | (df['Sales'] > upper)]

print("\nNumber of Outliers:", len(outliers))

# ================== DESCRIPTIVE STATISTICS ==================

print("\nSales Statistics:")
print(df['Sales'].describe())

print("\nAge Statistics:")
print(df['Age'].describe())

# ================== GROUPBY ANALYSIS ==================

print("\nRegion vs Sales:")
print(df.groupby('Region')['Sales'].agg(['count','mean','max']))

print("\nCustomer Name vs Sales:")
print(df.groupby('Customer_Name')['Sales'].agg(['mean','max']))

# ================== VISUALIZATIONS ==================

# 1 Histogram
plt.figure(figsize=(6,4))
plt.hist(df['Sales'], bins=20)
plt.title("Distribution of Sales")
plt.savefig(f"{output_folder}/hist_sales.png")
plt.close()

# 2 Boxplot
plt.figure(figsize=(6,4))
plt.boxplot(df['Sales'])
plt.title("Sales Boxplot")
plt.savefig(f"{output_folder}/boxplot_sales.png")
plt.close()

# 3 Bar Chart
plt.figure(figsize=(8,5))
df.groupby('Region')['Sales'].mean().plot(kind='bar')
plt.title("Average Sales by Region")
plt.savefig(f"{output_folder}/bar_region_sales.png")
plt.close()

# 4 Horizontal Bar Chart
plt.figure(figsize=(8,5))
df.groupby('Customer_Name')['Sales'].mean().plot(kind='barh')
plt.title("Average Sales by Customer")
plt.savefig(f"{output_folder}/barh_customer_sales.png")
plt.close()

# 5 Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df['Age'], df['Sales'])
plt.xlabel("Age")
plt.ylabel("Sales")
plt.title("Age vs Sales")
plt.savefig(f"{output_folder}/scatter_age_sales.png")
plt.close()

# 6 Pie Chart
plt.figure(figsize=(6,6))
df['Region'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Region Distribution")
plt.savefig(f"{output_folder}/pie_region.png")
plt.close()

# 7 Line Plot
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(8,5))
plt.plot(monthly_sales.index, monthly_sales.values)
plt.title("Monthly Sales Trend")
plt.savefig(f"{output_folder}/line_sales_trend.png")
plt.close()

# 8 Stacked Bar Chart
plt.figure(figsize=(8,5))
pd.crosstab(df['Region'], df['Customer_Name']).plot(kind='bar', stacked=True)
plt.title("Region vs Customer")
plt.savefig(f"{output_folder}/stacked_bar.png")
plt.close()

# 9 Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df[['Age','Sales','Rating']].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig(f"{output_folder}/heatmap.png")
plt.close()

# 10 Violin Plot
plt.figure(figsize=(8,5))
sns.violinplot(x='Region', y='Sales', data=df)
plt.title("Sales Distribution by Region")
plt.savefig(f"{output_folder}/violin_plot.png")
plt.close()

# ================== SAVE CLEANED DATA ==================

df.to_csv("cleaned_superstore_data.csv", index=False)

print("\n✅ Data Cleaning Completed")
print("✅ Graphs Saved in Visualization Folder")
print("✅ Cleaned Dataset Saved Successfully")