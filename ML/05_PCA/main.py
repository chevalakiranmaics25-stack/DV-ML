"""Reduce the Iris dataset to two principal components."""
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def main():
    data = load_iris()
    X = StandardScaler().fit_transform(data.data)
    pca = PCA(n_components=2)
    components = pca.fit_transform(X)
    print("Explained variance ratio:", pca.explained_variance_ratio_)
    print(f"Total variance retained: {pca.explained_variance_ratio_.sum():.3f}")
    for label, name in enumerate(data.target_names):
        mask = data.target == label
        plt.scatter(components[mask, 0], components[mask, 1], label=name, alpha=.75)
    plt.xlabel("Principal component 1"); plt.ylabel("Principal component 2")
    plt.title("PCA on Iris dataset"); plt.legend()
    plt.tight_layout(); plt.savefig("output.png", dpi=150)
    print("Saved plot: output.png")

if __name__ == "__main__":
    main()
