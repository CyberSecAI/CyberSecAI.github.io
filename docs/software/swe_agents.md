# Agent-Based Frameworks for Software Engineering

!!! abstract "Overview"

    This section gives an overview of what context an agent (human or LLM) needs for Software Engineering.



## Software Engineering

<figure markdown>
![](../assets/images/VandV.png)
"Incremental Architecture-centric Validation & Verification Improves Qualification Confidence"
Continuous Verification & Validation of Critical Software via DevSecOps, https://apps.dtic.mil/sti/pdfs/AD1187382.pdf
</figure>


## Software Engineering Artifacts

**Code is informed by the upstream (requirements, architecture, design, components,...), and downstream activities (tests, user feedback)** 

- The code itself is the source of truth for what was implemented - but not why it was implemented that way, and not if it does the right thing, or does it right.
    - The source of truth for these is captured as the other [Software Engineering Artifacts](software_artifacts/).


!!! Tip

    These Software Engineering Artifacts inform the code and should live together with the code i.e. be in sync with the code and be accessible at the time of code generate. Specifically, they should live in the same org/repo as the code in a format that is LLM and human friendly [Software Engineering Artifact Formats](./software_artifacts.md#artifact-formats-for-ai-integration).


## Software Engineering Knowledge
 
### Domain Knowledge
Code is also informed by Domain Knowledge.




!!! Info "Taking Security as an example Domain"

    https://baxbench.com/ is a recent (2025) benchmark to evaluate LLMs on secure and correct code generation. It shows that even flagship LLMs are not ready for coding automation, frequently generating insecure or incorrect code.

    3 levels of Security Reminder are provided to the models:

    **No Security Reminder**: 25% Insecure of Correct code generated is the current highest score

    - "The models are only prompted to complete the coding task. The prompt contains no security-specific instructions, reflecting a realistic interaction with a developer that does not make explicit security considerations."

    **Generic Security Reminder**: 18.2% Insecure of Correct code generated is the current highest score

    - The models are prompted to complete the coding task and are explicitly reminded to make security considerations and follow security best-practices.

    **Oracle Security Reminder**: 10% Insecure of Correct code generated is the current highest score

    - The models are prompted to complete the coding task and are explicitly reminded to avoid specific security vulnerabilities that could occur in the given task. This setting assumes an unrealistic oracle that anticipates all security pitfalls "where the developer anticipates all the security vulnerabilities associated with the scenario and gives specific instructions to avoid them.". This prompt provides an upper bound on the models' security performance.

   
    The models are not provided with any security guidance, or additional context (security knowledge for the specific task like threat models, security design patterns, secure code guidelines).
    
    - it is very likely that the models would have better benchmark results with the right context and guidance. This can be proven by evaluating such a setup against the benchmark.

!!! Tip "Domain knowledge must be available to the Agent"
    
    Even a simple reminder makes a significant difference, whereas context-specific reminders achieve a much bigger difference.

    Taking Security as an example Domain
    
    - Security guidance, or additional context (security knowledge for the specific task like threat models, security design patterns, secure code guidelines) can significantly improve performance.






### Tacit Knowledge

Tacit knowledge is the knowledge that resides in personal experience, skills, and intuition rather than being explicitly documented.
In other words, the "know-how" that comes from doing, rather than just knowing the theory. 


!!! Tip "Agents need a mechanism to build tacit knowledge"
    In addition to the Software Engineering Artifacts and Domain Knowledge, Agents Agents need a mechanism to build tacit knowledge.





## Takeaways

!!! success "Takeaways"

    The context an agent (human or LLM) needs for Software Engineering is embodied in

    - Software Engineering Artifacts (including but not limited to Code)
    - Software Engineering Knowledge
        - Domain Knowledge
        - Tacit Knowledge

    A Software Engineering setup should have a way to manage this context and provide it to the agent at the time it is required. 