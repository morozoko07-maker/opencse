---
title: Revision sheet
---

# Revision sheet — Mathematics III

A last-week sheet for BCS301 statistics. Each module ends with model-paper questions.

## Exam pattern

CIE 50 + SEE 50. The model paper is **100 marks in 3 hours: five questions, one per module**, with an internal OR. Modules split 7 + 7 + 6.

## Module 1 — Probability distributions

### Must know

- Discrete: `Σp(x) = 1`; continuous: `∫f(x)dx = 1`.
- Binomial: n trials, constant p, `P = nCr p^r q^(n−r)`.
- Poisson: `P = e^(−λ) λ^r / r!`, λ = np.
- Normal: `Z = (X − μ)/σ`.
- Exponential: `f = λe^(−λx)`, `P(X > x) = e^(−λx)`.
- Poisson approximates the binomial for large n, small p.
- Mean and variance identify the model.
- Subtract table areas for an interval.

| Distribution | Mean | Variance |
|---|---|---|
| Binomial | np | npq |
| Poisson | λ | λ |
| Normal | μ | σ² |
| Exponential | 1/λ | 1/λ² |

### Definitions to reproduce

> A random variable is a real-valued function on the sample space.

> A density satisfies f(x) ≥ 0 and ∫f(x)dx = 1.

### Worked pattern — words to distribution

For successes in n trials use binomial; for a small rate over many trials use Poisson with λ = np. Substitute and answer in context.

## Module 2 — Joint distributions and Markov chains

### Must know

- The joint pmf gives `P(X = x, Y = y)`; marginals are row and column sums.
- Independence needs `p(x, y) = p(x)p(y)` everywhere.
- Stochastic rows are non-negative and sum to 1.
- A regular matrix has a power with all entries positive.
- The fixed vector satisfies `πP = π` and `Σπ = 1`.
- The n-step matrix is `P^n`.
- Long-run questions are solved from `πP = π`.
- The fixed vector does not depend on the starting state.

### Definitions to reproduce

> A stochastic matrix has non-negative entries and every row sums to one.

> A Markov chain is a process in which the next state depends only on the present state.

### Worked pattern — fixed vector

Write `π = (π1, …, πn)`, solve `πP = π` with `Σπi = 1`, and check every entry lies between 0 and 1.

## Module 3 — Sampling and hypothesis testing

### Must know

- Population mean μ, SD σ; sample mean x̄, SD s.
- Standard error is `σ/√n`; without replacement use `√((N−n)/(N−1))`.
- A statistic is a function of the sample.
- H0 states no difference; H1 states the claim.
- Type I rejects a true H0; Type II accepts a false one.
- Significance level is the Type I probability, 5% or 1%.
- Large-sample mean test: `z = (x̄ − μ)/(σ/√n)`.
- Proportion limits: `p ± z√(pq/n)`.

### Definitions to reproduce

> The null hypothesis is the hypothesis of no difference, tested against the alternative.

> A Type I error rejects a true null hypothesis; a Type II error accepts a false one.

## Module 4 — t-test and chi-square

### Must know

- Use t when σ is unknown: `t = (x̄ − μ)/(s/√n)`, n − 1 df.
- Two means: pool variances, `n1 + n2 − 2` df.
- Paired data: test the mean difference.
- Goodness of fit: `χ² = Σ(O−E)²/E`.
- df are `n − 1 − k`, for k parameters estimated.
- Expected frequencies preserve the total; merge classes until each E is 5 or more.
- Reject H0 if the calculated value exceeds the table value.
- A small t supports H0; a large one rejects it.

### Definitions to reproduce

> The chi-square test measures how far observed frequencies depart from those expected under a hypothesis.

> Degrees of freedom is the number of independent observations used to estimate a statistic.

### Worked pattern — goodness of fit

Compute expected frequencies as total × probability and merge small classes. Sum `(O−E)²/E`, find df, and compare with the printed table value.

## Module 5 — Curve fitting, correlation and regression

### Must know

- Least squares minimises squared vertical deviations.
- For `y = a + bx`: `Σy = na + bΣx`, `Σxy = aΣx + bΣx²`.
- For a parabola add the equations for `Σx²y` and `Σx⁴`.
- For `y = ax^b`, fit a line to log x and log y.
- r lies between −1 and 1; its sign follows the slope.
- Regression of y on x: `y − ȳ = byx(x − x̄)`.
- Rank correlation: `ρ = 1 − 6Σd²/(n(n²−1))`.
- Correlation is association, not causation.

### Definitions to reproduce

> Correlation is the degree of linear relationship between two variables.

> The coefficient of correlation measures the strength and direction of a linear relationship.

## Last 24 hours

1. Write the four distribution formulae with means and variances.
2. Do one Poisson and one normal-area problem.
3. Solve a two-state Markov fixed vector.
4. Compute a standard error with and without replacement.
5. Run one t-test and one chi-square test.
6. Fit a line and a power curve; find r and the regression line.
7. Compute a rank correlation, with the tie correction.

## Question bank

**Module 1**

1. The pmf of a variate is given by a table. Find the constant that makes it valid, then the mean and variance. [7]
2. In a factory 0.002 of blades are defective, packed in tens. Using Poisson, find packets with no, one and two defectives in 10,000. [7]

**Module 2**

3. From the given joint distribution, find the marginals, their means, and test independence. [10]
4. Define stochastic matrix and probability vector. Show the given matrix is regular and find its fixed vector. [10]

**Module 3**

5. A population is 3, 7, 11, 15. Find the mean and SD of the sampling distribution of means for samples of size 2 without replacement. [8]
6. A coin is tossed 400 times and heads appear 216 times. Test at 5% whether it is unbiased. [6]

**Module 4**

7. Ten heights are given. Test whether the mean is 66 inches, given t0.05(9) = 2.262. [7]
8. Fit a Poisson distribution to the given frequencies and test goodness of fit at 5%, given χ²0.05 = 7.82 for 3 df. [7]

**Module 5**

9. Fit a parabola `y = a + bx + cx²` to the given data by least squares. [7]
10. Calculate the correlation coefficient and obtain both regression lines. [7]

*Source: `BCS301_Model_QP.pdf`. Marks are as printed in that paper.*
