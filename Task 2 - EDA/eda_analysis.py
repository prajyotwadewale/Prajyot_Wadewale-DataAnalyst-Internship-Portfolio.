import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("Starting EDA Analysis...\n")

file_name = "cleaned_ecommerce_data.csv"

# Check file exists
if not os.path.exists(file_name):
    print("ERROR: cleaned dataset not found!")
    exit()

# Load dataset
df = pd.read_csv(file_name)

# ---------------------------
# BASIC INFO
# ---------------------------
print("Dataset Info:\n")
print(df.info())

print("\nSummary Statistics:\n")
print(df.describe())

print("\nMissing Values:\n")
print(df.isnull().sum())

# ---------------------------
# CREATE OUTPUT FOLDER
# ---------------------------
if not os.path.exists("charts"):
    os.makedirs("charts")

# ---------------------------
# UNIVARIATE ANALYSIS
# ---------------------------

# Sales Distribution
plt.figure()
plt.hist(df["TotalPrice"], bins=50)
plt.title("Sales Distribution")
plt.xlabel("TotalPrice")
plt.ylabel("Frequency")
plt.savefig("charts/sales_distribution.png")
plt.close()

# Top 10 Countries
plt.figure()
df["Country"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries by Orders")
plt.xlabel("Country")
plt.ylabel("Count")
plt.savefig("charts/top_countries.png")
plt.close()

# Top 10 Products
plt.figure()
df["Description"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Products")
plt.savefig("charts/top_products.png")
plt.close()

# ---------------------------
# BUSINESS INSIGHTS
# ---------------------------

# Top 5 Products by Revenue
top_products = df.groupby("Description")["TotalPrice"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products by Revenue:\n", top_products)

# Monthly Sales Trend
monthly_sales = df.groupby("Month")["TotalPrice"].sum()
print("\nMonthly Sales:\n", monthly_sales)

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.savefig("charts/monthly_sales.png")
plt.close()

# Top Countries by Revenue
top_countries = df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False).head(5)
print("\nTop Countries:\n", top_countries)

# Most Frequent Customers
top_customers = df["CustomerID"].value_counts().head(5)
print("\nTop Customers:\n", top_customers)

# Average Order Value
avg_order = df["TotalPrice"].mean()
print("\nAverage Order Value:", avg_order)

# ---------------------------
# MULTIVARIATE ANALYSIS
# ---------------------------

# Correlation Heatmap
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("charts/correlation.png")
plt.close()

# Scatter Plot (Quantity vs TotalPrice)
plt.figure()
plt.scatter(df["Quantity"], df["TotalPrice"])
plt.xlabel("Quantity")
plt.ylabel("TotalPrice")
plt.title("Quantity vs TotalPrice")
plt.savefig("charts/scatter.png")
plt.close()

# ---------------------------
# FINAL MESSAGE
# ---------------------------
print("\nEDA Completed Successfully!")
print("Charts saved in 'charts' folder.")