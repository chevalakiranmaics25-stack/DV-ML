# 5. Dimensionality Reduction using PCA

**Aim:** Transform four numeric features into two principal components.

**Dataset:** Iris dataset bundled with scikit-learn.

**Method:** Standardize features, then apply PCA with two components.

**Run:** `python ML/05_PCA/main.py`

**Output:** Explained-variance ratios and `output.png` scatter plot of the two components, colored by species.

**Conclusion:** PCA creates uncorrelated directions that capture as much variance as possible; the printed ratio indicates information retained by the two-dimensional representation.
