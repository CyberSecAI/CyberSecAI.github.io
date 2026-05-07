# Principles for Agentic Security Assurance

!!! abstract "Overview"

    Agentic security engineering does not replace software assurance. It makes the old rules harder to ignore.

    When agents can write code, review code, search code, and exploit code, the useful question is not "Which model should we use?" The useful question is "Which assurance principles still hold when the work moves faster than human review?"

## Start With V&V

[Software Assurance](software_assurance.md) already gives the foundation: verification asks whether we are building it right; validation asks whether we are building the right thing.

Agentic systems need both.

| Assurance question | Agentic security translation |
|---|---|
| Are we building it right? | Does the implementation match the security requirement, architecture decision, and expected control behavior? |
| Are we building the right thing? | Does the control reduce real risk in the operational setting, or did we automate the wrong assumption? |

A vulnerability report is verification-biased: it asks whether a bug exists. A security programme must also validate whether the remediation changes the outcome that matters.

This is where agents are most useful today: not as unchecked generators, but as scalable participants in validation and verification. Let them search, challenge, reproduce, compare, and propose. Keep the evidence standard outside the model.

## Requirements Are the Contract

Agents need precise "what" before they can safely produce or judge "how."

The requirements do not need to be bureaucratic. They do need to be testable. A requirement like "protect sensitive data" is too weak for an agent. A requirement like "the assistant must not send content from one origin to another without an explicit user-confirmed action" can be tested, challenged, and encoded as a regression check.

The [Software Artifacts](software_artifacts.md) chapter makes this point for AI-era engineering: artifacts become active contracts. Security requirements, threat models, acceptance criteria, ADRs, and test cases are no longer side documents. They are the steering system.

## Evidence Beats Assertion

An agent saying "this is exploitable" is not evidence. It is a lead.

Evidence can be source evidence, a reachable source-to-sink path, a reproducible proof of concept, a runtime trace, a failing regression test, or a clearly stated assumption that can be tested later.

| Claim type | Minimum useful evidence |
|---|---|
| Code vulnerability | Entry point, trust boundary, sink, and missing or broken control |
| Design weakness | Requirement or threat model mismatch, plus operational consequence |
| Runtime exposure | Reproducible behavior in a controlled environment |
| Variant | Structural similarity to a confirmed finding, independently verified |
| Remediation | Test showing the old path fails and expected behavior still works |

The standard is not perfect proof. The standard is enough evidence for a skilled critic to reproduce, dispute, or falsify the claim.

## Separate Discovery From Judgment

Discovery should be broad, creative, and cheap. Judgment should be slower, adversarial, and evidence-based.

This separation matters because agents are good at satisfying the test they can see. If the same agent generates the finding and grades the finding, the system is easy to fool. A better design uses one process to discover candidates and a separate process to disprove them.

| Stage | Bias we want | Failure mode |
|---|---|---|
| Discovery | Curiosity, breadth, pattern formation | Noise and overclaiming |
| Verification | Skepticism, reproduction, falsification | Missing novel paths |
| Judgment | Deduplication, severity, prioritization | Ranking by drama instead of risk |

## Static and Runtime Evidence Are Complements

Source analysis finds what is visible in code. Runtime testing finds what only appears in behavior, state, integration, or deployment.

Neither is enough alone.

Static review can show that a control is absent. Runtime review can show that a declared control is not effective. Static review can find a dangerous code path. Runtime review can show the attacker can actually reach it under realistic preconditions.

## Every Confirmed Finding Is a Seed

A confirmed vulnerability is not just a ticket. It is a new search pattern.

Once a finding is real, extract the class:

- What assumption failed?
- Which control was missing?
- Which framework or design pattern made it likely?
- Which sibling components could repeat it?
- Which regression test would stop it coming back?

This is the difference between fixing a bug and eradicating a class.

## Architecture Is Trade-Offs

Agentic systems turn architecture trade-offs into security decisions.

More autonomy improves user experience and task completion. It also expands blast radius. More context improves reasoning. It also increases leakage and prompt-injection exposure. More tools increase capability. They also increase the number of actions an attacker can redirect.

| Design choice | Security trade-off |
|---|---|
| More context | Better answers, larger data exposure |
| More tools | More capability, larger action surface |
| Fewer confirmations | Lower friction, higher misuse risk |
| Shared memory | Better continuity, persistence risk |
| Fail-open guardrails | Better availability, weaker containment |

The architecture decision record matters because future agents will copy the implementation. They need the reason and the consequences, not only the code.

## Quality Attributes Are Security Inputs

Security is not only the absence of vulnerabilities.

Reliability, recoverability, observability, isolation, and operability are security properties in agentic systems. If the system cannot explain what an agent did, recover from a bad action, or isolate a tool from sensitive state, the security design is incomplete.

| Quality attribute | Agentic security question |
|---|---|
| Reliability | Does the agent fail predictably under hostile input? |
| Recoverability | Can we undo or contain a bad action? |
| Observability | Can we trace input, reasoning context, tool call, and effect? |
| Isolation | Can one compromised context reach another? |
| Operability | Can humans safely supervise and intervene? |

## The Loop Matters More Than the Scan

A scanner without a feedback loop becomes another alert queue.

!!! tip "The durable assurance loop"

    ```text
    find -> verify -> judge -> fix -> test -> propagate -> learn
    ```

Each step changes the next run. False positives become suppression rules or better prompts. Confirmed findings become variant seeds. Fixes become regression tests. Repeated classes become policy-as-code or design guidance.

This connects directly to [Policy-as-Code Served Pre and Post Coding](pre_post_policy_as_code.md): static documents become small, testable rules that can guide design, coding, review, and verification.

## References

- [Software Assurance](software_assurance.md)
- [Software Artifacts](software_artifacts.md)
- [Policy-as-Code Served Pre and Post Coding](pre_post_policy_as_code.md)
- [Software Engineering 1.0 Redux](swe_redux.md)

## Takeaways

!!! success "Takeaways"

    - Do not let agentic speed collapse verification and validation into one vague "security review."
    - If the requirement is not testable, an agent cannot reliably verify it.
    - Treat agent output as hypotheses until evidence upgrades it.
    - Let discovery be noisy. Make verification unforgiving.
    - Do not ask static analysis to prove runtime safety, or runtime testing to replace source understanding.
    - Never close a confirmed finding until you have asked where else the same class could exist.
    - Make the trade-off explicit. "Why" is more important than "how" when agents will reproduce the pattern.
    - Treat quality attributes as first-class security requirements.
    - Do not buy or build "an AI scanner." Build a learning assurance loop.
