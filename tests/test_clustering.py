from src.synthetic_data import generate_wafer_data
from src.clustering import cluster_data
def test_labels_match_rows():
    d=generate_wafer_data(120); assert len(cluster_data(d,"kmeans",4).labels)==120
