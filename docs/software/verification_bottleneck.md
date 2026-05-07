# Verification Is the Bottleneck

!!! abstract "Overview"

    Agentic discovery creates more leads than humans can triage by hand.

    That is not a security outcome unless verification scales with it. A pile of plausible findings is an attention attack on your own engineers; eventually they stop trusting the queue.

    The verifier is the trust boundary of the pipeline. It decides what is real, what is exploitable, what should be fixed now, and what should become a broader class-eradication campaign.

## What Verification Must Prove

Verification turns a candidate into an evidence-backed decision.

It does not always need a weaponized exploit. It does need enough proof to classify the finding, reject it, or identify the missing evidence.

| Evidence tier | What it proves | When it is enough |
|---|---|---|
| Source evidence | The pattern exists in code | Early triage and variant search |
| Reachability evidence | Attacker-controlled input can reach the sink | Promotion to probable finding |
| Reproduction | Behavior occurs in a controlled setting | High-confidence vulnerability |
| Runtime proof | The exploit works under realistic preconditions | Critical or high-risk prioritization |
| Regression test | The fix closes the path | Remediation acceptance |

!!! tip "Verification ladder"

    Verification is not one technique. It is a ladder of confidence. Use the lightest evidence that can answer the disputed security question.

## Try to Disprove the Finding

The best verifier is adversarial.

It asks why the finding might be wrong:

- Is the cited code still present?
- Is the input actually attacker-controlled?
- Is there an upstream validator?
- Is the sink reachable in the deployed configuration?
- Is the dangerous branch dead code?
- Is the impact blocked by permissions, isolation, or user confirmation?
- Is the report a duplicate of the same root cause?

This is where critical thinking belongs in the pipeline. A confident agent report without disproof attempts is not yet analysis.

## Proofs of Concept Are Tools, Not Trophies

A PoC has one job: reduce uncertainty.

Sometimes a small script is enough. Sometimes a unit test is better. Sometimes runtime interaction in an isolated twin is required. The PoC should match the disputed assumption.

| Disputed assumption | Useful PoC shape |
|---|---|
| Parser accepts unsafe input | Minimal parser test |
| Sanitizer is bypassable | Payload matrix |
| Tool call can be redirected | Controlled interaction scenario |
| Cross-context data can leak | Isolated runtime reproduction |
| Fix works | Regression test using the old payload |

The goal is decision-quality evidence. Spectacle adds noise.

!!! observation "Match the proof to the doubt"

    If the doubt is "does the parser accept this shape?", write the parser test. If the doubt is "can a user actually reach this action?", use a runtime replay. A bigger PoC is not automatically a better PoC.

## Proximity Scores Evidence, Not Drama

Proximity is the exploitation-distance score used to decide how close a finding is to a working exploit.

!!! info "Proximity scale"

    | Score | Meaning | How to read it |
    |---|---|---|
    | 0 | No viable path | Not a finding, or structurally unreachable. |
    | 1 | Sink found | A dangerous operation exists, but attacker-controlled input has not been shown to reach it. |
    | 2 | Sink reached | Attacker-controlled input reaches the sink, but a sanitizer, guard, framework mitigation, or deployment constraint blocks exploitation. |
    | 3 | Barrier absent or bypassed | The source-to-sink path exists with no effective sanitizer, guard, or deployment barrier. |
    | 4 | Payload constructable | The source, sink, and missing barrier are confirmed; a concrete attack input can be described, but full execution is not yet proven. |
    | 5 | Exploit proven | The exploit is mechanically demonstrated end to end. |

!!! tip "Scoring discipline"

    - P4 requires a concrete payload or attack input. If the exact input cannot be specified, cap at P3.
    - P3 requires demonstrated barrier absence. If a sanitizer, auth gate, framework mitigation, or deployment constraint remains, cap at P2.
    - P5 requires execution or mechanical proof of the full chain, not just a convincing story.

Severity tells impact. Proximity tells how much evidence exists that the impact can be realized.

## Deduplicate by Failed Assumption

Agentic discovery often reports symptoms as separate vulnerabilities.

That is useful during discovery and dangerous during planning. If five reports share one missing control, engineering should usually fix the control, not chase five isolated patches.

Deduplication should preserve evidence while grouping by root cause:

- same missing authorization gate
- same sanitizer gap across surfaces
- same unsafe helper used by multiple callers
- same deployment template repeated across environments
- same trust-boundary assumption copied across tools

The grouping unit is the failed assumption, not the file path.

## Severity Needs Preconditions

Severity without preconditions is storytelling.

A useful verified finding states what the attacker needs:

- network position
- authentication level
- user interaction
- feature flag
- tenant boundary
- victim state
- required timing
- target configuration

This protects both sides. Security avoids exaggeration. Engineering sees what must be true for exploitation.

## Remediation Must Be Verified Too

A fix is also a hypothesis.

It says: this change removes the vulnerability without breaking intended behavior. Verification has to test both halves.

The remediation acceptance test should include:

- the old exploit or failure mode no longer works
- expected behavior still works
- sibling paths are checked
- the class is represented in a regression test, rule, or review checklist
- the decision is documented when the fix is a trade-off

This is where twin environments matter. They let teams replay the old path, observe the new behavior, and catch unintended breakage before the fix becomes another incident.

The word "fixed" should mean two things: the old path is closed, and the intended path still works.

## Time to Insight Actioned

Candidate count is a volume metric. It does not tell you whether risk moved.

Track how quickly the pipeline turns a candidate into an actioned outcome:

```text
candidate -> verified finding -> prioritized work -> patch -> regression -> variant search -> prevention
```

| Metric | Why it matters |
|---|---|
| Time to verification | Measures whether discovery volume is overwhelming triage |
| Time to remediation | Measures whether proven risk is reaching ownership and closure |
| False-positive rate | Measures trust in the pipeline |
| Confirmed finding rate | Measures discovery quality |
| Proximity distribution | Measures evidence strength, not just severity labels |
| Findings converted into tests or rules | Measures compounding learning |

The bottleneck moves as the system improves. First it is discovery. Then verification. Then remediation. Then prevention.

## References

- [Principles for Agentic Security Assurance](agentic_security_principles.md)
- [Software Assurance](software_assurance.md)
- [Security Intelligence Pipeline](security_intelligence_pipeline.md)
- [Twin Environments and Continuous Runtime Testing](twin_environments_cart.md)
- [Software Artifacts](software_artifacts.md)

## Takeaways

!!! success "Takeaways"

    - Candidate findings are cheap. Verified findings are valuable.
    - The verifier should try to disprove the report before promoting it.
    - A PoC is a decision tool, not a trophy.
    - Proximity measures exploitation distance; severity measures impact.
    - Deduplicate by failed assumption so teams can fix the control, not the symptoms.
    - Preconditions are part of the vulnerability.
    - Remediation is not done until the old path is closed and intended behavior still works.
    - The metric that matters is time to insight actioned.
