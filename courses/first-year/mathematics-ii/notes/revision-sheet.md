---
title: Revision sheet
---

# Revision sheet — Mathematics for CSE Stream II

The model paper supplies the marks; the bank supplies extra practice. The formula handbook is allowed, so revise method, not memorised formulae.

## Exam pattern

The BMSIT model paper gives 100 marks in 3 hours: five full questions, one per module. Each is 20 marks (8 + 8 + 4) with an internal OR. The VTU formula handbook is permitted. The README gives CIE 50 + SEE 50.

## Module 1 — Integral calculus

### Must know

- Take double-integral limits from the region; reverse the order when the given order is awkward.
- Polar form: x = r cos θ, y = r sin θ, dx dy = r dr dθ.
- Area = ∬ dA; volume = ∬ z dx dy or ∭ dV.
- Γ(n + 1) = nΓ(n), Γ(1/2) = √π; B(m, n) = Γ(m)Γ(n)/Γ(m + n).

### Definitions to reproduce

> The Beta function is B(m, n) = ∫₀¹ xᵐ⁻¹(1 − x)ⁿ⁻¹ dx for m, n > 0.

## Module 2 — Vector calculus

### Must know

- Directional derivative of φ along a unit vector â is ∇φ · â.
- Solenoidal means ∇ · F = 0. Irrotational means ∇ × F = 0, and then F = ∇φ.
- Scale factors hᵢ = |∂r/∂uᵢ|. Cylindrical: hρ = 1, hφ = ρ, hz = 1. Spherical: hr = 1, hθ = r, hφ = r sin θ.

### Definitions to reproduce

> A vector field is irrotational if its curl is zero; it is then the gradient of a scalar potential.

## Module 3 — Vector spaces and linear transformations

### Must know

- A vector space is closed under addition and scalar multiplication and satisfies the eight axioms.
- A subspace contains the zero vector and is closed under both operations.
- Linear independence: c₁v₁ + … + cₙvₙ = 0 forces every cᵢ = 0.
- A basis is a linearly independent spanning set; its size is the dimension.
- A linear transformation satisfies T(u + v) = T(u) + T(v) and T(cu) = cT(u).
- Kernel maps to zero; range is the set of images; rank + nullity = dim(domain).

### Definitions to reproduce

> The nullity of a linear transformation is the dimension of its kernel.

## Module 4 — Numerical methods: roots, interpolation and integration

### Must know

- Regula falsi: x₂ = [a f(b) − b f(a)] / [f(b) − f(a)], keeping the sign-change bracket.
- Newton–Raphson: xₙ₊₁ = xₙ − f(xₙ)/f′(xₙ); needs a good start and f′ ≠ 0.
- Trapezoidal: (h/2)[y₀ + yₙ + 2(y₁ + … + yₙ₋₁)].
- Simpson 1/3: (h/3)[y₀ + yₙ + 4(odd ordinates) + 2(even ordinates)], even number of intervals.
- Simpson 3/8: (3h/8)[y₀ + yₙ + 3(remaining odd) + 2(remaining even)], multiple of three intervals.

### Definitions to reproduce

> Interpolation estimates a function value between known data points.

## Module 5 — Numerical solution of ordinary differential equations

### Must know

- Taylor series method differentiates y′ repeatedly and substitutes the initial condition.
- Modified Euler predicts with Euler and corrects with the average of slopes.
- RK4: k₁ = hf(x, y), k₂ = hf(x + h/2, y + k₁/2), k₃ = hf(x + h/2, y + k₂/2), k₄ = hf(x + h, y + k₃), y₁ = y + (k₁ + 2k₂ + 2k₃ + k₄)/6.
- Milne uses a predictor from four earlier values and a Simpson-type corrector.
- Keep a table of x, y and f(x, y); most lost marks are arithmetic.

### Definitions to reproduce

> A predictor–corrector method estimates the next value first and then improves it with an implicit formula.

## Last 24 hours

1. Do one change-of-order integral and one polar area.
2. Prove that the intersection of two subspaces is a subspace.
3. Do one Regula falsi and one Newton–Raphson root to four decimals.
4. Do one RK4 step and one Milne corrector; write every intermediate value.

## Question bank

**Module 1**

1. Evaluate ∫₁² ∫₃⁴ (xy + eʸ) dy dx. [7]
2. Find by double integration the area between y² = 4ax and x² = 4ay. [7]

**Module 2**

3. Find the directional derivative of φ = x²yz + 4xz² at (1, −2, −1) in the direction of 2î − ĵ − 2k̂. [7]
4. Prove that the spherical coordinate system is orthogonal. [6]

**Module 3**

5. Let W be the subset of R³ of vectors (a, a², b). Is W a subspace? [7]
6. Find the kernel and range of T(x, y, z) = (x + y, z) from R³ to R². [6]

**Module 4**

7. Find an approximate root of xeˣ = 3 by Regula falsi, carrying out three iterations. [7]
8. Given sin 45° = 0.7071, sin 50° = 0.7660, sin 55° = 0.8192 and sin 60° = 0.8660, find sin 52° by Newton's forward interpolation formula. [7]

**Module 5**

9. Find y at x = 0.1 and x = 0.2 to five decimal places by Taylor's series from dy/dx = x²y − 1, y(0) = 1. [7]
10. Using fourth-order Runge–Kutta, find y(0.1) for dy/dx = 3eˣ + 2y, y(0) = 0, h = 0.1. [7]

*Source: `model paper for SEE (VTU).pdf` and `BMATS201_Question bank_9_06_23.pdf`. Marks are from the VTU paper. The multiple-integral and vector-calculus note PDFs are scans.*
