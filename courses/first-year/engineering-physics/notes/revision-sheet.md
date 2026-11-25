---
title: Revision sheet
---

# Revision sheet — Engineering Physics

Module names follow the 2022 scheme syllabus. The only marked set is the Module 1 assignment, out of 10; others come from the quantum-mechanics notes and carry no marks.

## Exam pattern

The SEE is 100 marks in three hours, scaled to 50: five full questions of 20 marks, one per module. Theory CIE is 30.

## Module 1 — Laser and optical fibres

### Must know

- Induced absorption raises an atom from E₁ to E₂; spontaneous emission needs no stimulus; stimulated emission is triggered by a photon of the same energy.
- Einstein's coefficients are B₁₂, A₂₁ and B₂₁; at equilibrium B₁₂ = B₂₁ and A/B = 8πhν³/c³.
- Laser action needs population inversion, a metastable state and an optical resonator.
- A semiconductor diode laser is a heavily doped p-n junction; electron-hole recombination emits light.
- Acceptance angle: NA = sin θₐ = √(n₁² − n₂²). The V-number is V = (2πa/λ)√(n₁² − n₂²), and V < 2.405 gives single-mode operation.

### Definitions to reproduce

> A laser produces a coherent, monochromatic and highly directional beam by stimulated emission.

> Numerical aperture is the sine of the largest acceptance angle for which light is totally internally reflected along the core.

## Module 2 — Quantum mechanics

### Must know

- de Broglie: λ = h/p = h/√(2mE) for a non-relativistic particle.
- Heisenberg: Δx Δp ≥ ħ/2, which forbids an electron from staying inside a nucleus.
- The wave function is complex; |ψ|² is the probability density and ∫|ψ|² dV = 1 for a normalised state.
- Time-independent Schrödinger equation: −(ħ²/2m) d²ψ/dx² + Vψ = Eψ. For an infinite well of width a, Eₙ = n²h²/(8ma²); the lowest energy is not zero.

### Definitions to reproduce

> A wave function describes the state of a quantum system; its squared modulus gives the probability density of finding the particle at a point.

> The uncertainty principle states that position and momentum cannot both be known exactly at the same time.

## Module 3 — Quantum computing

### Must know

- A qubit is α|0⟩ + β|1⟩, with |α|² + |β|² = 1; the Bloch sphere pictures a pure state.
- Single-qubit gates: X (NOT), Z, Hadamard H, phase S and T. Hadamard turns |0⟩ into (|0⟩ + |1⟩)/√2.
- Two-qubit gates include CNOT, controlled-Z, swap and Toffoli; CNOT flips the target when the control is 1.
- Superposition and interference give the advantage; measurement collapses the state. Moore's law doubles transistor counts about every two years.

### Definitions to reproduce

> A qubit is a two-state quantum system that can exist in a superposition of |0⟩ and |1⟩.

> A quantum gate is a unitary operation that transforms the state of one or more qubits.

## Module 4 — Physics in computing

### Must know

- Frames per second sets the number of images shown each second; a higher rate gives smoother motion.
- The odd rule: a body falling from rest under gravity covers distances in the ratio 1:3:5:7 in successive equal intervals.
- Statistical physics: descriptive statistics, Poisson and normal distributions, and Monte Carlo sampling.

### Definitions to reproduce

> The odd rule states that a body starting from rest under constant acceleration covers distances in the ratio of odd numbers in successive equal time intervals.

## Module 5 — Superconductivity

### Must know

- A superconductor has zero resistance below Tc; the Meissner effect expels magnetic flux from its interior.
- The critical field Hc destroys superconductivity and falls to zero at Tc.
- Type I has one critical field and a complete Meissner effect; Type II has two critical fields and allows flux vortices between them.
- BCS theory pairs electrons through phonons. A Josephson junction is a thin barrier between two superconductors, and a SQUID uses two such junctions to measure tiny fields.
- Uses include MRI magnets, maglev trains and quantum circuits.

### Definitions to reproduce

> A superconductor conducts electricity with zero resistance below a critical temperature.

> The Meissner effect is the complete expulsion of magnetic field lines from a superconductor below its critical temperature.

## Last 24 hours

1. Draw the energy-level diagram for the three radiative processes.
2. Derive the numerical aperture and do one V-number calculation.
3. Write the infinite-well energies and wave functions.

## Question bank

1. With a neat sketch, write a note on acceptance angle and derive the condition for propagation inside an optical fibre.
2. Write a note on how lasers are used in barcode readers and laser printers, and mention the type used in each.
3. State Heisenberg's uncertainty principle and show that electrons cannot reside inside the nucleus during beta decay.
4. A 10 km fibre link has a loss of 1.5 dB/km and a connector loss of 0.5 dB every km. Find the minimum launch power for 0.5 mW at the detector.
5. Calculate the numerical aperture, V-number and number of modes for a fibre with core diameter 45 μm, n₁ = 1.41, n₂ = 1.40 and λ = 820 nm.
6. Derive the time-independent Schrödinger equation and state the conditions on ψ.
7. Set up the Schrödinger equation for a particle in a one-dimensional infinite well and obtain its eigenvalues and eigenfunctions.

*Sources: `phy big assignment.pdf` (1–5, out of 10); `quantum notes official.pdf` (6–7). No per-question marks.*
