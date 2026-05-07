# Twin Environments and Continuous Runtime Testing

!!! abstract "Overview"

    A twin environment is an adversarial proof instrument.

    Staging reduces release risk. A twin lets agents explore, inject, probe, trace, and prove behavior safely.

    The strategic question is no longer only "Can we find it?" It is "Can we prove it, fix it, verify the fix, and turn the lesson into a standing control?"

    Runtime completes the assurance argument in [Software Assurance](software_assurance.md). A finding may be true in code and still unimportant in operation; a control may exist in code and still fail in operation.

## A Twin Is Not CI/CD

CI answers whether codified checks pass. A twin answers whether a system behaves correctly under realistic interaction. Those are different assurance problems.

| Environment | Primary purpose | Security testing limit |
|---|---|---|
| Local dev | Fast developer feedback | Simplified dependencies and state |
| CI | Deterministic checks | Mostly static or scripted |
| Staging | Release confidence | Usually not safe for unbounded adversarial exploration |
| Production | Real behavior | Too risky for exploit development |
| Twin | Safe adversarial realism | Requires deliberate fidelity investment |

!!! info "Practical distinction"

    CI/CD asks whether known tests pass. A twin lets an agent ask new questions, take actions, observe results, and adapt the next step.

!!! observation "Where staging falls short"

    Staging can tell you whether the happy path still works. It rarely lets an agent safely place hostile content in the workflow, force strange state transitions, probe the policy boundary, and keep the trace needed to prove what happened.

## What a Twin Is

A twin is an isolated, production-representative simulator built for exploration.

Copy only the production details needed to exercise the claim: identity, authorization, tool calls, data boundaries, network egress, logging, user interaction, persistence, and failure modes. Some dependencies can be real; others can be simulated, mocked with richer behavior, or generated agentically.

!!! info "Fidelity contract"

    | Fidelity dimension | Must preserve |
    |---|---|
    | Identity | The same authentication and authorization decision shape |
    | State | The state transitions relevant to the claim |
    | Tool and action surface | The risky actions, permissions, and confirmation gates |
    | Data boundary | The origin, tenant, workspace, or sensitivity boundary under test |
    | Observability | Enough trace data to prove or disprove the path |
    | Replay | The same exploit and fix scenario can be rerun |

| Twin capability | Use |
|---|---|
| Injection | Place adversarial content, state, requests, files, or tool results at controlled points |
| Probing | Ask whether a boundary, sanitizer, confirmation, or policy actually activates |
| Tracing | Reconstruct the path through prompts, tools, services, logs, and data stores |
| Replay | Re-run the old failure after a patch |
| Isolation | Test dangerous behavior without production blast radius |

## Fidelity Should Follow Risk

Start with one high-risk workflow. Define the security properties. Simulate only the dependencies needed to test those properties. Increase fidelity where a disputed assumption requires it.

A practical sequence:

1. Pick one high-risk workflow.
2. Define the security properties to test.
3. Build minimal behavioral clones for required dependencies.
4. Add injection points, probes, and trace capture.
5. Run adversarial test cases.
6. Convert confirmed failures into regression tests.
7. Expand to the next workflow.

!!! tip "Fidelity rule"

    Build the smallest twin that can answer the security question. Add realism when low fidelity hides or distorts the behavior under test.

## Why Runtime Testing Matters

Source code shows intent. Runtime shows behavior after deployment, identity resolution, cloud state changes, and tool sequencing.

Runtime testing catches failures that are invisible or ambiguous in code:

- guardrails configured differently than expected
- authorization that depends on live identity state
- logging declared but not flowing
- network egress that exists despite policy
- cross-service behavior missing from unit tests
- prompt injection that only works through real tool sequencing
- data exposure caused by integration, not a single line of code
- remediations that close the exploit but break intended behavior

Use source analysis for hypotheses. Use runtime testing for behavior.

!!! observation "Runtime-only classes"

    Logging that is declared but not flowing, stale resources, cloud-state drift, organization membership, short-lived identity state, and post-deploy configuration mutations are not source-code facts. They are runtime facts.

## Understand the Data First

Before building a twin or CART programme, look at the findings data you already have:

| Data question | Why it matters |
|---|---|
| Where do findings concentrate? | Pareto effects decide where to build fidelity first |
| Which classes are false positives? | Bad signal destroys trust before the programme matures |
| How long does remediation actually take? | Mean time hides survival curves and stuck queues |
| Which alerts never become owned work? | Detection without action is backlog theatre |
| Which controls disagree about reality? | A scanner and an enforcement log can both be "working" and still contradict each other |

!!! tip "EDA before CART"

    Use exploratory data analysis to decide where runtime verification will produce signal and where it will produce noise.

## Continuous Exploration

A twin is a standing exploration environment for features, bugs, and vulnerabilities. Agents can explore a workflow, find a strange behavior, adapt their plan, and choose the next test.

The scarce resource becomes decision-quality proof.

!!! info "Exploration loop"

    ```text
    observe -> hypothesize -> inject -> trace -> judge -> replay -> learn
    ```

## Discovery Forces Proof Infrastructure

Hundreds of plausible findings make manual triage the bottleneck. Hundreds of plausible critical findings make manual triage a programme risk. Proof infrastructure turns candidates into evidence, rejects weak reports, and replays fixes without exhausting the software owners.

That is the twin's strategic role.

!!! observation "The forcing function"

    Mass discovery is only useful when proof keeps up. Otherwise the result is a larger queue with better prose.

## Continuous Automated Red Teaming

Continuous automated red teaming keeps pressure on known classes between human-led assessments. It turns expert red-team methods into recurring checks for critical workflows.

The timing pressure comes from public evidence. The Zero Day Clock tracks exploit windows collapsing, and the [un]prompted "8 Minutes to Admin" case shows how fast an AI-assisted intrusion can move once the path is found. Periodic testing still has value, but it cannot be the only pressure on critical paths.

Two modes are useful:

| Mode | Viewpoint | Finds |
|---|---|---|
| External runtime testing | What an unauthenticated or low-privilege attacker sees | exposed services, auth gaps, unsafe defaults |
| Twin runtime testing | What a controlled adversary can do inside a representative system | tool misuse, lateral movement, data flow, configuration drift |

Continuous testing turns red-team knowledge into an operational control.

!!! info "CART modes"

    - **External mode:** no credentials, no source access, same view as an attacker.
    - **Twin mode:** authenticated or post-compromise context inside an isolated representative system.

    The first tests the perimeter. The second tests what source review and perimeter testing cannot see.

## Agentic Systems Need Interaction

Agentic vulnerabilities often require a sequence.

The unsafe behavior may require a model to read untrusted content, choose a tool, call the tool, observe the result, and choose another action. Static review can identify the possibility. A twin proves the chain.

Rehberger's promptware examples, BrowseSafe's production prompt-injection work, and capability-bounded agent designs all point at the same runtime requirement: test the full sequence.

Sequence-dependent classes include:

- prompt injection
- unsafe tool chaining
- hidden or indirect instructions
- cross-context data exposure
- persistent memory poisoning
- confirmation bypass
- action/state desynchronization

Verify sequence-dependent vulnerabilities in an environment that can run the sequence.

## Time to Insight Actioned

Measure time to insight actioned: how long it takes to move from candidate vulnerability to proven risk, accepted fix, verified non-regression, and reusable learning.

For a vulnerability, the value stream is:

```text
find -> triage -> prove -> patch -> verify -> prevent -> detect
```

| Step | Evidence expected |
|---|---|
| Find | Candidate path, source evidence, or runtime symptom |
| Triage | Deduplication, preconditions, severity, and proximity |
| Prove | PoC, replay, trace, or mechanically demonstrated exploit path |
| Patch | Remediation tied to the failed assumption |
| Verify | Old path closed and intended behavior still works |
| Prevent | Regression test, policy rule, safer abstraction, or design guidance |
| Detect | Variant search, monitoring, or future discovery rule |

Discovery without this loop creates backlog.

## System Owners Own the Remediation

Security can find, verify, and explain. System owners change the code, configuration, workflow, or architecture.

A twin should produce evidence a system owner can act on: replay, trace, preconditions, expected behavior, remediation shape, and regression test. A verified finding should arrive as engineering work.

When discovery scales, ownership and remediation discipline become the constraint.

Target self-service. Security supplies proof, replay, proximity, and class guidance. System owners apply the fix, make the design trade-off, replay the scenario, and keep the regression.

Handoff: proven failure, replay, failed assumption, closure criteria. Let the owning team choose the implementation unless the control must be centralized.

## Feed Runtime Findings Back Into Source Intelligence

When a twin exposes a failure, extract the class. Search for source patterns, configuration templates, policy gaps, and design assumptions that could repeat it. Add tests, rule cards, or review guidance so future source analysis can catch the same class earlier.

```text
runtime failure -> class extraction -> source/variant search -> fix -> regression -> twin replay
```

The compounding value is the lesson, not the single replay.

Runtime findings can become source intelligence. A misconfiguration pattern discovered in a twin can become a static rule, a policy-as-code rule card, a review checklist, or a variant search across infrastructure templates.

## References

- [Verification Is the Bottleneck](verification_bottleneck.md)
- [Principles for Agentic Security Assurance](agentic_security_principles.md)
- [Software Assurance](software_assurance.md)
- [Security Intelligence Pipeline](security_intelligence_pipeline.md)
- [Threat Model](threat_model.md)
- [Zero Day Clock](https://zerodayclock.com/)
- [The Dark Factory Pattern](https://hackernoon.com/the-dark-factory-pattern-moving-from-ai-assisted-to-fully-autonomous-coding)
- [Sergej Epp: 8 Minutes to Admin](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/xCtcQkJBReQ_Sergej_Epp_8_Minutes_to_Admin_We_Caught_It_in_the_Wild.md)
- [Johann Rehberger: Your Agent Works for Me Now](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/zVUm23P7ZNg_Johann_Rehberger_Your_Agent_Works_for_Me_Now.md)
- [Kyle Polley: Training BrowseSafe](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/Fzgqx1MauJg_Kyle_Polley_Training_BrowseSafe_Lessons_from_Detecting_Prompt_Injection.md)
- [Brooks McMillin: Building Secure Agentic Systems](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/SzLVXAzjOEU_Brooks_McMillin_Building_Secure_Agentic_Systems.md)

## Takeaways

!!! success "Takeaways"

    - A twin is an adversarial test instrument, separate from staging.
    - CI/CD proves known checks. A twin gives agents room for interactive exploration.
    - Build twins around security properties, not around perfect production cloning.
    - Probes, hooks, injection points, traces, and replay are the core features.
    - Runtime testing turns plausible paths into behavioral evidence.
    - Runtime-only classes include state drift, stale resources, identity state, and logging reality.
    - Do EDA before CART: know your false positives, Pareto clusters, and remediation queues.
    - Mass discovery forces proof infrastructure; otherwise the queue just gets bigger.
    - The strategic metric is time to insight actioned: find, prove, patch, verify, prevent, detect.
    - System owners need actionable proof, not a pile of plausible reports.
    - Every runtime proof should become a source-analysis seed, regression test, or preventive control.
