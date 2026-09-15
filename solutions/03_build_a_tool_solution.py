def lowest_yield_cluster(data,labels):
    d=data.copy(); d["Cluster"]=labels; means=d.groupby("Cluster")["Yield_Pct"].mean(); c=int(means.idxmin()); return f"Cluster {c} has mean synthetic yield {means.loc[c]:.2f} percent."
