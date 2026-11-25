---
title: Revision sheet
---
# Revision sheet — Building Enterprise Applications

Building Enterprise Applications (BCS703B) is a CSE course. The folder has no syllabus, only three internal-assessment scheme papers, so this sheet groups the material by four themes.

## Exam pattern

The scheme papers use 5-mark and 10-mark descriptive questions, several of them scenario-based with a marks split.

## Topic 1 — Enterprise architecture and TOGAF

### Must know

- Enterprise architecture describes business processes, applications, data and technology as one coordinated system.
- The TOGAF content framework has four domains: business, applications, data and technology architecture.
- Viewpoints: business, application, data, technology and integration.
- Inception establishes the problem, stakeholders, As-Is and To-Be processes, requirements, feasibility, risks, SRS and business case. Design turns those outputs into components, technologies, patterns and models.
- Non-functional requirements: performance, scalability, availability, security, usability and maintainability.

### Definitions to reproduce

**Enterprise architecture** is a structured description of an organisation's processes, systems, data and technology, used to align IT with business goals. **TOGAF** is an enterprise-architecture framework containing the Architecture Development Method and its content framework. A **viewpoint** is the perspective from which part of the architecture is described for a stakeholder. **Logical architecture** represents business processes as logical building blocks and maps them to applications.

### Worked pattern

For the hospital appointment scenario, draw a layered logical architecture. The presentation layer holds patient and doctor portals. A service-access gateway passes requests to the business layer, which orchestrates validation, availability, appointment update and notification. The data-access layer reads appointment tables, and the integration layer calls the EMR.

## Topic 2 — Business layer, patterns and infrastructure

### Must know

- Technical layers: presentation, business, data access, database, integration, security and infrastructure.
- The business layer holds entities, rules and constraints and coordinates workflows.
- Business Delegate hides service lookup. Session Façade wraps fine-grained services in one coarse-grained workflow.
- Infrastructure blocks: networking and communication, hardware and software, middleware, and management policies.
- Use-case actors may be human or external systems; associations show who interacts with the use case.

### Definitions to reproduce

A **business service** implements one unit of logic, such as validation, debit or credit. A **Session Façade** exposes one workflow interface over several services, often through Enterprise Session Beans. A **Business Delegate** is the presentation-to-business bridge that hides lookup details. **Infrastructure architecture** covers servers, storage, networks, middleware, security and operational policies.

### Worked pattern

For funds transfer, draw presentation → Business Delegate → FundsTransferFacade → validation, debit and credit services. Add business model objects for account and transaction. The façade groups three calls into one, cuts latency and gives atomic transaction behaviour.

## Topic 3 — Code quality, security and testing

### Must know

- Code review checks completeness, correctness, consistency, maintainability, traceability and robustness.
- A defect report names the violation, cites the checklist item, states the effect and gives a corrective action.
- Unit testing verifies one module in isolation and catches logic errors before integration.
- Static analysis inspects code without running it; dynamic analysis profiles a running application.
- Vulnerabilities: SQL injection, cross-site scripting, broken authentication and session management, insecure storage, improper error handling and weak access control.
- Security engineering life cycle: security NFR validation, threat modelling, security design, secure coding review, penetration testing and review of attack vectors.

### Definitions to reproduce

**Code review** is a systematic inspection of source code against a checklist before integration. **Static analysis** examines code structure without execution. **Dynamic analysis** observes a running program through profiling and coverage. **Penetration testing** attempts attacks such as SQL injection, XSS and session hijacking to verify controls.

### Worked pattern

For a defect report, use one row per defect: location, checklist item, evidence, severity and corrective action. A naming violation is fixed by consistent identifiers and indentation; an unused variable is removed or initialised; a hard-coded value becomes a configuration parameter. End with a retest condition.

## Topic 4 — Testing, environments and rollout

### Must know

- Test levels: unit, integration, system, acceptance and production.
- A test strategy covers environment, test types, team, effort, cost, timeline, defect tracking and exit criteria.
- Functional testing checks stated behaviour; non-functional testing checks quality attributes. Black-box tests behaviour, white-box tests internal paths.
- Environments: development, testing or QA, staging and production. Isolation keeps unstable code and real data apart.
- Rollout strategies: brand new, parallel, rolling, phased and up-down-up. Prerequisites include a rollout plan, communication plan, certification, rollback and a deployment window.

### Definitions to reproduce

**Unit testing** tests one module in isolation. **Integration testing** tests interactions between combined modules. **System testing** tests the complete system against requirements. **Acceptance testing** is performed by users before release. **Staging** is a production-like dress rehearsal. **Parallel rollout** runs old and new systems together while traffic is switched gradually.

### Worked pattern

For "levels of testing", draw a ladder and give purpose, owner and exit criterion for each level. Apply it: unit-test modules, integration-test interfaces, system-test end to end, then acceptance and a production pilot.

## Last 24 hours

Memorise the TOGAF four domains, five viewpoints, seven technical layers, testing levels and five rollout strategies. Rehearse the hospital architecture, funds-transfer façade and defect report.

## Question bank

1. Sketch the TOGAF Architecture Content Framework. Apply it to a retail scenario, explaining how data and application architecture address inventory synchronisation. (5 marks)
2. Illustrate the relationship between a Customer and a Loan Product in a banking system, using association and aggregation. (5 marks)
3. A banking app's funds transfer performs poorly because validation, debit and credit are separate UI calls. Sketch a business-layer diagram using the Session Façade to combine them into one workflow. (10 marks)
4. Prepare a code-review defect report for naming, unused-variable and hard-coded-value violations, with corrective actions. (5 marks)
5. A developer skips unit tests, integrates the code and faces repeated integration failures. Explain how proper unit testing would have prevented this. (5 marks)
6. A loan system is slow, but the team cannot tell whether method calls, threads or memory are responsible. Illustrate how dynamic code analysis locates the bottleneck. (5 marks)
7. Analyse the levels of testing in an enterprise application environment, with a diagram, and explain their purpose. (10 marks)
8. A bank is rolling out a loan management system worldwide. Devise a rollout strategy and list the essential prerequisites. (5 marks)
9. Analyse the roles of development, testing, staging and production environments in reducing deployment risk. (10 marks)

*Source: `BEA-Scheme-IA2.pdf` and `BEA Scheme IA3.pdf`. `SCHEME IA1.pdf` is a scan with no usable text, so no question was taken from it.*
