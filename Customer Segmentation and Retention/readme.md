Customer Segmentation & Retention Dashboard (RFM + KMeans)
📌 Project Overview
Businesses spend heavily on acquiring customers, but retaining them is more profitable in the long run.
This project applies RFM analysis and KMeans clustering to segment customers, enabling targeted retention strategies.

The results are visualized in an interactive Power BI dashboard that highlights customer behavior, segment contributions, and business recommendations.

🎯 Objectives
Segment customers using Recency, Frequency, Monetary (RFM) analysis.

Apply KMeans clustering to group customers into meaningful segments.

Provide business insights & retention strategies for each segment.

Build an interactive Power BI dashboard to visualize customer behavior.

📂 Project Structure
bash
Copy
Edit
├── data.csv                      # Raw Online Retail dataset
├── segmented_customers.csv        # Final output with clusters & segments
├── customer_segmentation.ipynb    # Jupyter Notebook (analysis + clustering)
├── customer_segmentation.py       # Python script version of notebook
├── README.md                      # Project documentation (this file)
🛠️ Methodology
Data Cleaning

Removed returns, missing IDs, negative/zero quantities.

Standardized fields, created TotalPrice.

Feature Engineering (RFM)

Recency = Days since last purchase

Frequency = Number of invoices

Monetary = Total spending

Clustering

Scaled features with StandardScaler.

Used KMeans clustering (evaluated with Silhouette, Calinski-Harabasz, Davies-Bouldin).

Visualized with PCA 2D projection.

Segmentation

Assigned business-friendly labels:

💎 High-Value Loyal

🌱 Potential Loyalist

⚠️ At-Risk

❄️ Low-Value

Visualization (Power BI)

Built KPI cards, bar charts, scatter plots, and heatmaps.

Added slicers for interactivity.

📊 Power BI Dashboard
Key Features:

KPIs (Cards)

Total Customers, Total Revenue, Avg Revenue/Customer, High-Value Customers

Charts

Customers per Segment

Revenue Contribution by Segment (% of total revenue)

Customer Value Map (Recency vs Frequency, size = Monetary)

Segment Averages (Recency, Frequency, Monetary)


💡 Insights & Recommendations
High-Value Loyal: Reward with loyalty programs, VIP offers.

Potential Loyalist: Target with upselling, personalized discounts.

At-Risk: Win-back campaigns, “We miss you” emails.

Low-Value: Use broad, low-cost marketing (social, newsletters).

Business Impact

Improved retention

Reduced churn

Optimized marketing budget

Increased Customer Lifetime Value (CLV)

🚀 How to Run
1. Python Analysis
bash
Copy
Edit
# Run Jupyter Notebook
jupyter notebook customer_segmentation.ipynb

# Or run Python script
python customer_segmentation.py
2. Power BI Dashboard
Open Power BI Desktop.

Import segmented_customers.csv.

Recreate visuals using provided instructions (or theme JSON).

📈 Tech Stack
Python → Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

Clustering → KMeans, PCA

BI Tool → Power BI

📜 Dataset
Online Retail Dataset (UK transactions, 2010–2011).
Source: UCI Machine Learning Repository.