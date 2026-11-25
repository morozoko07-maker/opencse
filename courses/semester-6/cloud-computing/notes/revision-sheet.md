---
title: Revision sheet
---

# Revision sheet — Cloud Computing

This sheet follows the five note files in `material/Cloud Computing/ISE notes`. The 2025 IA-1 paper tests the ecosystem and virtualisation; the course-file bank supplies wording for later topics.

## Exam pattern

The README gives CIE 50 + SEE 50. The 2025 IA-1 paper is headed 40 marks across eight questions, with sub-parts carrying 4, 5, 6 or 7 marks. The 2018-19 course file is for 15CS565 and prints IA 20 + exam 80, so ignore its split.

## Module 1 — The cloud ecosystem and enabling technologies

### Must know

- NIST defines cloud computing as on-demand access to a shared pool of configurable resources, provisioned with minimal management effort.
- The five enabling technologies are Web 2.0, service level agreements, virtualisation, distributed systems and utility computing.
- Benefits: no upfront commitment, on-demand access, rapid scalability, efficient allocation, energy efficiency and third-party services.
- The IA-1 answer lists five negative impacts: technological disruption, environmental degradation, social inequality, mental health strain and ethical dilemmas.
- Other challenges: security, compliance, data breaches, legal jurisdiction, interoperability and vendor lock-in.

### Definitions to reproduce

> Cloud computing is a utility-oriented and Internet-centric way of delivering IT services on demand.

> Utility computing is a service-provisioning model in which computing resources are metered and paid for as they are used.

## Module 2 — Virtualisation

### Must know

- A virtualised environment has three parts: guest, host and hypervisor.
- Process-level virtualisation runs on an existing operating system; system-level virtualisation runs on hardware.
- Full virtualisation runs an unmodified guest and emulates the hardware. Paravirtualisation exposes a modified interface; the guest uses hypercalls. Partial virtualisation emulates only part of the hardware.
- Type I hypervisors run natively on hardware; Type II hypervisors depend on a host operating system.
- Xen is an open-source paravirtualisation platform; modified guest kernels run on the Xen hypervisor.
- Hyper-V uses VMBus, virtual service providers and virtual service clients. Enlightened I/O avoids full emulation.

### Definitions to reproduce

> Virtualisation creates a virtual version of a computing resource, separating it from the physical resource.

> A hypervisor, or virtual machine manager, creates and manages the environment in which guest operating systems run.

### Worked pattern

For "full versus para", use a table with rows for guest modification, interface, performance, isolation and example. Then note that Xen keeps a thin hypervisor and moves device work into a privileged domain.

## Module 3 — Architecture, service models and deployment

### Must know

- The reference model stacks physical infrastructure, virtual infrastructure, middleware and applications.
- IaaS supplies virtual machines, storage and networking. PaaS supplies a runtime and development platform. SaaS supplies a finished application. XaaS is the general label.
- Deployment models: public, private, hybrid and community. A community cloud serves organisations with shared requirements.
- Open challenges: interoperability, scalability, security, trust, privacy and organisational issues.
- The IA-1 paper asks for IaaS components in an e-commerce scenario and the VMware vCloud stack: web portal, self-provisioning, vFabric and hosted services such as Zimbra.

### Definitions to reproduce

> IaaS provides virtualised hardware, storage and network resources over a network.

> PaaS provides a development and runtime platform; the provider manages the underlying infrastructure.

## Module 4 — Aneka

### Must know

- Aneka is cloud middleware and a pure PaaS solution built on a service-oriented architecture.
- The container is the unit of deployment and hosts fabric, foundation and application services.
- Fabric services manage infrastructure; foundation services support the platform; application services schedule, execute, monitor and store work.
- Aneka supports dynamic provisioning, multi-tenancy, user management, metering and billing.
- Deployment modes are private, public and hybrid. Hybrid mode adds public resources by dynamic provisioning.
- The SDK and management tools cover infrastructure, platform and application administration.

### Definitions to reproduce

> An Aneka container is a lightweight runtime layer that hosts services and interacts with the rest of the Aneka cloud.

> Dynamic provisioning adds or removes resources while an application is running.

## Module 5 — Cloud applications and data-intensive computing

### Must know

- Cloud application development faces resource imbalance, workload partitioning, performance isolation, security isolation, reliability and network variability.
- Coordination can use workflow patterns or a state-machine model. ZooKeeper provides a replicated namespace, leader election and a single system image through an ensemble.
- MapReduce splits work into map tasks, shuffles intermediate keys and reduces values by key. Data locality keeps computation near storage.
- GrepTheWeb is the Amazon case study: a controller starts Hadoop on EC2, monitors the job and stores results in S3.
- YARN separates resource management from execution; Tez models dataflow; Pig, Hive and Impala give SQL-like access over Hadoop.

### Definitions to reproduce

> Data-intensive computing processes very large data sets where I/O and storage, not arithmetic, dominate the cost.

> MapReduce is a programming model that expresses a computation as map and reduce functions over key-value pairs.

## Last 24 hours

1. Draw the cloud reference model and label IaaS, PaaS and SaaS.
2. Draw the virtualisation reference model and add Type I and Type II hypervisors.
3. Write the six-point significance answer from memory.
4. Trace a word-count MapReduce job from input split to output.

## Question bank

**Module 1**

1. Outline the challenges and negative impacts that are to be resolved in cloud computing. [4]
2. Describe cloud computing and explain the significance and scope that has made it a popular technology. [6]
3. Analyse how the five core technologies interact to enable cloud computing. [4]

**Module 2**

4. Provide an illustrated explanation of virtualisation and outline the primary characteristics of a virtualised environment. [4]
5. Construct and explain the taxonomy of virtualisation, highlighting Type-1 and Type-2 hypervisors. [6]
6. Contrast para-virtualisation with full virtualisation and apply para-virtualisation to Xen technology. [6]

**Module 3**

7. Classify and describe the main features that define Platform-as-a-Service. [4]
8. Explain the basic components of an IaaS solution for an e-commerce company that needs scalable compute, storage and networking. [5]
9. Analyse the VMware Cloud Solution stack with respect to various cloud services. [5]

**Module 4**

10. Describe the main characteristics of Aneka and the use of the Aneka container.

**Module 5**

11. What is data-intensive computing? Describe the characteristics that define the term.
12. What are the requirements of a programming platform that supports data-intensive computations? What is MapReduce?

*Source: `IA-1 Scheme and Solution.pdf` for questions 1–9, with the printed marks; `COURSE_FILE_CLOUD COMPUTING(2018-19).docx.pdf` for questions 10–12. `IA-2 Scheme and Solution.pdf` and `21IS68 AUG 2024.pdf` are scans and were not used.*
