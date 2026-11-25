---
title: Revision sheet
---

# Revision sheet — Machine Learning

This sheet uses the IA-1 and IA-3 schemes and the module notes. The folder has no current syllabus, so the module headings follow the note sets; confirm the official split with your handout.

## Exam pattern

The README gives CIE 50 + SEE 50. The IA-1 scheme marks each full question out of 10; the IA-3 paper is headed 40 marks. Marks below appear only where the scheme prints them.

## Module 1 — Learning foundations and concept learning

### Must know

- Machine learning builds models from data rather than hand-written rules. A well-posed problem states the task, performance measure and training experience.
- Supervised learning uses labelled data; unsupervised learning finds structure in unlabelled data; semi-supervised learning mixes a little labelled with much unlabelled data.
- Concept learning infers a Boolean function from examples. A hypothesis is a conjunction of attribute constraints; `?` means any value and `∅` means none.
- Find-S starts with the most specific hypothesis and generalises it on each positive example. It ignores negatives, so it can fit noise.
- Candidate elimination keeps the specific boundary S and the general boundary G; the version space is every hypothesis between them.
- Common challenges: data quality, overfitting, underfitting, bias, high dimensionality and interpretability.

### Definitions to reproduce

> The version space is the set of all hypotheses consistent with the training examples and the hypothesis space.

## Module 2 — Supervised learning

### Must know

- Simple linear regression fits `y = b0 + b1x` by minimising squared error. Gradient descent updates each weight to lower the cost.
- Model complexity controls the bias-variance trade-off. A high-degree polynomial can overfit; a straight line can underfit. Overfitting gives low training error and high test error.
- k-Nearest Neighbours classifies a point by the majority label among its k nearest neighbours. Scale features and choose k carefully.
- A support vector machine finds the maximum-margin hyperplane; kernels handle non-linear boundaries.
- A decision tree splits on the attribute with the highest information gain. `Gain = entropy(parent) - weighted entropy(children)`.
- A perceptron computes a weighted sum and applies a step function. Backpropagation sends the error backward and updates weights by gradient descent.

### Definitions to reproduce

> Overfitting is learning the training data, including noise, so that performance on unseen data falls.

> Information gain is the reduction in entropy obtained by splitting a data set on an attribute.

## Module 3 — Unsupervised learning

### Must know

- Clustering groups similar points without labels. k-means alternates assignment and centroid updates; it needs k in advance and is sensitive to initial centres.
- DBSCAN groups dense regions and labels sparse points as noise. It finds arbitrary shapes but struggles when density varies.
- PCA finds orthogonal directions of maximum variance and projects data onto the first few components. t-SNE preserves local neighbourhoods for visualisation.
- The curse of dimensionality makes distances less informative as dimensions grow.

### Definitions to reproduce

> Clustering is the task of grouping instances so that members of a group are more similar to each other than to outsiders.

> PCA is a linear transformation that projects data onto orthogonal components ordered by variance.

## Module 4 — Feature engineering

### Must know

- Categorical variables need encoding. Label encoding assigns an integer per category; one-hot encoding creates one binary column per category.
- One-hot avoids false order but increases dimensionality. Label encoding is compact but can imply an order that does not exist.
- Binning turns a continuous variable into intervals. Equal-width bins use the same range; equal-frequency bins use the same count.
- Polynomial features add powers and cross-products to capture non-linearity.
- Log and square-root transforms reduce right skew and stabilise variance.

### Definitions to reproduce

> One-hot encoding represents each category as a separate binary feature.

> Binning converts a continuous variable into a small number of intervals.

## Module 5 — Evaluation and ensembles

### Must know

- Cross-validation splits data into folds, trains on k-1 and tests on the rest. Leave-one-out uses one test point per round.
- Grid search tries every combination in a parameter grid; random search samples combinations and is cheaper in high dimensions.
- Confusion matrix: TP, FP, FN, TN. Accuracy is `(TP+TN)/total`; precision is `TP/(TP+FP)`; recall is `TP/(TP+FN)`; F1 is their harmonic mean.
- Bagging averages models trained on bootstrap samples. Boosting trains models in sequence, each correcting the previous one.

### Definitions to reproduce

> Precision is the fraction of predicted positives that are actually positive.

> Recall is the fraction of actual positives that the model finds.

### Worked pattern

For a confusion-matrix question, write TP, FP, FN and TN, then substitute into each formula. Example: TP = 30, FP = 15, FN = 5, TN = 950; accuracy 0.98, precision 0.667, recall 0.857 and F1 0.750.

## Last 24 hours

1. Write the supervised, unsupervised and semi-supervised comparison table.
2. Run Find-S and candidate elimination on one small table.
3. Compute accuracy, precision, recall and F1 from one confusion matrix.
4. Draw a perceptron and write the weight-update rule.

## Question bank

**Module 1**

1. Differentiate supervised, unsupervised and semi-supervised learning systems by explaining the data and objectives. [10]
2. Identify and explain the key challenges that arise commonly in machine learning. [10]
3. Find the maximally general and specific hypothesis using Find-S, write the algorithm and discuss its issues. [10]

**Module 2**

4. Apply candidate elimination and give the specific and general boundaries for the training examples. [10]
5. Apply ID3 to a loan-approval data set and find the root node, showing entropy and information gain. [10]
6. A COVID data set of 1000 tests has 30 true positives, 15 false positives and 5 false negatives. Draw the confusion matrix and compute accuracy, precision, recall and F1. [10]
7. Construct a perceptron for the OR gate with `w1 = 1.2`, `w2 = 0.6`, threshold 1 and learning rate 0.5, and justify gradient descent. [10]
8. Apply backpropagation with learning rate 0.25 and target output 0, and find the total error. [10]

**Module 3**

9. Define unsupervised learning and list two applications. Differentiate clustering from dimensionality reduction.

**Module 4**

10. Explain the difference between one-hot encoding and label encoding with examples. What is binning?

*Source: `IA1_scheme(ML).pdf` for questions 1, 2 and 4–8, with the printed 10-mark totals; `ML-QP-IA3_scheme.pdf` for questions 1, 3 and the 40-mark paper heading; `ML_BAI503_Sample Questions.pdf` for questions 9–10, which carry no printed marks. `Mod_3_K-Means_Clustering.pdf`, `Mod_3_DBSCAN.pdf` and `Mod_3_tSNE.pdf` are scans and were not used.*
