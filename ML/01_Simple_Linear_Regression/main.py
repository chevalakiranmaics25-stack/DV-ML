"""Simple Linear Regression on reproducible synthetic data."""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def main():
    rng = np.random.default_rng(42)
    X = np.arange(1, 101, dtype=float).reshape(-1, 1)
    y = 4.5 * X.ravel() + 12 + rng.normal(0, 18, len(X))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression().fit(X_train, y_train)
    pred = model.predict(X_test)
    print(f"Intercept: {model.intercept_:.3f}")
    print(f"Slope: {model.coef_[0]:.3f}")
    print(f"Test MSE: {mean_squared_error(y_test, pred):.3f}")
    print(f"Test R2: {r2_score(y_test, pred):.3f}")
    order = np.argsort(X.ravel())
    plt.scatter(X, y, alpha=.55, label="Observed data")
    plt.plot(X[order], model.predict(X[order]), color="red", label="Regression line")
    plt.xlabel("Study hours (example feature)")
    plt.ylabel("Score (example target)")
    plt.title("Simple Linear Regression")
    plt.legend(); plt.tight_layout(); plt.savefig("output.png", dpi=150)
    print("Saved plot: output.png")

if __name__ == "__main__":
    main()
