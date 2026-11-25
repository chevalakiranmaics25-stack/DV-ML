# 1. Simple Linear Regression

**Aim:** Fit a straight-line model to predict a continuous target from one input feature.

**Dataset:** Reproducible synthetic data generated in the script (seed 42).

**Algorithm:** `sklearn.linear_model.LinearRegression`.

**Run:** `python ML/01_Simple_Linear_Regression/main.py`

**Output:** Prints intercept, slope, test MSE and R²; saves `output.png` with observed points and fitted regression line.

**Conclusion:** The slope describes the expected target change for a one-unit increase in the feature. R² and MSE summarize test-set fit.
