---
title: Revision sheet
---

# Revision sheet — Computer Networks

The material follows the five BCS502 modules: Forouzan for Modules 1 and 2, and the Kurose–Ross slides for Modules 3 to 5. Revise the layered vocabulary first, then the numerical procedures.

## Exam pattern

The only readable scheme is the IA-1 answer scheme: 40 marks in 1 hour 30 minutes, answer four full questions, each split into a 6-mark part and a 4-mark part. The IA-2 and SEE papers are scans, so their pattern cannot be confirmed from the files.

## Module 1 — Introduction, physical layer and switching

### Must know

- Data communication needs a sender, receiver, message, medium and protocol. Its criteria are delivery, accuracy, timeliness and jitter.
- Network types: LAN, WAN, MAN. Topologies: star, mesh, bus, ring; star and mesh are the usual campus choices.
- OSI has seven layers; TCP/IP has four. Layering gives flexibility, reuse, scalability and easier troubleshooting.
- Impairments: attenuation, distortion and noise. Guided media: twisted pair, coaxial, fibre; unguided: radio, microwave, infrared.
- Line coding: NRZ, NRZ-L, NRZ-I, RZ, Manchester. Manchester is self-clocking.

### Definitions to reproduce

**Protocol** — a set of rules governing data communication between devices.

**Attenuation** — loss of signal energy as it travels through a medium.

### Worked pattern

A 3.4 kHz channel with S/N = 30 dB has S/N = 1000, so C = 3400 log₂(1001) ≈ 33.9 kbps. For 4800 bps, 4800 = 3400 log₂(1 + S/N), so S/N ≈ 1.66.

## Module 2 — Data link layer

### Must know

- Duties: framing, addressing, flow control, error control and media access control.
- Error detection: parity, checksum and CRC. CRC uses modulo-2 division and a generator polynomial.
- Error control: stop-and-wait ARQ, Go-Back-N and selective repeat, driven by sequence numbers and timers.
- Flow control: stop-and-wait and sliding window. Protocols: HDLC and PPP.
- MAC: pure ALOHA, slotted ALOHA, CSMA, CSMA/CD and CSMA/CA. Pure ALOHA has vulnerable time 2Tt and 18.4% efficiency; slotted ALOHA has Tt and 36.8%.
- PPP fields: flag, address, control, protocol, payload and FCS; phases: establishment, authentication, network negotiation and termination.

### Definitions to reproduce

**CRC** — a cyclic redundancy check that appends a remainder so the codeword is divisible by the generator.

**ARQ** — automatic repeat request; the receiver acknowledges frames and the sender retransmits lost or damaged ones.

### Worked pattern

For data 1010, divisor 1011 and three check bits, append 000 to get 1010000. Divide by 1011 using XOR; the remainder is 011, so the codeword is 1010011. A non-zero remainder at the receiver means an error.

## Module 3 — Network layer

### Must know

- Forwarding moves a packet from input to output at one router; routing chooses the path across the network.
- IPv4 header: version, header length, total length, identification, flags, fragment offset, TTL, protocol, checksum and addresses.
- Classful ranges: A 1–126, B 128–191, C 192–223, D 224–239, E 240–255. Classless addressing uses CIDR.
- Subnetting borrows host bits; the mask separates network and host portions.
- IPv6: fixed 40-byte header, 128-bit addresses, no router fragmentation.
- Routing: link-state (Dijkstra), distance-vector (Bellman-Ford); RIP, OSPF, BGP; ICMP reports errors.

### Definitions to reproduce

**Routing** — determining the path taken by packets from source to destination.

**CIDR** — classless inter-domain routing, written as an address with a prefix length.

### Worked pattern

Classify by the first octet: 201.20.31.65 is C; 126.11.11.239 is A; 193.14.56.22 is C; 130.34.54.12 is B. For a CIDR block, host bits equal 32 minus the prefix length.

## Module 4 — Transport layer

### Must know

- The transport layer gives logical communication between processes using ports and multiplexing.
- UDP is connectionless and unreliable, with an 8-byte header: source port, destination port, length and checksum.
- TCP is connection-oriented and reliable: sequence numbers, acknowledgements, three-way handshake and four-way close.
- Flow control protects the receiver; congestion control protects the network.
- TCP congestion control: slow start, congestion avoidance (AIMD), fast retransmit and fast recovery.
- Go-Back-N retransmits the whole window; selective repeat retransmits only the missing frame.

### Definitions to reproduce

**Multiplexing** — gathering data from several processes and passing it down with port numbers.

**Flow control** — matching the sender's rate to the receiver's capacity.

### Worked pattern

On a Go-Back-N timeline, mark frames, cumulative ACKs and the timeout. If frame 3 is lost, the receiver discards 4 and 5 and sends ACK 2; the sender retransmits 3, 4 and 5. Selective repeat resends only 3.

## Module 5 — Application layer

### Must know

- Architectures: client–server and peer-to-peer. A socket is the interface between an application and the transport layer.
- HTTP: request/response, methods, status codes and cookies. Non-persistent HTTP opens a connection per object; persistent HTTP reuses one.
- DNS is a hierarchical, distributed database; resolution is iterative or recursive; records include A, AAAA, CNAME, MX and NS.
- Email: SMTP sends; POP3 or IMAP retrieves. FTP uses separate control and data connections.

### Definitions to reproduce

**Socket** — the IP address and port number that identify an application endpoint.

**DNS** — the domain name system, which maps names to IP addresses.

## Last 24 hours

- Draw the OSI and TCP/IP stacks with one protocol per layer.
- Redo the Shannon, CRC and addressing calculations.
- Put ALOHA, stop-and-wait, Go-Back-N and selective repeat in one comparison table.
- Trace one TCP handshake and one DNS lookup.

## Question bank

Each full question below carries 10 marks, split 6 + 4 in the scheme.

**Module 1**

1. Identify the importance of data communication and the characteristics affecting performance; explain how protocol layering helps a chat application. (10 marks)
2. Apply NRZ, NRZ-L, NRZ-I, RZ and Manchester to 1011001011; explain attenuation, noise and delay distortion. (10 marks)
3. Add three CRC bits to 1010 with divisor 1011 and check at the receiver; solve for data elements and signal elements when bit rate is 8000 bps and baud rate is 1000 baud. (10 marks)
4. Analyse Go-Back-N when all frames arrive, when frames are lost and when an ACK is lost; solve channel capacity for 3.4 kHz at 30 dB and the S/N for 4800 bps. (10 marks)

**Module 2**

5. Explain quantization in PCM; choose a campus topology and its limitations. (10 marks)
6. Compare the seven OSI layers for slow transfers and failed email; compare pure and slotted ALOHA. (10 marks)

*Source: `material/CN/IA-1 answer scheme.pdf` (Computer Networks BCS502, IA-I, 25/11/2024). The IA-2 question notes, handwritten notes and SEE papers are scans or OCR noise and were not used.*
