---
title: Revision sheet
---

# Revision sheet — Introduction to Electronics Engineering

The model paper sets the shape: five modules, two ten-mark parts each, with a choice inside every module. Numericals appear in power supplies and oscillators, so keep formulae ready.

## Exam pattern

The model paper gives 100 marks in 3 hours: five full questions, one per module, each 10 + 10 with an internal OR. The paper is headed 22ESC143 and first semester but uses the same title; this course is BESCK204C. The README gives CIE 50 + SEE 50.

## Module 1 — Power supplies and amplifiers

### Must know

- Power supply blocks: transformer, rectifier, filter, regulator. Half-wave uses one diode; full-wave uses two with a centre tap; the bridge uses four.
- Ripple factor = AC component / DC component: 1.21 for half-wave, 0.48 for full-wave. Efficiency is 40.5% and 81.2% respectively.
- Zener regulator holds VZ constant in reverse breakdown. Line regulation is the output change for an input change; load regulation is the output change for a load-current change.
- Amplifier gain = output / input; negative feedback lowers gain but improves stability and bandwidth.

### Definitions to reproduce

> A rectifier converts alternating current into pulsating direct current.

> Line regulation is the change in output voltage caused by a change in input voltage, with the load fixed.

## Module 2 — Oscillators and operational amplifiers

### Must know

- Barkhausen criterion: loop gain Aβ = 1 and total loop phase shift is 360°.
- RC phase-shift oscillator uses three RC sections for 180° plus a common-emitter amplifier for the other 180°.
- Ideal op-amp: infinite gain, infinite input impedance, zero output impedance, infinite bandwidth, zero offset.
- Inverting gain = −Rf/Rin; non-inverting gain = 1 + Rf/Rin; voltage follower gain = 1.

### Definitions to reproduce

> The Barkhausen criterion states that an oscillator sustains oscillation when the loop gain is unity and the total loop phase shift is a multiple of 360°.

## Module 3 — Digital electronics

### Must know

- Boolean identities: A + A′ = 1, A·A′ = 0, A + AB = A, A + A′B = A + B. De Morgan: (A + B)′ = A′B′, (AB)′ = A′ + B′.
- NAND and NOR are universal gates; any function can be built from either.
- XOR is 1 when inputs differ; XNOR is its complement. XOR from NAND needs four gates; XNOR needs five.
- Half adder: sum = A ⊕ B, carry = AB. Full adder: sum = A ⊕ B ⊕ Cin, carry = AB + BCin + ACin.
- A full adder is two half adders plus an OR gate.

### Definitions to reproduce

> A universal gate is a gate from which any other logic gate can be constructed; NAND and NOR are universal.

## Module 4 — Embedded systems

### Must know

- An embedded system is a dedicated computer inside a larger product, built for a specific function.
- Classification: small, medium and large; or real-time, stand-alone, networked and mobile.
- Structural elements: processor, memory, I/O ports, timers, interrupts, power supply and software.
- A microprocessor is a general-purpose CPU with external memory and peripherals. A microcontroller integrates CPU, memory, timers and I/O on one chip.

### Definitions to reproduce

> An embedded system is a combination of hardware and software designed to perform a dedicated function within a larger system.

## Module 5 — Electronic applications

### Must know

- Wind turbine: blades convert wind kinetic energy to rotation, the gearbox drives a generator, and power electronics convert the variable AC.
- Available wind power P = ½ρAv³: density, swept area and the cube of wind speed.
- RFID: tag, reader and antenna. The reader interrogates the tag, which returns its stored identity to the host system.

### Definitions to reproduce

> RFID is a wireless identification system in which a reader interrogates a tag carrying a unique identity.

## Last 24 hours

1. Derive the ripple factor and efficiency of the half-wave rectifier.
2. Draw the Zener regulator and explain line and load regulation.
3. Draw the RC phase-shift oscillator and state the Barkhausen condition.
4. Realise XOR and XNOR using NAND gates only.
5. Design a full adder from two half adders.

## Question bank

**Module 1**

1. What is a rectifier? With a neat diagram, explain the half-wave rectifier without a capacitor filter and derive the ripple factor and efficiency. [10]
2. Explain the Zener diode as a voltage regulator and discuss line regulation and load regulation with diagrams. [10]

**Module 2**

3. Explain the Barkhausen criterion and the RC phase-shift oscillator with a circuit diagram and equation. [10]
4. Explain the op-amp applications: inverting amplifier, non-inverting amplifier, adder and integrator, with circuit diagrams and derivations. [10]

**Module 3**

5. Realise two-input XOR and XNOR gates using only NOR gates and only NAND gates. [10]
6. Design a full adder circuit and implement it using two half adders. [10]

**Module 4**

7. Distinguish between a microprocessor and a microcontroller. [10]

**Module 5**

8. With a functional diagram, explain a wind turbine for small power applications and the factors determining available wind power. [10]

*Source: `Model Question Paper_IE_Descriptive.pdf`; marks are from that paper. `1st - assignment.pdf` is a handwritten scan and was not used. `offical TB.pdf` is a scanned textbook with no extractable text.*
