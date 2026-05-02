\# 📊 Task 2: Exploratory Data Analysis (EDA) \& Business Intelligence



\## 🏢 Internship



\*\*ApexPlanet Software Pvt. Ltd.\*\*



\## 👤 Intern



\*\*Prajyot Wadewale\*\*



\## 🆔 Intern ID



\*\*APSPL2630610\*\*



\---



\# 🎯 Objective



The objective of this task is to uncover patterns, trends, and relationships within the dataset and gain proficiency in data analysis and SQL for solving business problems.



\---



\# 📂 Dataset



\* Dataset: Cleaned E-commerce Dataset (from Task-1)

\* Source: Kaggle (Online Retail Dataset)



\---



\# 🔍 Key Tasks Performed



\## 1️⃣ Descriptive Statistics \& Univariate Analysis



\* Generated summary statistics (mean, median, etc.)

\* Analyzed distributions using histograms and bar charts

\* Identified top products and countries



\---



\## 2️⃣ Business Insights



Answered key business questions:



\* Top 5 products by revenue

\* Monthly sales trend

\* Top countries by revenue

\* Most frequent customers

\* Average order value



\---



\## 3️⃣ Data Visualization



Created visualizations using Python:



\* Sales distribution histogram

\* Top countries bar chart

\* Top products bar chart

\* Monthly sales trend line chart

\* Scatter plot (Quantity vs TotalPrice)

\* Correlation heatmap



\---



\## 4️⃣ Multivariate Analysis



\* Analyzed relationships between variables

\* Used correlation heatmap to identify patterns



\---



\## 🧾 SQL Analysis



Sample business queries:



```sql

\-- Top 5 products by revenue

SELECT Description, SUM(TotalPrice) AS Revenue

FROM data

GROUP BY Description

ORDER BY Revenue DESC

LIMIT 5;



\-- Monthly sales trend

SELECT Month, SUM(TotalPrice) AS TotalSales

FROM data

GROUP BY Month

ORDER BY Month;

```



\---



\# 📊 Key Insights



\* Identified top-performing products contributing to revenue

\* Observed monthly trends in sales

\* Found high-revenue countries

\* Analyzed customer purchasing behavior



\---



\# 🧰 Technologies Used



\* Python (Pandas, Matplotlib, Seaborn)

\* SQL

\* Command Prompt (CMD)



\---



\# 📁 Project Structure



```

Task2\_EDA

│

├── eda\_analysis.py

├── queries.sql

├── cleaned\_ecommerce\_data.csv

├── charts/

└── README.md

```



\---



\# 📈 Output



\* Visual charts for analysis

\* Business insights from dataset

\* SQL query results



\---



\# 🎥 Deliverables



\* ✔️ GitHub Repository (EDA + SQL + Charts)

\* ✔️ LinkedIn Video (5–7 min explanation of insights)



\---



\# 🚀 Key Learnings



\* Data exploration and visualization

\* Extracting business insights from data

\* Writing SQL queries for analysis

\* Understanding relationships between variables



\---



\# 🌟 Conclusion



This task enhanced my ability to analyze real-world datasets and extract meaningful insights using data analytics techniques.



\---



