# Principles for Agentic Security Assurance

!!! abstract "Overview"

    Agentic security engineering makes software assurance harder to ignore.

    The old assurance questions still work. They punish vague requirements, hidden trade-offs, and findings that cannot be reproduced.

    When agents can write code, review code, search code, and exploit code, ask: "What evidence would make us trust the outcome?"

!!! info "Basis for this model"

    This is a practitioner model grounded in [software assurance](software_assurance.md), [Software Engineering Security](swe_redux_security.md), CodeQL-style semantic analysis, [multi-repo variant analysis](https://github.blog/security/vulnerability-research/multi-repository-variant-analysis-a-new-way-to-perform-security-research/), [OWASP GenAI risks](https://genai.owasp.org/), [DARPA AIxCC](aixcc.md), and runtime validation practice. Treat the loop as an assurance pattern, then calibrate thresholds and metrics with local evidence.

## Update the Risk Model

Pre-AI assumptions leak into security programmes.

Public [un]prompted 2026 notes make the pressure concrete:

- [Trail of Bits at 200 bugs/week/engineer](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/kgwvAyF7qsA_Dan_Guido_200_Bugs_Week_Engineer_How_We_Rebuilt_Trail_of_Bits_Around_AI.md): discovery economics are changing.
- [Meta FENRIR at $8.80 per vulnerability](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/c6_bRzHCf3U_Peter_Girnus_Derek_Chen_FENRIR_AI_Hunting_for_AI_Zero-Days_at_Scale.md): triage and verification costs are dropping.
- [Real-world intrusion speed measured in minutes](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/xCtcQkJBReQ_Sergej_Epp_8_Minutes_to_Admin_We_Caught_It_in_the_Wild.md): exploitation can move quickly once the path is found.

Treat those as demonstrated external signals, not local guarantees. The lesson: discovery, triage, and exploitation are getting cheaper.

| Old assumption | Agentic security assumption |
|---|---|
| The vulnerability has a CVE | Dangerous findings can begin as unnamed zero-days |
| The scanner is the control | The pipeline is the control |
| Human review scales with code volume | Verification must be designed as a system |
| Per-repo scanning gives coverage | Cross-repo intelligence is needed for variants and class campaigns |
| Remediation is a ticket | Remediation includes patch, regression, variant search, and prevention |

!!! observation "The moat is the system"

    Models change. The durable investment is the harness: requirements, source intelligence, verifier, twin, judge, campaign tracker, and learning loop.

## Start With V&V

[Software Assurance](software_assurance.md) gives the foundation: verification asks whether we are building it right; validation asks whether we are building the right thing.

| Assurance question | Agentic security translation |
|---|---|
| Are we building it right? | Does the implementation match the security requirement, architecture decision, and expected control behavior? |
| Are we building the right thing? | Does the control reduce real risk in the operational setting, or did we automate the wrong assumption? |

A vulnerability report asks whether a bug exists. A security programme must also validate whether the remediation changes the outcome that matters.

Agents are most useful today as scalable participants in validation and verification. Let them search, challenge, reproduce, compare, and propose. Keep the evidence standard outside the model.

## Requirements Are the Contract

Agents need precise "what" before they can safely produce or judge "how."

Requirements need to be testable. "Protect sensitive data" is too weak. "The assistant must not send content from one origin to another without an explicit user-confirmed action" can be tested, challenged, and encoded as a regression check.

The [Software Artifacts](software_artifacts.md) chapter makes this point for AI-era engineering: artifacts become active contracts. Security requirements, threat models, acceptance criteria, ADRs, and test cases are no longer side documents. They are the steering system.

!!! observation "Bad framing creates bad autonomy"

    The wrong move is to ask an agent to "make this secure."

    The better move is to state the boundary, the attacker, the forbidden outcome, and the evidence needed to accept the result. Agents are much better at executing a security contract than guessing one.

## Evidence Beats Assertion

An agent saying "this is exploitable" is a lead.

Evidence can be source evidence, a reachable source-to-sink path, a reproducible proof of concept, a runtime trace, a failing regression test, or a clearly stated assumption that can be tested later.

| Claim type | Minimum useful evidence |
|---|---|
| Code vulnerability | Entry point, trust boundary, sink, and missing or broken control |
| Design weakness | Requirement or threat model mismatch, plus operational consequence |
| Runtime exposure | Reproducible behavior in a controlled environment |
| Variant | Structural similarity to a confirmed finding, independently verified |
| Remediation | Test showing the old path fails and expected behavior still works |

The standard is enough evidence for a skilled critic to reproduce, dispute, or falsify the claim.

!!! tip "Evidence test"

    If another reviewer cannot rerun the path, inspect the trace, or challenge the assumption, the report is still a hypothesis.

## Separate Discovery From Judgment

Discovery should be broad, creative, and cheap. Judgment should be slower, adversarial, and evidence-based.

Agents satisfy the test they can see. If the same loop generates and grades the finding, the process is easy to fool. Use one process to discover candidates and a separate process to disprove them.

| Stage | Bias we want | Failure mode |
|---|---|---|
| Discovery | Curiosity, breadth, pattern formation | Noise and overclaiming |
| Verification | Skepticism, reproduction, falsification | Missing novel paths |
| Judgment | Deduplication, severity, prioritization | Ranking by drama instead of risk |

## Static and Runtime Evidence Are Complements

Source analysis finds what is visible in code. Runtime testing finds what appears in behavior, state, integration, or deployment.

Static review can show an absent control or dangerous path. Runtime review can show whether a declared control works and whether an attacker can reach the path under realistic preconditions.

## Every Confirmed Finding Is a Seed

A confirmed vulnerability becomes a new search pattern.

Once a finding is real, extract the class:

- What assumption failed?
- Which control was missing?
- Which framework or design pattern made it likely?
- Which sibling components could repeat it?
- Which regression test would stop it coming back?

That is the difference between fixing a bug and eradicating a class.

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

The architecture decision record matters because future agents will copy the implementation. They need the reason and the consequences alongside the code.

## Quality Attributes Are Security Inputs

Reliability, recoverability, observability, isolation, and operability are security properties in agentic systems. A system that cannot explain what an agent did, recover from a bad action, or isolate a tool from sensitive state has an incomplete security design.

| Quality attribute | Agentic security question |
|---|---|
| Reliability | Does the agent fail predictably under hostile input? |
| Recoverability | Can we undo or contain a bad action? |
| Observability | Can we trace input, reasoning context, tool call, and effect? |
| Isolation | Can one compromised context reach another? |
| Operability | Can humans safely supervise and intervene? |

## The Loop Matters More Than the Scan

A scanner without a learning loop becomes another alert queue.

!!! tip "The durable assurance loop"

    ```text
    find -> verify -> judge -> fix -> test -> propagate -> learn
    ```

Each step changes the next run. False positives become suppression rules or better prompts. Confirmed findings become variant seeds. Fixes become regression tests. Repeated classes become policy-as-code or design guidance.

This connects directly to [Policy-as-Code Served Pre and Post Coding](pre_post_policy_as_code.md): static documents become small, testable rules that can guide design, coding, review, and verification.

## References

- [Software Assurance](software_assurance.md)
- [Software Artifacts](software_artifacts.md)
- [Software Engineering Security](swe_redux_security.md)
- [DARPA AI Cyber Challenge Tools Comparison](aixcc.md)
- [Policy-as-Code Served Pre and Post Coding](pre_post_policy_as_code.md)
- [Software Engineering 1.0 Redux](swe_redux.md)
- [Anthropic: Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense)
- [Anthropic Red Team: Claude Mythos Preview zero-day evaluation](https://red.anthropic.com/2026/mythos-preview/)
- [Zero Day Clock](https://zerodayclock.com/)
- [OWASP GenAI Security Project](https://genai.owasp.org/)
- [CodeQL documentation](https://codeql.github.com/docs/)
- [[un]prompted 2026 conference index](https://github.com/CyberSecAI/unprompted_2026)
- [Dan Guido: 200 Bugs/Week/Engineer](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/kgwvAyF7qsA_Dan_Guido_200_Bugs_Week_Engineer_How_We_Rebuilt_Trail_of_Bits_Around_AI.md)
- [Meta FENRIR: AI Hunting for AI Zero-Days at Scale](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/c6_bRzHCf3U_Peter_Girnus_Derek_Chen_FENRIR_AI_Hunting_for_AI_Zero-Days_at_Scale.md)
- [Sergej Epp: 8 Minutes to Admin](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/xCtcQkJBReQ_Sergej_Epp_8_Minutes_to_Admin_We_Caught_It_in_the_Wild.md)

## Takeaways

!!! success "Takeaways"

    - Do not let agentic speed collapse verification and validation into one vague "security review."
    - If the requirement is not testable, an agent cannot reliably verify it.
    - Treat agent output as hypotheses until evidence upgrades it.
    - Let discovery be noisy. Make verification unforgiving.
    - Use static analysis for source understanding and runtime testing for behavior.
    - Never close a confirmed finding until you have asked where else the same class could exist.
    - Capture the "why." Future agents will reproduce the pattern.
    - Treat quality attributes as first-class security requirements.
    - Do not buy or build "an AI scanner." Build a learning assurance loop.
