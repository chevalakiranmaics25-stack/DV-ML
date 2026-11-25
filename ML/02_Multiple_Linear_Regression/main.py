"""Multiple Linear Regression using scikit-learn's diabetes dataset."""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def main():
    data = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=.2, random_state=42)
    model = LinearRegression().fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Features:", ", ".join(data.feature_names))
    print(f"MAE: {mean_absolute_error(y_test, pred):.2f}")
    print(f"MSE: {mean_squared_error(y_test, pred):.2f}")
    print(f"R2: {r2_score(y_test, pred):.3f}")
    plt.scatter(y_test, pred, alpha=.7)
    limits = [min(y_test.min(), pred.min()), max(y_test.max(), pred.max())]
    plt.plot(limits, limits, "r--", label="Ideal prediction")
    plt.xlabel("Actual target"); plt.ylabel("Predicted target")
    plt.title("Multiple Linear Regression: Diabetes dataset")
    plt.legend(); plt.tight_layout(); plt.savefig("output.png", dpi=150)
    print("Saved plot: output.png")

if __name__ == "__main__":
    main()
