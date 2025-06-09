# Software Assurance

!!! abstract "Overview"

    This section provides a brief overview of Software Assurance fundamentals that are independent of the Software Development Life Cycle (SDLC) [Methodology](https://en.wikipedia.org/wiki/Software_development_process#Methodologies) or what entity is creating the software:
   
       1. Software Assurance
       2. Verification and Validation
       3. Architecture
          1. Laws of Software Architecture
          2. Quality Attributes Drive the Architecture Design

    It also covers the what, how, and why for the how, of Software Engineering.


!!! quote
    
    "Don't worry about that specification paperwork. We'd better hurry up and start coding, because we're going to have a whole lot of debugging to do."

    Verifying And Validating Software Requirements And Design Specifications, Barry Boehm, 1984


## Software Assurance

!!! quote "Software assurance aims to ensure the reliability, safety, and security of software products."

    Software assurance (SwA) is a critical process in software development that ensures the reliability, safety, and security of software products.

    There are several types of software assurance initiatives, including:

    - **Certification and accreditation**: These programs establish standards and guidelines for software development, and verify that software products meet these standards. Certification and accreditation can help to ensure that software products are reliable, secure, and compliant with regulations and industry standards.[6]
    - **Training and education**: These initiatives provide software developers with the knowledge and skills they need to create high-quality, secure software. Training and education can include courses on software testing, secure coding practices, and industry standards and best practices.[7]
    - **Code analysis and testing**: These initiatives use tools and techniques to analyze software code and identify defects or vulnerabilities. Code analysis and testing can include static analysis, dynamic analysis, and fuzz testing, among other techniques.[8]
    - **Threat modeling and risk assessment**: These initiatives assess the potential risks and threats to a software system, and identify strategies for mitigating these risks. Threat modeling and risk assessment can help to ensure that software systems are designed to be resilient to attacks and other threats.[21]

    Software assurance is executed through a series of activities that aim to ensure the reliability, safety, and security of software products. These activities include requirements analysis, design reviews, code inspections, testing, and formal verification.

    https://en.wikipedia.org/wiki/Software_assurance


## Validation vs. Verification

!!! quote "verification and validation to resolve issues early in the software life cycle"

    **The basic objectives in verification and validation (V&V) of software requirements and design specifications are to identify and resolve software problems and high-risk issues early in the software life cycle.**

    **Verification** - to establish the truth of the correspondence between a software product and its specification. 
    
    - "Are you building it right?" 

    **Validation** - to establish the fitness or worth of a software product for its operational mission.

    - "Are you building the right thing?"
    
    **Verification** activities begin in the Product Design phase and conclude with the acceptance test. They do not lead to changes in the requirements baseline; only to changes in the refinements descending from it.

    On the other hand, **validation** identifies problems which must be resolved by a change of the requirements specification. Thus, there are validation activities which occur throughout the software life cycle, including the development phase. 

        - For example, a simulation of the product design may establish not only that the design cannot meet the baseline performance requirements (verification), but also that the performance requirements are too stringent for any cost-effective product designs, and therefore need to be changed (validation).

    Basic V&V criteria for software requirements and design specifications: 
    
    - completeness
    - consistency
    - feasibility
    - testability

    Guidelines For Verifying And Validating Software Requirements And Design Specifications, Barry W. Boehm


### Continuous Validation And Verification Process

<figure markdown>
![](../assets/images/fig1big.webp.png)
A continuous validation and verification process. Validation ensures the requirements correctly capture the users' and stakeholders' expectations and should be performed whenever a translation of requirements from one domain to another occurs. https://www.infoq.com/articles/ieee-verification-and-validation-for-software-systems/
</figure>

The **key artifact that distinguishes verification activities from validation activities is the software requirements** specification.

- This covers **what** the software product will do (but not **how** it will do it; this is to be done in the design specification).

<figure markdown>
![](../assets/images/VandV.png)
"Incremental Architecture-centric Validation & Verification Improves Qualification Confidence"
Continuous Verification & Validation of Critical Software via DevSecOps, https://apps.dtic.mil/sti/pdfs/AD1187382.pdf
</figure>

!!! note

    These assurance steps apply independent of the Software Development Life Cycle (SDLC) [Methodology](https://en.wikipedia.org/wiki/Software_development_process#Methodologies). 


## Architecture

### Laws of Software Architecture

[Fundamentals of Software Architecture](https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/), Mark Richards & Neal Ford, defines some fundamental Laws of Software Architecture.

#### First Law of Software Architecture

**"Everything in software architecture is a trade-off."**

- Corollary 1: If an architect thinks they have discovered something that isn't a trade-off, more likely they just haven't identified the trade-off yet.


#### Second Law of Software Architecture

**"Why is more important than how."**


### Quality Attributes Drive The Architecture Design

!!! quote "Quality Attributes drive the architecture design"

    Requirements for a software system fall into the following two categories: 

    1. Functional requirements: These requirements describe the business capabilities that the system must provide, as well as its behavior at run-time. 

    2. Non-functional requirements: These requirements describe the "[Quality Attributes](https://en.wikipedia.org/wiki/ISO/IEC_9126)" that the system must meet in delivering functional requirements.

    **Quality Attributes drive the architecture design.**

    [Continuous Architecture: Sustainable Architecture in an Agile and Cloud-Centric World](https://www.oreilly.com/library/view/continuous-architecture/9780128032855/)


### Architecture Decision Records (ADR)

!!! quote "ADRs as a Decision Log"

    An ADR can help you understand the reasons for a chosen architectural decision, along with its trade-offs and consequences. The collection of ADRs created and maintained in a project constitute its decision log.
    https://adr.github.io/

ADRs are common e.g.

- [Azure Well-Architected Framework ADRs](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)
- [Amazon AWS ADR Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)
- [Google GCP Architecture](https://cloud.google.com/architecture/architecture-decision-records)

!!! quote "ADRs as Documentation"

    Architecture Decision Records can be used as an effective means to document a software architecture. 
    
    - The Context section of an ADR provides an excellent opportunity to describe the specific area of the system that requires an architecture decision to be made. This section also provides an opportunity to describe the alternatives. 
    - Perhaps more important is that the Decision section describes the reasons why a particular decision is made, which is by far the best form of architecture documentation. 
    - The Consequences section adds the final piece to the architecture documentation by describing additional aspects of a particular decision, such as the trade-off analysis of choosing performance over scalability.

    Chapter 19: Architecture Decisions, [Fundamentals of Software Architecture](https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/), Mark Richards & Neal Ford


## The What How Why Of Software Engineering

!!! observation "People often struggle with what vs how"

    As a software architect for most of my career, I've seen people (customers and technical people) struggle with the **what vs how**. 
    
    They will often specify the implementation details (the **how**), but not **what** they want and why.
    
    - Or they will specify what they know exists - not what they actually want.

    I've seen this also in a security context e.g. 

    - how: "I want to share a secret key with a trusted 3rd party"
        - The wrong thing to do is start by describing secure ways to share keys (which some technical people will do regardless of their seniority)
        - The right thing to do is ask "why, what are you trying to do? Can you give an example?", but often people don't ask.
    - what: "I want to give read access to a trusted 3rd party to data on *somewhere* so they can do *something*"
        - This may not require sharing keys depending on the context. But even if it does require sharing keys, you can give advice appropriate to the use case and context.

    !!! quote "Framing the "what""
    
        Think of me as a good plumber:

        1. Ask for what you want, not what you think you can get. In other words, assume you can have anything you want, now what do you want?
        2. You tell me what features you want. I'll take care of the plumbing details.


### What How Why

- The **what** is captured in the **Software Requirements**.
- The **how** is captured in the **System Design**.
- The **why** for the **how** is captured in Decision Records covering the reasons and tradeoffs associated with the decisions. These decisions can be at an Architecture or Design level.


## Takeaways

!!! success "Takeaways"

    The key artifact that distinguishes verification activities from validation activities is the software requirements.

    It is important to understand the **what** independent of the **how** (requirements vs design).

    It is important to understand the **why** for the **how** (e.g. ADRs) aka 
    
    "Why is more important than how."

    Everything in software architecture is a trade-off.

    Quality Attributes drive the architecture design.