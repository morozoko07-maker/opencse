---
title: Revision sheet
---

# Revision sheet — Mathematics for CSE Stream I

Banks cover Modules 1–2; the IA-2 sheet names Modules 3 and 5. The syllabus table is blank, so Module 4 is omitted. No marks printed.

## Module 1 — Calculus

### Must know

- Polar coordinates: x = r cos θ, y = r sin θ; the angle φ between the radius vector and the tangent satisfies tan φ = r dθ/dr.
- The pedal equation connects p, the perpendicular from the pole to the tangent, with r: 1/p² = u² + (du/dθ)², where u = 1/r.
- Angle of intersection: find φ₁ and φ₂ at the common point, then tan α = |(tan φ₁ − tan φ₂)/(1 + tan φ₁ tan φ₂)|.
- Radius of curvature in Cartesian form: ρ = [1 + (dy/dx)²]^(3/2) / (d²y/dx²).
- Radius of curvature in polar form: ρ = (r² + r₁²)^(3/2) / (r² + 2r₁² − r r₂), with r₁ = dr/dθ and r₂ = d²r/dθ².

### Definitions to reproduce

> The pedal equation of a curve is a relation between the length of the perpendicular from the pole to the tangent and the distance of the point of contact from the pole.

> The radius of curvature at a point is the radius of the circle that touches the curve there and has the same curvature.

## Module 2 — Series expansion and multivariable calculus

### Must know

- Limits of the form 1^∞, 0^0 and ∞^0 are evaluated by taking logarithms and then using L'Hôpital's rule or standard limits.
- Maclaurin series: f(x) = f(0) + x f′(0) + (x²/2!) f″(0) + ⋯.
- Taylor series about (a, b) uses the same partial derivatives at the point, with increments (x − a) and (y − b).
- Chain rule: if u = f(x, y) and x, y depend on t, then du/dt = u_x x′ + u_y y′.
- Euler's theorem for a homogeneous function of degree n: x u_x + y u_y = n u.
- For maxima and minima of f(x, y), solve f_x = 0 and f_y = 0, then test rt − s²: positive with r > 0 gives a minimum, positive with r < 0 a maximum, negative a saddle point.

### Definitions to reproduce

> A function f(x, y) is homogeneous of degree n if f(tx, ty) = tⁿ f(x, y) for every t > 0.

> The Jacobian of the transformation from (x, y) to (u, v) is the determinant of the matrix of partial derivatives ∂u/∂x, ∂u/∂y, ∂v/∂x and ∂v/∂y.

## Module 3 — Ordinary differential equations

### Must know

- The order is the highest derivative present; the degree is the power of the highest derivative after the equation is made polynomial in derivatives.
- A first-order equation is separable when it can be written f(y) dy = g(x) dx.
- A homogeneous first-order equation is solved by putting y = vx.
- A linear first-order equation dy/dx + P y = Q has integrating factor e^(∫P dx).
- The IA-2 case study uses a series LR circuit, whose current satisfies a first-order linear equation with a constant driving voltage.

### Definitions to reproduce

> The order of a differential equation is the order of the highest derivative occurring in it.

> An integrating factor is a function which, when multiplied into a linear differential equation, makes the left-hand side an exact derivative.

## Module 5 — Linear algebra

### Must know

- The rank of a matrix is the number of non-zero rows in its row-echelon form.
- Elementary row operations do not change the rank or the solution set of a linear system.
- A system AX = B is consistent when the rank of A equals the rank of the augmented matrix [A|B].
- Gauss elimination reduces [A|B] to echelon form and uses back substitution; Gauss-Jordan continues to reduced echelon form.
- The IA-2 sheet limits this module to the Gauss-Jordan method, so revise that method first.

### Definitions to reproduce

> The rank of a matrix is the order of the largest non-zero minor of the matrix.

> A system of linear equations is consistent if it has at least one solution, and inconsistent if it has none.

## Last 24 hours

1. Derive the pedal equation for r = a(1 + cos θ).
2. Find the radius of curvature of x³ + y³ = 3axy at (3a/2, 3a/2).
3. Expand eˣ log(1 + x) by Maclaurin's series to four terms.

## Question bank

1. With usual notations, prove that tan φ = r dθ/dr and 1/p² = u² + (du/dθ)².
2. Find the angle of intersection of r = a(1 − cos θ) and r = 2a cos θ.
3. Find the radius of curvature of x³ + y³ = 3axy at (3a/2, 3a/2).
4. Obtain the Maclaurin expansion of e^(sin x).
5. Expand eˣ log(1 + x) by Maclaurin's expansion up to fourth-degree terms.
6. If u = f(x + ay) + g(x − ay), show that ∂²u/∂y² = a² ∂²u/∂x².
7. If u = x(1 − y) and v = xy, find J = ∂(u,v)/∂(x,y) and J′ = ∂(x,y)/∂(u,v); verify JJ′ = 1.

*Sources: `Question bank Module 1 and Module 2.pdf`, `proper Question Bank from college.pdf` and `first pink book assignmentModule 1 .pdf`; titles from `Case study_CSE_AIML_EEE.pdf`.*
