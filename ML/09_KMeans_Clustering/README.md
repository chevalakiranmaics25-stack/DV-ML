# 9. K-means Clustering

**Aim:** Group observations into four clusters without using class labels.

**Dataset:** Reproducible two-dimensional synthetic blobs (seed 42).

**Algorithm:** KMeans with k=4 and 10 initializations.

**Run:** `python ML/09_KMeans_Clustering/main.py`

**Output:** Cluster centers, inertia, silhouette score and `output.png` scatter plot with centroids.

**Conclusion:** K-means assigns each observation to its nearest centroid and updates centroids iteratively. Inertia measures within-cluster squared distance; silhouette score measures separation and cohesion.
