"""Decision Tree classification on the real-world Wine dataset."""
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

def main():
    data = load_wine()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=.2, stratify=data.target, random_state=42)
    model = DecisionTreeClassifier(max_depth=4, random_state=42)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, pred):.3f}")
    print(classification_report(y_test, pred, target_names=data.target_names))
    fig, ax = plt.subplots(figsize=(16, 9))
    plot_tree(model, feature_names=data.feature_names, class_names=data.target_names, filled=True, rounded=True, fontsize=7, ax=ax)
    plt.title("Decision Tree — Wine dataset")
    plt.tight_layout(); plt.savefig("output.png", dpi=150)
    print("Saved plot: output.png")

if __name__ == "__main__":
    main()
