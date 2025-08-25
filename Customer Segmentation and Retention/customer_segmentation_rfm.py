# customer_segmentation_final.py
# End-to-end Customer Segmentation with RFM + KMeans

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn.decomposition import PCA

# --- Config ---
DATA_PATH = "data.csv"
EXPORT_CSV = "segmented_customers.csv"
RANDOM_STATE = 42
N_CLUSTERS = 4

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 120)

# --- Load ---
df = pd.read_csv(DATA_PATH, encoding="ISO-8859-1")
print("Original shape:", df.shape)

# --- Clean ---
df.columns = [c.strip() for c in df.columns]
df = df.dropna(subset=['CustomerID'])
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
df['CustomerID'] = df['CustomerID'].astype(int)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
print("Cleaned shape:", df.shape)

# --- RFM ---
reference_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
rfm = (
    df.groupby('CustomerID')
      .agg(
          Recency=('InvoiceDate', lambda x: (reference_date - x.max()).days),
          Frequency=('InvoiceNo', 'nunique'),
          Monetary=('TotalPrice', 'sum')
      )
      .astype({'Recency': int, 'Frequency': int, 'Monetary': float})
)

p99 = rfm['Monetary'].quantile(0.99)
rfm['Monetary_capped'] = np.where(rfm['Monetary'] > p99, p99, rfm['Monetary'])
rfm_for_model = rfm[['Recency','Frequency','Monetary_capped']].copy()

# --- Scale ---
scaler = StandardScaler()
X = scaler.fit_transform(rfm_for_model)

# --- Cluster evaluation ---
cluster_range = list(range(2,9))
sil_scores, ch_scores, dbi_scores, inertias = [], [], [], []

for k in cluster_range:
    km = KMeans(n_clusters=k, n_init=10, random_state=RANDOM_STATE)
    labels = km.fit_predict(X)
    sil_scores.append(silhouette_score(X, labels))
    ch_scores.append(calinski_harabasz_score(X, labels))
    dbi_scores.append(davies_bouldin_score(X, labels))
    inertias.append(km.inertia_)

print("Silhouette scores:", [round(s,4) for s in sil_scores])
print("Calinski-Harabasz:", [round(c,2) for c in ch_scores])
print("Davies-Bouldin:", [round(d,4) for d in dbi_scores])
print("Inertias:", [round(i,2) for i in inertias])

# --- Final clustering ---
kmeans = KMeans(n_clusters=N_CLUSTERS, n_init=10, random_state=RANDOM_STATE)
rfm['Cluster'] = kmeans.fit_predict(X)

# --- Label clusters ---
cluster_stats = rfm.groupby('Cluster').agg(
    Recency_mean=('Recency','mean'),
    Frequency_mean=('Frequency','mean'),
    Monetary_mean=('Monetary','mean')
).reset_index()

def min_max_norm(s): return (s - s.min()) / (s.max()-s.min()+1e-9)
score = (1-min_max_norm(cluster_stats['Recency_mean'])) + min_max_norm(cluster_stats['Frequency_mean']) + min_max_norm(cluster_stats['Monetary_mean'])
cluster_stats['Score'] = score

labels = ["High-Value Loyal","Potential Loyalist","At-Risk","Low-Value"]
if len(cluster_stats) > len(labels):
    labels += [f"Segment {i}" for i in range(len(labels), len(cluster_stats))]

cluster_stats = cluster_stats.sort_values('Score', ascending=False).reset_index(drop=True)
cluster_stats['Segment'] = labels[:len(cluster_stats)]
cluster_to_label = dict(zip(cluster_stats['Cluster'], cluster_stats['Segment']))
rfm['Segment'] = rfm['Cluster'].map(cluster_to_label)

print("Cluster summary:")
print(cluster_stats)

# --- Export ---
out = rfm.reset_index()[['CustomerID','Recency','Frequency','Monetary','Cluster','Segment']]
out.to_csv(EXPORT_CSV, index=False)
print(f"✅ Exported {EXPORT_CSV}")
