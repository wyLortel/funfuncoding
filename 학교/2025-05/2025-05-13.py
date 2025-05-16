import numpy as np
# import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = np.loadtxt("old_faithful_geyser.csv" , delimiter="," , skiprows=1)

X = data

KMeans = KMeans(n_clusters=2 , random_state=0)
KMeans.fit(X)

lables = KMeans.labels_
centroids = KMeans.cluster_centers_

print(f"SSE : {KMeans.inertia_}")