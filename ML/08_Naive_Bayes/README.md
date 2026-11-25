# 8. Naive Bayes Classifier

**Aim:** Perform binary classification using Bayes' theorem and a conditional-independence assumption.

**Dataset:** Breast cancer Wisconsin dataset bundled with scikit-learn.

**Algorithm:** GaussianNB.

**Run:** `python ML/08_Naive_Bayes/main.py`

**Output:** Accuracy, classification report and `output.png` confusion matrix.

**Conclusion:** Gaussian Naive Bayes models each feature with a class-conditional Gaussian distribution. It is simple and fast, although the independence assumption may not hold exactly.
