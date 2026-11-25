---
title: Revision sheet
---
# Revision sheet — Information and Network Security

Information and Network Security (BCS701) is a four-credit course. The 11 September 2025 syllabus sets five modules: classical cryptography, hash functions, random numbers and authentication protocols, key management, and applications.

## Exam pattern

The syllabus gives CIE 50 and SEE 50, with a three-hour SEE. IA papers are 40 marks and mix 5-mark and 10-mark questions.

## Module 1 — Classical cryptography and cryptanalysis

### Must know

- Simple substitution, including Caesar shifts and letter permutations, and frequency analysis against them.
- A cryptosystem is secure when the best known attack is exhaustive key search.
- One-time pad: key as long as the message, truly random, used once; perfect secrecy and practical problems.
- Codebook ciphers and Project VENONA, where repeated pad material allowed partial decryption.
- Taxonomy of cryptography and cryptanalysis.

### Definitions to reproduce

**Cryptography** designs secrecy systems; **cryptanalysis** attempts to break them. A **simple substitution** replaces each plaintext letter by one fixed ciphertext letter. A **one-time pad** combines plaintext with a random key of equal length. A **codebook cipher** replaces words by numbers from a shared book.

### Worked pattern

For `QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD`, `QEB` repeats like `THE`. Q to T is a forward shift of 3, so decrypt by shifting every letter forward by 3. The result is `THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG`.

## Module 2 — Hash functions and related topics

### Must know

- Properties: preimage resistance, second-preimage resistance and collision resistance.
- The birthday problem and the birthday-attack bound of about 2^(n/2) for an n-bit hash.
- Non-cryptographic hashes, Tiger, and HMAC as a keyed message authentication code.
- Uses: password storage, file checksums, commitments and message integrity.

### Definitions to reproduce

A **hash function** maps arbitrary input to a fixed-length digest and should be one-way. A **collision** is two different inputs with the same digest. A **birthday attack** finds a collision after roughly the square root of the output space. **HMAC** is a MAC built from a hash and a secret key.

### Worked pattern

For 25 employees, there are 25 × 24 / 2 = 300 pairs. Each pair matches with probability 1/365, so a match is more likely than intuition suggests; the source quotes about 57 per cent. For a hash, the same combinatorics gives a collision near 2^(n/2) trials, not 2^n.

## Module 3 — Random numbers, authentication and protocols

### Must know

- Freshness, nonces and timestamps; replay attacks and challenge-response.
- Entity authentication by passwords, dynamic password schemes and zero-knowledge mechanisms.
- The man-in-the-middle attack on unauthenticated Diffie-Hellman and the reflection attack on Protocol 3.
- AKE goals: mutual entity authentication, data-origin authentication, key establishment, confidentiality and freshness.

### Definitions to reproduce

**Entity authentication** verifies who a party is. **Message authentication** verifies the origin and integrity of a message. A **nonce** is a fresh value used once to prevent replay. A **PRNG** is deterministic and reproducible from a seed; a **TRNG** uses a physical source.

### Worked pattern

For the Protocol 3 reflection attack, Bob sends nonce rB and a challenge. The attacker reflects it with Alice's name substituted. Bob replies with a MAC over rB, and the attacker returns that reply as Alice's. Since the reply omits the responder's identity, Bob accepts his own MAC; include identifiers in the authenticated message to fix it.

## Module 4 — Key management

### Must know

- Key length and lifetime; generation by random generation, derivation or components.
- Key establishment by transport, agreement and UKPT.
- Key storage in software and hardware, backup, archival, usage, change and destruction.
- Public-key management, certificate lifecycle and CA domains.
- Reputation-based and closed certificate models.

### Definitions to reproduce

The **key lifecycle** covers generation, establishment, storage, backup, archival, usage, rotation and destruction. **UKPT** means unique key per transaction: terminal and host derive a fresh key from a base key and a counter. A **certificate** binds a public key to an identity and is signed by a CA. **Cross-certification** lets two CA domains trust each other.

### Worked pattern

For UKPT at a POS terminal, draw terminal and host sharing an initial key. Both combine it with the transaction counter through a derivation function to obtain the same per-transaction key.

## Module 5 — Cryptographic applications

### Must know

- SSL/TLS: handshake, record protocol, session keys and certificate checks.
- Wireless LAN security and its early weaknesses.
- Video broadcasting and identity cards.
- A sound algorithm still needs sound deployment: phishing, usage failures and key storage remain weak points.

### Definitions to reproduce

**SSL/TLS** establishes a secure channel using a handshake, authentication and derived symmetric session keys. A **certificate chain** links a server certificate to a trusted root. Across the applications, a sound algorithm still fails if keys are stored or used badly.

### Worked pattern

For an SSL handshake, list client hello, server hello and certificate, key exchange, finished messages, then application data. Certificate checking gives entity authentication, key exchange gives a shared secret, and the record protocol gives confidentiality and integrity.

## Last 24 hours

Revise the Caesar example, birthday bound, HMAC, Protocol 3 reflection, key lifecycle, UKPT and SSL handshake. Learn one table for PRNG versus TRNG.

## Question bank

1. Illustrate the working of a simple substitution cipher by encrypting and decrypting the word CRYPTO. (5 marks)
2. Explain the purpose of HMAC and why a secret key is essential, then illustrate how it is computed. (5 marks)
3. In a company of 25 employees, two share a birthday. Relate this to the birthday problem and interpret its significance for attacks on hash functions. (10 marks)
4. Explain the role of entity authentication before sensitive data is exchanged, and differentiate it from message authentication. (10 marks)
5. Explain how a reflection attack works against Protocol 3, and how the protocol can be repaired. (5 marks)
6. Analyse the key lifecycle from generation to destruction and explain how each stage protects customer transactions. (10 marks)
7. Apply UKPT to repeated card payments at a POS terminal and illustrate key generation and distribution. (10 marks)
8. Analyse how cryptographic parameters secure a live video broadcasting platform. (5 marks)
9. Analyse how cryptography secures a WLAN. (5 marks)

*Source: `BCS701-Scheme_INS_IA-1-Q10-10-2025.pdf`, `IA_2_INS QP-FINAL.pdf` and `IA_2_INS QP-SCHEME.pdf`. The module note PDFs `INS module-1 N19.pdf`, `INS module-2 N19.pdf`, `INS module -2 .pdf`, `INS module-3 N19.pdf`, `INS module-5 .pdf`, `INS Notes IA_2 N19.pdf` and `INS Notes m-5 IA_2 N19.pdf` are scans with no usable text.*
