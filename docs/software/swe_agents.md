# Agent-Based Frameworks for Software Engineering

!!! abstract "Overview"

    This section provides an overview of the context an agent (human or LLM) needs for Software Engineering.


## Software Engineering

<figure markdown>
![](../assets/images/VandV.png)
"Incremental Architecture-centric Validation & Verification Improves Qualification Confidence"
Continuous Verification & Validation of Critical Software via DevSecOps, https://apps.dtic.mil/sti/pdfs/AD1187382.pdf
</figure>

## Software Engineering Artifacts

**Code is informed by upstream activities (requirements, architecture, design, components, etc.) and downstream activities (tests, user feedback).**

  - The code itself is the source of truth for what was implemented, but not why it was implemented that way, nor whether it does the right thing or does it correctly.
      - The source of truth for these aspects is captured in other [Software Engineering Artifacts](https://www.google.com/search?q=software_artifacts/).

!!! Tip


    These Software Engineering Artifacts inform the code and should live with the code. This means they should be in sync with the code and accessible when code is generated. Specifically, they should be located in the same organization/repository as the code, in a format that is both LLM and human-friendly ([Software Engineering Artifact Formats](./software_artifacts.md#artifact-formats-for-ai-integration)).


## Software Engineering Knowledge

### Domain Knowledge

Code is also informed by Domain Knowledge.

!!! Info "Taking Security as an example Domain"

    [https://baxbench.com/](https://baxbench.com/) is a recent (2025) benchmark evaluating LLMs on secure and correct code generation. It demonstrates that even flagship LLMs are not yet ready for coding automation, frequently generating insecure or incorrect code.

    Three levels of Security Reminder are provided to the models:

    **No Security Reminder**: The current highest score is 25% Insecure or Correct code generated.

    - "The models are only prompted to complete the coding task. The prompt contains no security-specific instructions, reflecting a realistic interaction with a developer that does not make explicit security considerations."

    **Generic Security Reminder**: The current highest score is 18.2% Insecure or Correct code generated.

    - The models are prompted to complete the coding task and are explicitly reminded to make security considerations and follow security best practices.

    **Oracle Security Reminder**: The current highest score is 10% Insecure or Correct code generated.

    - The models are prompted to complete the coding task and are explicitly reminded to avoid specific security vulnerabilities that could occur in the given task. This setting assumes an unrealistic oracle that anticipates all security pitfalls, "where the developer anticipates all the security vulnerabilities associated with the scenario and gives specific instructions to avoid them." This prompt provides an upper bound on the models' security performance.

    The models are not provided with any security guidance or additional context (security knowledge for the specific task like threat models, security design patterns, or secure code guidelines).

    - It is very likely that the models would achieve better benchmark results with the right context and guidance. This can be proven by evaluating such a setup against the benchmark.


!!! Tip "Domain knowledge must be available to the Agent"

    Even a simple reminder makes a significant difference, whereas context-specific reminders yield a much greater difference.

    Taking Security as an example Domain:

    - Security guidance or additional context (security knowledge for the specific task, such as threat models, security design patterns, or secure code guidelines) can significantly improve performance.


### Tacit Knowledge

Tacit knowledge is knowledge that resides in personal experience, skills, and intuition rather than being explicitly documented. In other words, it is the "know-how" that comes from doing, rather than just knowing the theory.

!!! Tip "Agents need a mechanism to build tacit knowledge"
    In addition to Software Engineering Artifacts and Domain Knowledge, agents need a mechanism to build tacit knowledge.

In a recent study, Developers report AI not utilizing important tacit knowledge or context as a factor likely to contribute to slowdown.

!!! quote "Implicit repository context (Limits AI performance, Raises developer performance)"

    One developer notes that AI often
    acts like a new contributor to the repository, and that “AI doesn’t pick the right location to make the
    edits.” Another developer notes that while “we [..] know the data that will interact with the code,
    but the model doesn’t know the data. It doesn’t know we need to take care of this weird case of
    backwards compatibility and [thus] keep this specific line. And this is very hard to give as [context
    to the model].”.

    [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/pdf/2507.09089#page=17), "C.1.5 Implicit repository context (Limits AI performance, Raises developer performance)" July 2025





## Takeaways

!!! success "Takeaways"


    The context an agent (human or LLM) needs for Software Engineering includes:

    - Software Engineering Artifacts (including, but not limited to, Code)
    - Software Engineering Knowledge
        - Domain Knowledge
        - Tacit Knowledge

    A Software Engineering setup should have a way to manage this context and provide it to the agent when required.
