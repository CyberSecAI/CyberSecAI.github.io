# How AI is Changing Software Engineering

!!! abstract "Overview"

    AI accelerates feedback loops: ideas → prototypes → validation happen in minutes, not weeks.

    We look at Software 2.0 where "AI is **eating** software", and Software 1.0 Redux where "AI is **feeding** software."

## Evolution of Software Engineering as Communication over Code

 

Effective software development depends fundamentally on clear communication between all stakeholders—from business experts to developers to end users. The evolution from rigid, document-heavy approaches to collaborative, feedback-driven methodologies illustrates how the industry has learned to prioritize human communication over process documentation.

### The Waterfall Challenge

The [Waterfall model](https://en.wikipedia.org/wiki/Waterfall_model) dominated software development for decades through its linear, sequential approach. However, this methodology created significant communication barriers. Requirements, design documents, and other pre-coding artifacts quickly became outdated as projects progressed. The code itself became the only reliable source of truth, but most stakeholders couldn't understand it.

This disconnect between documentation and reality often led teams to solve the wrong problems. The fundamental issue was the lack of continuous feedback loops between those who understood the business needs and those building the software.

### The Agile Response

During the 1990s, [lightweight development methodologies emerged](https://en.wikipedia.org/wiki/Agile_software_development) in response to these heavyweight, document-centric approaches. [Agile software development](https://en.wikipedia.org/wiki/Agile_software_development) became the most influential of these approaches, emphasizing iterative development, continuous feedback, and direct collaboration between business stakeholders and development teams.

Rather than relying on comprehensive documentation, Agile methodologies prioritize working software and frequent communication. This shift recognized that software development is fundamentally a collaborative, creative process that benefits from ongoing dialogue rather than upfront specification.

### The Language of Collaboration

<figure markdown>
![](../assets/images/doublediamondprocess.png)
</figure>

!!! tip

    See the Design Council’s [Systemic Design Framework](https://medium.com/design-council/developing-our-new-systemic-design-framework-e0f74fe118f7) for an evolution of the Double Diamond that  recognises the importance of the ‘invisible activities’ that sit around the design process: orientation and value setting, continuing the journey, collaboration and connection, and leadership and storytelling.


Software engineering thought leaders have consistently emphasized how critical shared understanding becomes in successful projects. [Alistair Cockburn's research](https://agilemodeling.com/essays/communication.htm) demonstrated that face-to-face communication, particularly when enhanced by shared modeling tools like whiteboards, represents the most effective form of team communication. His work on [communication effectiveness](https://alistaircockburn.com/) showed that physical proximity and multiple communication modalities dramatically improve information transfer and reduce misunderstandings.

Eric Evans, in his foundational work on [Domain-Driven Design](https://www.domainlanguage.com/), introduced the concept of ["ubiquitous language"](https://martinfowler.com/bliki/UbiquitousLanguage.html)—a shared vocabulary that bridges the gap between business experts and technical teams. This common language emerges from ongoing collaboration and becomes embedded in both conversations and code, ensuring that business terminology permeates throughout the software system.

[Dan North](https://dannorth.net/) extended these ideas when developing [Behavior-Driven Development (BDD)](https://dannorth.net/introducing-bdd/), creating frameworks that use natural language constructs to describe software behavior in terms that all stakeholders can understand. BDD treats the specification of desired behavior as a ubiquitous language for the entire project team, helping prevent communication breakdowns between developers and business stakeholders.

These approaches share a common insight: **successful software development requires more than technical expertise—it demands ongoing communication, shared vocabulary, and collaborative understanding of both the problem domain and the solution being built.**


## Software 2.0

The emergence of artificial intelligence is fundamentally changing how we think about software development. 

Andrej Karpathy introduced the concept of "Software 2.0" to describe this transformation, where traditional human-written code gives way to AI-generated solutions.

!!! quote

    Software (1.0) is eating the world, and now AI (Software 2.0) is eating software.

    The “classical stack” of Software 1.0 is what we’re all familiar with — it is written in languages such as Python, C++, etc. It consists of explicit instructions to the computer written by a programmer. By writing each line of code, the programmer identifies a specific point in program space with some desirable behavior.

    In contrast, Software 2.0 is written in much more abstract, human unfriendly language, such as the weights of a neural network. No human is involved in writing this code because there are a lot of weights (typical networks might have millions), and coding directly in weights is kind of hard

    In Software 1.0, human-engineered source code (e.g. some .cpp files) is compiled into a binary that does useful work. 
    
    In Software 2.0 most often the source code comprises 
    
    1. the dataset that defines the desirable behavior and 
    2. the neural net architecture that gives the rough skeleton of the code, but with many details (the weights) to be filled in.

    It is likely that any setting where the program is not obvious but one can repeatedly evaluate the performance of it (e.g. — did you classify some images correctly? do you win games of Go?) will be subject to this transition, because the optimization can find much better code than what a human can write.

    Andrej Karpathy, Nov 11, 2017 https://karpathy.medium.com/software-2-0-a64152b37c35


### Software 2.0 Example: Tesla Autopilot transition from C++ code to AI

Tesla's Autopilot system demonstrates this transition in practice. As Karpathy explained:

!!! quote 


    Neural network can eat through the [programming] stack… When I joined Tesla, there was a ton of C++ code, and now there's much, much less C++ code in the code that runs in the car. 

    Neural network initially was just doing a detection on the image level, then it went for multiple images, it gives you prediction, then multiple images over time give you a prediction, and you're discarding C++ code. And eventually you're just giving steering commands.

    … I do suspect that the end-to-end systems for Tesla in, say, 10 years, it is just a neural net. I mean, the videos stream into a neural net and commands come out.

    https://www.linkedin.com/pulse/andrej-karpathy-8-big-ideas-mikael-alemu-gorsky-eckuf/


This evolution illustrates how AI systems can progressively replace traditional programmatic logic, moving toward end-to-end neural networks that process inputs and generate outputs directly.


### Data as the New Source Code

In this Software 2.0 world, datasets become the primary artifact of development. 

[Hugging Face](https://huggingface.co/) has emerged as "Software 2.0's GitHub," hosting over [400K+ datasets](https://huggingface.co/datasets) alongside 1.7M+ models, where repositories contain datasets and commits represent additions and edits of labels rather than code changes.

This shift fundamentally changes how we think about version control, collaboration, and the artifacts that define our systems. The focus moves from managing code repositories to curating and versioning the data that trains our AI systems. 

As Karpathy noted:

!!! quote 

    Github is a very successful home for Software 1.0 code. Is there space for a Software 2.0 Github? In this case repositories are datasets and commits are made up of additions and edits of the labels.

    https://karpathy.medium.com/software-2-0-a64152b37c35


## Software 1.0 Redux

!!! note

    It's "Software 1.0 Redux" because all the artifacts from "Software 1.0" are still the same, and even more relevant, but the Software factory has transformed with LLMs.

!!! quote 

    “The hottest new programming language is English.”  
    
    —[Andrej Karpathy on X/Twitter, 2023](https://x.com/karpathy/status/1617979122625712128) 

Not all problems are suited to the Software 2.0 paradigm of neural networks replacing traditional code. 

For such problems, Large Language Models (LLMs) are transforming how we write traditional software, creating what we might call "Software 1.0 Redux", where AI feeds and enhances traditional software, rather than eating it ala Software 2.0.

While AI handles low-level implementation details, human developers are elevated to higher levels of abstraction, using natural language to specify intent and behavior. 

The skill shifts from syntax mastery to effective requirements management, architecture, and system design, and clean coding principles. 

### Thoughts on the Future from the Past

I captured some thoughts from the past on how I thought the future of software would play out.
These pre-dated LLMs. LLMs have made these thoughts real.


#### More Continuity between Requirements – Documentation – Test – SW
6 years ago, as part of a presentation on DevSecOps, I concluded with my view of the next 10 years. 

<figure markdown>
![](../assets/images/devsecops_10yrs.png)
</figure>

For "More Continuity between Requirements – Documentation – Test – SW", these points were already playing out at that time:

- Less heavy lifting required by people to build software
- The breadth and depth and rate of change of new technologies means that developers can’t keep pace
- Value moves further up the stack – the lower layers become commodities


The "More Continuity between Requirements – Documentation – Test – SW" is playing out as "Software 1.0 Redux" where
the non-code artifacts (requirements, architecture and design documentation, tests, user documentation) become the contracts from which the code is generated by the LLM - and the code becomes more of a byproduct. And these contracts are maintained and versioned - along with the code.

Natural language prompts have become first-class citizens in development workflows, allowing developers to specify intent at higher levels of abstraction while AI handles implementation details.
Prompt engineering is also an important skill currently, though the need for Prompt engineering is less for more capable models. 

#### Diagrams as Code

5 years ago, as part of a "Thoughts For The Future" chapter for [The Hitchhiker’s Guide to PlantUML!](https://crashedmind.github.io/PlantUMLHitchhikersGuide/) (linked from [plantuml.com](https://www.plantuml.com)) I wrote:



!!! quote

    1.3. Machine Processing Of Text Files

    Having a diagram source as a text file is powerful because it allows for machine processing e.g.

    1. If standard building blocks are used, it allows automated analysis and recognition of the diagram text source, and recommendations to the user e.g. if an arrow text includes “TLS” to indicate the link is secured, then an external program can provide recommendations on TLS protocol version, cipher-suites etc…

    2. As companies move towards standard architecture icon sets (AWS, MS/Azure, Google,…), it is possible to process an existing architecture diagram image with optical recognition (and machine learning) and create the text (plantuml) equivalent.


Today Multi-modal LLMs can process diagram images directly, or diagrams-as-code e.g. generate the code for an architecture diagram, provide security guidance or threat models based on the diagram, etc...


### From Code-Centric to Contract-Centric Development

This transformation reflects a broader trend toward what [a16z calls](https://a16z.com/nine-emerging-developer-patterns-for-the-ai-era/) "upstream artifacts" becoming the primary deliverables:

> In agent-driven workflows, code becomes a byproduct—like a compiled artifact—while high-level inputs become the core deliverable. Code becomes the byproduct of those inputs, more like a compiled artifact than a manually authored source.

#### The New Development Hierarchy

| Aspect               | Traditional (Software 1.0)           | AI-Enhanced (Software 1.0 Redux)            |
|----------------------|---------------------------------------|----------------------------------------------|
| **Primary Artifact** | Code                                  | Requirements, contracts, specifications       |
| **Developer Role**   | Implementation focused                | Architecture and validation focused          |
| **Skill Emphasis**   | Syntax, algorithms, debugging         | Requirements engineering, system design      |
| **Version Control**  | Code changes                          | Contract changes + generated artifacts       |

#### Critical Upstream Artifacts

The most valuable artifacts in AI-driven development become the specifications that guide code generation:

| Artifact Category         | Examples                                             | AI-Centric Value                             |
|---------------------------|------------------------------------------------------|----------------------------------------------|
| **Requirements**          | User stories, acceptance criteria, functional specs  | Clear evaluation targets for AI validation   |
| **Architecture & Design** | ADRs, system diagrams, API contracts                | Unambiguous constraints for code generation  |
| **Data & Schemas**        | JSON schemas, database models, API specifications    | Structured templates for consistent output   |
| **Security & Compliance** | Threat models, security policies, audit requirements | Automated guardrails and validation rules    |

### Everything-as-Code: The Infrastructure Precedent

This shift toward specification-driven development builds on existing "everything-as-code" movements:

- **Infrastructure as Code** (Terraform, CloudFormation)
- **Policy as Code** (Open Policy Agent)
- **Diagrams as Code** (Mermaid, PlantUML)
- **Configuration as Code** (Kubernetes manifests)

These approaches already demonstrated the value of maintaining human-readable specifications that generate operational artifacts. AI extends this pattern to application code itself.

### Blurred Boundaries: Developer Roles Evolve

The lines between traditional software engineering roles are blurring:

**Developer + Requirements Analyst:** Developers must now excel at translating business needs into precise specifications that AI can implement reliably.

**Human + Machine Collaboration:** Success requires understanding both what AI can do well (pattern matching, code generation) and what humans do better (creative problem-solving, architectural judgment).

This evolution suggests developers will spend less time on implementation minutiae and more time on:

- **System design** and architectural decision-making
- **Requirements engineering** and specification writing  
- **Quality validation** of AI-generated outputs
- **Integration orchestration** across AI and human-created components






## Coding for AI Agents


### Evolving “Clean Code” for AI Agents
> “Code for AI agents may prefer _verbose naming_, thorough comments, and highly regular structures—even if that feels like over-documentation to humans.”  
> — Ikangai, 2024[^5]

**New Guidelines**  
- **Naming:** Explicit, unambiguous  
- **Comments:** Machine-readable annotations  
- **Formatting:** Consistent AST-friendly style  


Furthermore, the increasing involvement of AI agents is expanding the "audience" for code. Traditionally, code was written primarily by and for human developers, with a strong emphasis on readability and maintainability for human comprehension. However, code intended to be generated or maintained by AI agents may prioritize different qualities to align with an AI's interpretive capabilities. 1 This can lead to a preference for thorough comments, verbose naming conventions, and highly regular code structures, even if a human developer might consider these practices "over-documentation" or overly explicit. This adjustment in coding best practices is driven by the need to ensure AI agents can correctly parse and manipulate the code. This means that the definition of "clean code" may evolve to balance human readability with optimal AI parseability. Organizations will likely need to establish new guidelines for "AI-optimized code" to ensure that their systems can be effectively maintained and evolved by autonomous agents. This also suggests that documentation will transition from passive information repositories to active instructions that AI agents can directly interpret and act upon. 2
[Coding for AI Agents vs. Humans — Ikangai](https://www.ikangai.com/coding-for-ai-agents-vs-coding-for-human-developers/)  












## Leveraging AI to Improve Software Engineering

Tracy Bannon's excellent talk [Applying AI to the SDLC: New Ideas and Gotchas! - Leveraging AI to Improve Software Engineering](https://www.infoq.com/presentations/ai-sdlc/) includes a model for where AI can be used with DevSecOps.

<figure markdown>
![](../assets/images/ai_devsecops.png)
</figure>

Tracy Bannon’s model outlines opportunities from planning to monitoring: [Applying AI to the SDLC — InfoQ](https://www.infoq.com/presentations/ai-sdlc/) 

| Phase         | AI Use Case                                    |
|---------------|------------------------------------------------|
| Plan & Design | Generate design variants, review ADRs          |
| Code          | Autocomplete, synthesis from prompts          |
| Test & QA     | Auto-generate test cases, fuzzing              |
| Deploy & Ops  | Predictive scaling, anomaly detection          |
| Monitor       | Automated root-cause analysis                  |


## Takeaways
  
!!! success "Takeaways" 

    1. AI is reframing software engineering: _upstream artifacts_ become the true deliverables, and “code” is an executable byproduct. 
    2. Success demands mastery of requirements, architecture, and prompt-engineering as much as traditional coding skills.



### Critical Artifacts for AI-Driven Development

| Artifact Category         | Examples                                             | AI-Centric Need                             |
|---------------------------|------------------------------------------------------|----------------------------------------------|
| **Requirements**          | User stories, functional & non-functional specs      | Clear acceptance criteria for evaluation     |
| **Architecture & Design** | ADRs, UML/component diagrams, API contracts          | Unambiguous intents for prompt templates     |
| **Data & Schemas**        | Training datasets, JSON/YAML schemas                 | Consistent structure for model generation    |
| **Security & Compliance** | Threat models, audit reports                        | Automated guardrails for AI outputs          |









