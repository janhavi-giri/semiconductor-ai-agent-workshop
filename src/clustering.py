from dataclasses import dataclass
import pandas as pd
from sklearn.cluster import KMeans,DBSCAN,AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from .synthetic_data import FEATURES
@dataclass
class ClusterResult: labels: object; silhouette: float|None; coordinates: object
def cluster_data(data,algorithm="kmeans",clusters=4):
    x=StandardScaler().fit_transform(data[FEATURES]); name=algorithm.lower()
    if name=="kmeans": labels=KMeans(n_clusters=clusters,random_state=42,n_init=10).fit_predict(x)
    elif name=="dbscan": labels=DBSCAN(eps=1.25,min_samples=8).fit_predict(x)
    elif name=="hierarchical": labels=AgglomerativeClustering(n_clusters=clusters).fit_predict(x)
    else: raise ValueError("Use kmeans, dbscan, or hierarchical")
    score=silhouette_score(x,labels) if len(set(labels))>1 else None
    return ClusterResult(labels,score,PCA(n_components=2).fit_transform(x))
def find_optimal_k(data):
    x=StandardScaler().fit_transform(data[FEATURES]); rows=[]
    for k in range(2,9):
        labels=KMeans(n_clusters=k,random_state=42,n_init=10).fit_predict(x); rows.append({"clusters":k,"silhouette":silhouette_score(x,labels)})
    return pd.DataFrame(rows)
def summarize_clusters(data,labels):
    d=data.copy(); d["Cluster"]=labels; return d.groupby("Cluster")[FEATURES].mean().round(3)
