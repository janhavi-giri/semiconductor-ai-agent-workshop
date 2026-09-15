import json
from .clustering import cluster_data,find_optimal_k,summarize_clusters
class WaferToolkit:
    def __init__(self): self.data=None; self.labels=None
    def load(self,data): self.data=data.copy(); self.labels=None
    def inspect_data(self,_=""):
        return "No data loaded." if self.data is None else json.dumps({"rows":len(self.data),"columns":list(self.data.columns),"missing":int(self.data.isna().sum().sum())})
    def optimal_clusters(self,_=""):
        if self.data is None:return "No data loaded."
        s=find_optimal_k(self.data); b=s.loc[s.silhouette.idxmax()]; return f"Best tested k is {int(b.clusters)} with silhouette {b.silhouette:.3f}."
    def apply_kmeans(self,count="4"):
        if self.data is None:return "No data loaded."
        r=cluster_data(self.data,"kmeans",int(count or 4)); self.labels=r.labels; return f"Created {len(set(r.labels))} clusters with silhouette {r.silhouette:.3f}."
    def analyze_clusters(self,_=""):
        return "Run clustering first." if self.labels is None else summarize_clusters(self.data,self.labels).to_string()
