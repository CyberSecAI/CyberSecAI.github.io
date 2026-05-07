# Security Intelligence Pipeline

!!! abstract "Overview"

    The bottleneck has moved.

    Finding possible vulnerabilities is getting cheaper. Turning those possibilities into evidence-backed, prioritized, fixed, and regression-tested outcomes is the hard part.

    An agentic security pipeline should not be a single scanner. It should be an intelligence system that decides what to look for, where to look, how to verify it, and how to make the next run smarter.

## The Pipeline Shape

The useful loop is simple.

!!! tip "Pipeline loop"

    ```text
    intelligence -> discovery -> verification -> judgment -> remediation -> propagation -> feedback
    ```

Each stage has a different job.

| Stage | Question | Output |
|---|---|---|
| Intelligence | What should we look for and where? | Priority targets, threat themes, historical signals |
| Discovery | What might be wrong? | Candidate findings |
| Verification | Is it real? | Evidence, reproduction, exploitability notes |
| Judgment | How important is it? | Severity, proximity, deduplication, ownership |
| Remediation | What should change? | Patch, control change, test, or architecture update |
| Propagation | Where else could it exist? | Variant search and class-level campaign |
| Feedback | What did we learn? | Tuning, suppressions, new rules, new tests |

## The Discovery Funnel

The funnel starts wide and ends narrow.

It begins with an owned software portfolio: many repositories, many languages, many dependency ecosystems, and uneven security history. The goal is not to scan everything with the most expensive method. The goal is to route attention through increasingly precise stages until only evidence-backed findings remain.

This often works better out of band than inside a single repository. Clone the portfolio, build the index, run cross-repo intelligence, and then hand product teams only the evidence-backed work they need to own. CI still matters, but CI is not the only place security reasoning should happen.

!!! info "Generic discovery funnel"

    ```text
    Portfolio input
      -> intelligence gathering
         -> target and pattern prioritization
            -> complementary discovery modes
               -> consolidation and deduplication
                  -> verification and proximity scoring
                     -> remediation, variant search, and feedback
    ```

Each stage reduces a different kind of uncertainty.

| Funnel stage | Reduces uncertainty about |
|---|---|
| Portfolio input | What software is in scope |
| Intelligence gathering | Which systems, patterns, and vulnerability classes deserve attention |
| Target prioritization | Where expensive reasoning should be spent first |
| Complementary discovery | Which candidate findings exist across code, configuration, history, and runtime |
| Consolidation and deduplication | Which reports are the same failed assumption |
| Verification and proximity scoring | Which findings are real, exploitable, and close to proof |
| Remediation and feedback | Which fixes, tests, and rules make the next run better |

This is the important move: the funnel is not a report generator. It is a decision system.

## Intelligence Comes First

Blind scanning wastes agent time and reviewer attention.

Good intelligence narrows the search without making it brittle. It combines dependency alerts, historical fixes, churn, architecture notes, threat models, bug bounty themes, production incidents, known dangerous patterns, and code smells.

The point is not to predict every vulnerability. The point is to spend expensive reasoning on the code and designs where mistakes are most likely to matter.

| Signal | Why it matters |
|---|---|
| Security-relevant code smells | Unsafe complexity, ad hoc parsing, duplicated controls, and awkward fixes are often where vulnerabilities start |
| Recent churn in security-relevant files | Bugs cluster around change |
| Historical security fixes | Incomplete fixes and sibling variants are common |
| Repeated framework patterns | One bad pattern often appears across many services |
| Architecture trust boundaries | Missing controls are often design-level |
| Runtime incidents or alerts | Production behavior exposes assumptions source cannot show |

!!! tip "Core heuristic"

    Past vulnerabilities predict future ones. A confirmed weakness in one component often appears again as a variant in sibling components, shared templates, copied helpers, generated code, or repeated architecture patterns.

## Discovery Needs Multiple Lenses

No single method sees the whole system.

Exploratory reasoning finds logic flaws and missing checks. Domain scans find broad configuration and posture issues. Git history finds incomplete fixes. Semantic analysis finds source-to-sink paths. Runtime testing finds behavior that source cannot prove.

These are complements, not substitutes.

| Lens | Good at | Weak at |
|---|---|---|
| Exploratory reasoning | Novel chains, logic bugs, missing checks | Coverage guarantees |
| Domain breadth scans | Repeated posture issues, configuration classes | Deep exploit proof |
| History mining | Incomplete fixes, regressions, sibling variants | Brand-new code with no history |
| Semantic source-to-sink analysis | Dataflow, reachability, path evidence | Design intent and runtime state |
| Runtime probing | Operational truth, exploit preconditions | Exhaustive source coverage |

## History Feeds Variant Analysis

The history and variant workstreams should feed each other.

Git history answers: what changed, what was fixed, what was reverted, and what code remained adjacent to the fix. Variant analysis answers: where else does the same failed assumption exist now?

!!! info "History-to-variant loop"

    ```text
    historical fix or regression
      -> extract the failed assumption
         -> search current code for variants
            -> verify candidates
               -> feed confirmed classes back into history and future scans
    ```

This is why history is not only audit evidence. It is discovery intelligence.

## Verification Is Load-Bearing

Candidate findings are cheap. Verified findings are valuable.

Verification should be adversarial. It should try to disprove the finding, not merely decorate it.

!!! info "Verifier questions"

    - Is the source path real?
    - Is the input attacker-controlled?
    - Is the sink reachable?
    - Does another control break the chain?
    - Can the behavior be reproduced?
    - Does the remediation close the path without breaking intended use?

This is where many agentic systems fail. They optimize for plausible reports instead of reproducible evidence.

## Judgment Turns Findings Into Work

A finding is not ready for engineering until it has been judged.

Judgment means deduplicating variants, ranking by real risk, assigning ownership, and separating "fix now" from "campaign later." This is also where the pipeline should decide whether the right output is a patch, a design change, a policy rule, a regression test, or a broader class-eradication effort.

| Judgment dimension | Question |
|---|---|
| Exposure | Can an attacker reach it? |
| Proximity | How mechanically close is this to successful exploitation? |
| Blast radius | What can be read, changed, or triggered? |
| Control maturity | Is this one bug or a missing class of control? |
| Fix shape | Patch, test, rule, architecture change, or campaign? |

## Proximity Tracks Exploitation Distance

Proximity is not severity. It is the evidence ladder from "this looks dangerous" to "the exploit works."

!!! info "Proximity scale"

    | Score | Meaning | Evidence standard |
    |---|---|---|
    | 0 | No viable path | No exploitable flow identified. |
    | 1 | Sink found | Dangerous API, unsafe operation, or security-sensitive sink exists. |
    | 2 | Sink reached | Attacker-controlled or remote-influenced input reaches the sink, but a barrier remains. |
    | 3 | Barrier absent or bypassed | Source-to-sink path exists with no effective sanitizer, guard, or deployment barrier. |
    | 4 | Payload constructable | A concrete attack input can be specified, but one remaining defense or runtime unknown blocks full proof. |
    | 5 | Exploit proven | PoC executes, or exploitation is mechanically proven end to end. |

Severity tells impact. Proximity tells how much evidence exists that the impact can be realized.

## Propagation Is the Multiplier

The biggest advantage defenders have is owned-system visibility.

An external attacker sees one exposed surface at a time. A defender can search every codebase, design pattern, and deployment template they own. A confirmed finding should become a seed for variant analysis.

The seed should capture the class, not just the instance:

- vulnerable pattern
- missing control
- required preconditions
- framework or language markers
- false-positive signatures
- remediation pattern

## Feedback Makes the System Compound

Every run should improve the next run.

False positives should reduce future noise. Confirmed findings should add new seeds. Remediations should add tests. Repeated patterns should become rule cards, skills, prompts, or static checks. Human review decisions should be captured as training signal for the process, not trapped in chat transcripts.

The feedback loop is where agentic security becomes engineering instead of theater.

!!! tip "Compounding effect"

    - A false positive becomes a suppression, verifier check, or better query.
    - A confirmed finding becomes a variant seed.
    - A fix becomes a regression test.
    - A repeated class becomes policy-as-code or design guidance.
    - A runtime proof becomes a source-analysis pattern.
    - A reviewer decision becomes future triage guidance.

## References

- [Principles for Agentic Security Assurance](agentic_security_principles.md)
- [Software Assurance](software_assurance.md)
- [Software Artifacts](software_artifacts.md)
- [Policy-as-Code Served Pre and Post Coding](pre_post_policy_as_code.md)
- [GitHub: Multi-repository variant analysis](https://github.blog/security/vulnerability-research/multi-repository-variant-analysis-a-new-way-to-perform-security-research/)

## Takeaways

!!! success "Takeaways"

    - The scanner is one stage. The pipeline is the product.
    - The funnel starts broad and ends narrow: portfolio, intelligence, prioritization, discovery, deduplication, verification, remediation, feedback.
    - Start with the map. Agentic discovery is more effective when intelligence directs attention.
    - Past vulnerabilities predict future ones; confirmed classes should become search seeds.
    - Use overlap as a signal, but do not expect overlap. Different lenses should find different classes.
    - History feeds variant analysis, and variant findings should be checked against history.
    - The verifier is the trust boundary of the pipeline.
    - Prioritization should reward exploitability and blast radius, not report drama.
    - One verified bug should teach the organization how to find the whole family.
    - If the second run is not smarter than the first, you built a workflow, not a system.
