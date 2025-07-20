---
icon: material/play-box-edit-outline 
---

# Software Engineering Reimagined


!!! overview

    In the early stages of GenAI implementation, organizations tend to "shoehorn" GenAI's advanced capabilities into existing workflows and processes. 
    
    - They essentially use powerful new tools to perform the same tasks slightly more efficiently, without fundamentally reimagining what's possible.

    However, the true transformative potential of generative AI emerges when we recognize that it won't simply augment our current operational models—it will radically reshape them. 

    - The "way of doing things" inevitably undergoes profound change as the technology matures and its implications become more apparent.

    For effective GenAI strategy, organizations must simultaneously:

    - Address immediate needs by applying AI to current processes
    - Anticipate and design for entirely new operational paradigms that will emerge
    
    This dual focus ensures solutions remain relevant not just for today's challenges, but for the transformed landscape that GenAI will ultimately create.

    This section is hands on walk through of Software Engineering for a Greenfield application using GenAI.

## BMad Workflows

Having reviewed and played with some of the [SWE agents](swe_agents_report.md), the BMAD-Method was closest to my views on Software 1.0 Redux, so this is used here.

There's 2 [BMad Workflows](https://github.com/bmadcode/BMAD-METHOD/blob/main/docs/core-architecture.md#51-the-planning-workflow).

### [The Planning Workflow](https://github.com/bmadcode/BMAD-METHOD/blob/main/docs/core-architecture.md#51-the-planning-workflow) 
   
!!! quote "Key Planning Phases"

    - Optional Analysis: Analyst conducts market research and competitive analysis
    - Project Brief: Foundation document created by Analyst or user
    - PRD Creation: PM transforms brief into comprehensive product requirements
    - Architecture Design: Architect creates technical foundation based on PRD
    - Validation & Alignment: PO ensures all documents are consistent and complete
    - Refinement: Updates to epics, stories, and documents as needed
    - Environment Transition: Critical switch from web UI to IDE for development workflow
    - Document Preparation: PO shards large documents for development consumption

!!! note

    The created documents do include checks on these items, but a more detailed focused analysis can also be with these documents done before "The Core Development Cycle".

    - Security & Compliance 
    - Accessibility Implementation



    

### [The Core Development Cycle](https://github.com/bmadcode/BMAD-METHOD/blob/main/docs/core-architecture.md#52-the-core-development-cycle)

!!! quote "Key Planning Phases"

    When to move to the IDE: Once you have your PRD, Architecture, optional UX and Briefs - its time to switch over to the IDE to shard your docs, and start implementing the actual code! 

BMAD method breaks down the requirements and other upstream artifacts into epics and stories, enabling Claude Code to generate structured code and docs with little human intervention ([Level 4 Autonomy](./code/code_assistant_agents.md#autonomy-levels-for-ai-coding-tools)).


### Other Claude Code Workflows

There are other Claude Code workflows, some example are given here.

##### UI Designer 
https://www.youtube.com/watch?v=TyGx277x9hQ

##### Restrospectives 

https://www.youtube.com/watch?v=ai_sSQH1Pn4&t=478s




##### Multitasking

https://www.geeky-gadgets.com/how-to-use-git-worktrees-with-claude-code-for-seamless-multitasking/

There are UI tools built on GIT worktrees to support this.

### Other non-Claude Code Workflows

#### Security

!!! quote

    Effective threat modeling examines data flows, trust boundaries, and potential attack vectors to create a comprehensive security strategy tailored to the specific system.

    In a shift-left approach to security, threat modeling serves as a critical early intervention. By implementing **threat modeling during the design phase—before a single line of code is written**—organizations can identify and address potential vulnerabilities at their inception point. 

    AWS [Accelerate threat modeling with generative AI](https://aws.amazon.com/blogs/machine-learning/accelerate-threat-modeling-with-generative-ai/), JUN 2025 


##### Open Source Tools




Per [ref](https://xvnpw.github.io/posts/scaling-threat-modeling-with-ai/), the main artifacts associated with security analysis are:
🔒 Security Design Documentation: Generating detailed security design review.
🎯 Threat Modeling: Performing threat modeling analysis.
🔍 Attack Surface Analysis: Identifying potential entry points and vulnerabilities in the project’s attack surface.
🌳 Attack Tree Analysis: Visualizing potential attack vectors and their hierarchies through attack tree.

7. https://github.com/scragz/kornelius/tree/main 
9. https://github.com/awslabs/threat-composer#readme
10. https://aws.amazon.com/blogs/machine-learning/accelerate-threat-modeling-with-generative-ai/
https://github.com/awslabs/threat-designer/tree/main?tab=readme-ov-file#prerequisites

##### Security Analysis
https://github.com/xvnpw/ai-security-analyzer/blob/dabfc57b6e5da9d99b3df5229fd496a224dac862/ai_security_analyzer/prompts.py

##### Threat model Prompts
https://github.com/danielmiessler/Fabric/blob/main/data/patterns/create_stride_threat_model/system.md 
https://github.com/danielmiessler/Fabric/blob/main/data/patterns/create_threat_scenarios/system.md
https://github.com/scragz/kornelius/blob/main/prompts/audit/security.prompt

#### Accessibility
https://github.com/scragz/kornelius/blob/main/prompts/audit/a11y.prompt



## Existing Exploratory Documentation

In the exploratory part of the project at the start I had some [existing documentation](https://github.com/CWE-ChatBot/CWE-ChatBot/blob/main/README.md#additional-documentation):

1. A Cost Analysis was created by using 
      1. ChatGPT and Gemini **Reasoning** models to create an analysis
      2. Getting them to cross-review each other's output and amending their own output as a result
      3. Then taking the amended ChatGPT version as it was more succinct which is what I was looking for.
      4. The cost analysis was a back-of-napkin effort to understand likely operational costs early to see if these were a show-stopper or not.
2. Research Documents using ChatGPT and Gemini **Research** models and Anthropic
3. ADRs using an existing competed example I liked, and redoing it for the architecture decisions I had made using ChatGPT and Gemini **Reasoning** models and Anthropic.
4. Some Functional Requirements and use cases and user stories (in a Doc format) from MITRE CWE team.

!!! tip

    I worked the existing document content into the [The Planning Workflow](https://github.com/bmadcode/BMAD-METHOD/blob/main/docs/core-architecture.md#51-the-planning-workflow) by providing the content to the BMAD Persona at the relevant time via the prompt.


## [The Planning Workflow](https://github.com/bmadcode/BMAD-METHOD/blob/main/docs/core-architecture.md#51-the-planning-workflow) 

Here we build the [Upstream Software Engineering Artifacts](./software_artifacts.md).

Specifically these are the [artifacts](https://github.com/CWE-ChatBot/CWE-ChatBot/blob/main/README.md#project-documentation) that are built with the workflow below.


### Setup

The [BMAD-METHOD](./swe_agents_report.md) is used.

Specifically, the [Fastest Start: Web UI Full Stack Team at your disposal](https://github.com/bmadcode/BMAD-METHOD?tab=readme-ov-file#fastest-start-web-ui-full-stack-team-at-your-disposal-2-minutes) part where you create a Gemini GEM with a [BMAD-provided text file](https://github.com/bmadcode/BMAD-METHOD/blob/main/dist/teams/team-fullstack.txt).

- All these documents are created via a browser interface (Gemini GEM) so the process is IDE-independent!
- Gemini's long-context window allows it to keep the various documents produced in context so it can make consistent changes across them all.

!!! Success

    I was impressed how well this setup worked! 

    - following a logical workflow and prompting for choices or input at each stage (and not getting lost)
    - allowing me to request Gemini Gem to output a document at any time (so I could review and version control it before changes)
    - allowing me to refine the content or ask questions across all the documents as required e.g. if I suggested a change that impacted multiple documents then this was detected by Gemini and the updates made. This ensured consistency across the artefacts.
  

### Example Interactions with BMAD Gemini Gem



<figure markdown>
![](../assets/images/bmad1.png)
</figure>
<figure markdown>
![](../assets/images/bmad2.png)
</figure>

<figure markdown>
![](../assets/images/bmad4.png)
</figure>
<figure markdown>
![](../assets/images/bmad5.png)
</figure>
<figure markdown>
![](../assets/images/bmad6.png)
</figure>
<figure markdown>
![](../assets/images/bmad9.png)
</figure>
<figure markdown>
![](../assets/images/bmad10.png)
</figure>
<figure markdown>
![](../assets/images/bmad11.png)
</figure>

Some choices / decisions were delibertate postponed e.g. data exchange formats and schemas per [Principle #3 - Assume variability; preserve options](https://framework.scaledagile.com/assume-variability-preserve-options/). This results in a PARTIAL Status at this point.


<figure markdown>
![](../assets/images/bmad12.png)
</figure>
<figure markdown>
![](../assets/images/bmad13.png)
</figure>
<figure markdown>
![](../assets/images/bmad_choose.png)
Prompt to choose how to proceed. Or interact in general via the Prompt.
</figure>


## Security Documents
https://github.com/xvnpw/ai-security-analyzer/blob/dabfc57b6e5da9d99b3df5229fd496a224dac862/ai_security_analyzer/prompts.py
https://github.com/danielmiessler/Fabric/blob/main/data/patterns/create_stride_threat_model/system.md 

https://github.com/danielmiessler/Fabric/blob/main/data/patterns/create_threat_scenarios/system.md
## References

1. https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/
2. https://www.geeky-gadgets.com/how-to-use-git-worktrees-with-claude-code-for-seamless-multitasking/
3. https://github.com/ryoppippi/ccusage
4. Claude Taskmaster
5. https://www.reddit.com/r/vibecoding/comments/1lu37up/vibecoding_is_straight_chaos_without_instructions/ 
6. https://www.reddit.com/r/vibecoding/comments/1l5o93n/lets_talk_about_security/
7. https://github.com/scragz/kornelius/tree/main 
8. https://xvnpw.github.io/posts/scaling-threat-modeling-with-ai/
9. https://github.com/awslabs/threat-composer#readme
10. https://aws.amazon.com/blogs/machine-learning/accelerate-threat-modeling-with-generative-ai/
https://github.com/awslabs/threat-designer/tree/main?tab=readme-ov-file#prerequisites