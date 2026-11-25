"""Support Vector Machine classification on the breast cancer dataset."""
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def main():
    data = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=.2, stratify=data.target, random_state=42)
    model = make_pipeline(StandardScaler(), SVC(kernel="rbf", C=1.0, gamma="scale"))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, pred):.3f}")
    print(classification_report(y_test, pred, target_names=data.target_names))
    ConfusionMatrixDisplay.from_predictions(y_test, pred, display_labels=data.target_names, cmap="Purples")
    plt.title("SVM — Confusion Matrix")
    plt.tight_layout(); plt.savefig("output.png", dpi=150)
    print("Saved plot: output.png")

if __name__ == "__main__":
    main()
