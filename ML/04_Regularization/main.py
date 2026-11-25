"""Compare Linear, Ridge and Lasso regression on the diabetes dataset."""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def main():
    data = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=.2, random_state=42)
    models = {
        "Linear": LinearRegression(),
        "Ridge": make_pipeline(StandardScaler(), Ridge(alpha=1.0)),
        "Lasso": make_pipeline(StandardScaler(), Lasso(alpha=.1, max_iter=10000)),
    }
    scores = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        scores[name] = r2_score(y_test, pred)
        print(f"{name:8s} MSE={mean_squared_error(y_test, pred):.2f}  R2={scores[name]:.3f}")
    plt.bar(scores.keys(), scores.values())
    plt.ylabel("Test R²"); plt.ylim(min(0, min(scores.values())-.1), 1)
    plt.title("Regression model comparison")
    plt.tight_layout(); plt.savefig("output.png", dpi=150)
    print("Saved plot: output.png")

if __name__ == "__main__":
    main()
