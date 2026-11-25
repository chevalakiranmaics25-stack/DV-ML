"""K-means clustering on reproducible synthetic 2D data."""
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

def main():
    X, _ = make_blobs(n_samples=400, centers=4, cluster_std=1.0, random_state=42)
    X = StandardScaler().fit_transform(X)
    model = KMeans(n_clusters=4, random_state=42, n_init=10)
    labels = model.fit_predict(X)
    print("Cluster centers (scaled):")
    print(model.cluster_centers_)
    print(f"Inertia: {model.inertia_:.2f}")
    print(f"Silhouette score: {silhouette_score(X, labels):.3f}")
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=25, alpha=.8)
    plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], c="red", marker="X", s=180, label="Centroids")
    plt.xlabel("Feature 1 (scaled)"); plt.ylabel("Feature 2 (scaled)")
    plt.title("K-means Clustering (k=4)"); plt.legend()
    plt.tight_layout(); plt.savefig("output.png", dpi=150)
    print("Saved plot: output.png")

if __name__ == "__main__":
    main()
