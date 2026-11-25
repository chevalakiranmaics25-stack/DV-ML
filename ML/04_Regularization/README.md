# 4. Regression Models with Regularization

**Aim:** Compare ordinary Linear Regression with Ridge (L2) and Lasso (L1) regularization.

**Dataset:** Diabetes dataset bundled with scikit-learn.

**Run:** `python ML/04_Regularization/main.py`

**Output:** Test MSE and R² for all three models; `output.png` compares their R² scores.

**Conclusion:** Ridge shrinks coefficients; Lasso can shrink some coefficients to zero. Regularization can reduce overfitting, with performance depending on alpha.
