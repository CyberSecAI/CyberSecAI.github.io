# Security Intelligence Pipeline

!!! abstract "Overview"

    The bottleneck has moved.

    Agentic search makes candidate vulnerabilities cheaper. Evidence-backed, prioritized, fixed, regression-tested outcomes remain hard.

    If the output is only a longer findings list, the pipeline has failed. The work is to decide what to look for, where to look, how to prove it, and how the next run becomes harder to fool.

    Treat the pipeline as the product. The scanner is one component.

## The Shift: Stock, Flow, and Zero-Days

Security teams now face two queues.

| Queue | What it contains | Why the old model struggles |
|---|---|---|
| Existing debt | Vulnerabilities already present in mature code | CI only sees new changes |
| Incoming risk | New code, new CVEs, and AI-discovered zero-days | CVE-centric tooling only sees named vulnerabilities |

In-band scanning protects the flow: new commits, pull requests, pipeline gates. Out-of-band scanning protects the stock: the existing estate, old services, forgotten code paths, incomplete fixes, and cross-repo variants.

!!! observation "Stock vs flow"

    In-band checks are necessary. They do not answer the question, "What is already vulnerable in the code we have?" Out-of-band intelligence exists to answer that question.

The zero-day gap is the other pressure point. EPSS, KEV, CVSS, and dependency advisories assume the vulnerability has a name. AI-discovered zero-days start as a path through your code. Anthropic's AI-accelerated offense guidance, the Zero Day Clock, and the [un]prompted 2026 "8 Minutes to Admin" case point at the same problem: calendar-speed vulnerability management against machine-speed discovery.

## The Pipeline Shape

The loop is simple. The discipline is keeping the stages separate.

!!! tip "Pipeline loop"

    ```text
    intelligence -> find -> verify -> judge -> patch -> campaign -> learn
    ```

Each stage has a different job.

| Stage | Question | Output |
|---|---|---|
| Intelligence | What should we look for and where? | Priority targets, threat themes, historical signals |
| Find | What might be wrong? | Candidate findings |
| Verify | Is it real? | Evidence, reproduction, exploitability notes |
| Judge | How important is it? | Severity, proximity, deduplication, ownership |
| Patch | What should change? | Patch, control change, test, or architecture update |
| Campaign | Where else could it exist, and how do we keep it gone? | Variant search, class eradication, prevention control |
| Feedback | What did we learn? | Tuning, suppressions, new rules, new tests |

!!! observation "Pipeline over scanner"

    A scanner produces candidates. A security intelligence pipeline produces decisions: reject, prove, fix, campaign, suppress, or turn into a reusable rule.

## Three Capabilities, One System

Pair source scanning with runtime verification and data intelligence.

| Capability | Primary question | Examples |
|---|---|---|
| Source code intelligence | What is wrong in the code? | Missing checks, logic flaws, incomplete fixes, source-to-sink paths, variants |
| Runtime verification | What is actually exploitable or drifting in behavior? | Ineffective controls, identity state, logging not flowing, stale resources, lateral movement |
| Data intelligence | Where should we spend attention? | Pareto effects, false-positive rate, remediation survival curves, detection-to-action gaps |

Connect these capabilities so one confirmed issue changes what the system looks for next. That is the through-line from [Software Engineering Security](swe_redux_security.md) and [DARPA AIxCC](aixcc.md): orchestration, structured evidence, validation, and feedback beat a single clever prompt.

## The Discovery Funnel

The funnel starts wide and ends narrow.

Start with the owned software portfolio: many repositories, many languages, many dependency ecosystems, uneven security history. Route attention through increasingly precise stages until only evidence-backed findings remain.

Run this out of band. Clone the portfolio, build the index, run cross-repo intelligence, and hand system owners evidence-backed work. CI still matters. It is no longer the only place security reasoning should happen.

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

| Funnel stage | Reduces uncertainty about |
|---|---|
| Portfolio input | What software is in scope |
| Intelligence gathering | Which systems, patterns, and vulnerability classes deserve attention |
| Target prioritization | Where expensive reasoning should be spent first |
| Complementary discovery | Which candidate findings exist across code, configuration, history, and runtime |
| Consolidation and deduplication | Which reports are the same failed assumption |
| Verification and proximity scoring | Which findings are real, exploitable, and close to proof |
| Remediation and feedback | Which fixes, tests, and rules make the next run better |

Do not run the most expensive agentic review everywhere and call it coverage. Use cheap signals first, spend reasoning where the signal is strongest, and demand stronger evidence as the candidate moves down the funnel.

## Intelligence Comes First

Good intelligence narrows the search without making it brittle. It combines dependency alerts, historical fixes, churn, architecture notes, threat models, bug bounty themes, production incidents, known dangerous patterns, and code smells.

Spend expensive reasoning on the code and designs where mistakes are most likely to matter.

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

!!! observation "Code smells are routing signals"

    Awkward parsing, duplicated authorization checks, hand-rolled escaping, high churn around trust boundaries, and fixes that only touch one caller are not vulnerabilities by themselves. They are places where expensive review is more likely to pay rent.

## Skills Package Expert Judgment

The scalable unit is the skill.

A useful security skill packages a repeatable expert lens: code smells, target files, tool sequence, promotion evidence, false-positive suppressions, and remediation shape.

The expert does not restart every investigation from first principles. The skill carries the checklist, disproof questions, and promotion standard into the next run.

| Skill element | What it preserves |
|---|---|
| Smell model | The code or history patterns worth routing to expensive review |
| Tool sequence | The static, semantic, runtime, or history checks to run |
| Evidence rule | What turns a suspicion into a promoted finding |
| False-positive memory | Why similar-looking candidates were rejected before |
| Fix guidance | The preferred patch, test, policy, or campaign shape |

!!! observation "Skills route; verifiers decide"

    A skill proposes where to look and how to test. The verifier still decides what is real.

## Investigation Stages

Use four investigation stages.

| Stage | Name | Question | Output |
|---|---|---|---|
| A | Code churn hotspot | Where should expensive review start? | Files or components ranked by churn and security relevance |
| B | Vulnerability archaeology | What history matters? | Incomplete fixes, sibling candidates, regression seeds |
| C | CodeQL + LLM bridge | Is it semantically real? | Triaged source-to-sink paths with exploitability notes |
| D | Variant analysis | Where else does it exist? | Cross-codebase candidates and campaign scope |

The stages compound: Stage B produces seeds, Stage C tests them, Stage D propagates confirmed paths into campaign scope.

Public examples show the same shape. Source-to-sink LLM discovery uses structured path evidence to reduce shallow prompting. FENRIR reports deterministic pre-filtering that reduces hundreds of raw alerts to tens of high-confidence reports before deep verification. Trail of Bits describes the organizational version: compound expert audit knowledge into reusable agents.

## Discovery Needs Multiple Lenses

Exploratory reasoning finds logic flaws and missing checks. Domain scans find broad configuration and posture issues. Git history finds incomplete fixes. Semantic analysis finds source-to-sink paths. Runtime testing finds behavior that source cannot prove.

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

History doubles as discovery intelligence.

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

Many agentic systems optimize for plausible reports instead of reproducible evidence.

## Judgment Turns Findings Into Work

Engineering needs judged findings.

Judgment means deduplicating variants, ranking by real risk, assigning ownership, and choosing the output: patch, design change, policy rule, regression test, or class-eradication campaign.

| Judgment dimension | Question |
|---|---|
| Exposure | Can an attacker reach it? |
| Proximity | How mechanically close is this to successful exploitation? |
| Blast radius | What can be read, changed, or triggered? |
| Control maturity | Is this one bug or a missing class of control? |
| Fix shape | Patch, test, rule, architecture change, or campaign? |

## Proximity Tracks Exploitation Distance

Severity and proximity answer different questions. Proximity is the evidence ladder from "this looks dangerous" to "the exploit works."

!!! info "Proximity scale"

    | Score | Meaning | Evidence standard |
    |---|---|---|
    | 0 | No viable path | No exploitable flow identified. |
    | 1 | Sink found | Dangerous API, unsafe operation, or security-sensitive sink exists. |
    | 2 | Sink reached | Attacker-controlled or remote-influenced input reaches the sink, but a barrier remains. |
    | 3 | Barrier absent or bypassed | Source-to-sink path exists with no effective sanitizer, guard, or deployment barrier. |
    | 4 | Payload constructable | The source, sink, and absent or bypassed barrier are known; a concrete attack input can be specified, but full execution is not yet proven. |
    | 5 | Exploit proven | PoC executes, or exploitation is mechanically proven end to end. |

Severity tells impact. Proximity tells how much evidence exists that the impact can be realized.

## Propagation Is the Multiplier

Defenders have owned-system visibility.

An external attacker sees one exposed surface at a time. A defender can search every codebase, design pattern, and deployment template they own. A confirmed finding should become a seed for variant analysis.

The seed should capture class-level structure:

- vulnerable pattern
- missing control
- required preconditions
- framework or language markers
- false-positive signatures
- remediation pattern

## Feedback Makes the System Compound

False positives should reduce future noise. Confirmed findings should add new seeds. Remediations should add tests. Repeated patterns should become rule cards, skills, prompts, or static checks. Human review decisions should be captured as training signal for the process, not trapped in chat transcripts.

Compounding turns agentic security into engineering.

!!! tip "Compounding effect"

    - A false positive becomes a suppression, verifier check, or better query.
    - A confirmed finding becomes a variant seed.
    - A fix becomes a regression test.
    - A repeated class becomes policy-as-code or design guidance.
    - A runtime proof becomes a source-analysis pattern.
    - A reviewer decision becomes future triage guidance.

## Evidence Gates and Metrics

Measure the programme, not the tool.

| Metric | What it tells you |
|---|---|
| Coverage | Which high-risk systems have been scanned at least once |
| Triage speed | Whether findings move to an owned decision quickly |
| False-positive rate | Whether the verifier is protecting engineering attention |
| Signal quality | How many high-severity findings have verified exploitability |
| Patch velocity | Whether proven risk is being closed fast enough |
| Class eradication | Whether campaigns remove the family, not only the first instance |
| Model portability | Whether the system depends on one model or one vendor |

!!! warning "Common failure mode"

    A scanner that finds 10,000 issues but cannot triage them has not succeeded. A pipeline that triages 50 findings and eradicates one vulnerability class has.

!!! tip "Discovery as forcing function"

    Once discovery can produce many high-confidence candidates, the programme has to mature. The constraint moves from "can we find it?" to "can we prove it, assign it, fix it, and keep the class gone?"

!!! info "Reference trail"

    - [Software Engineering Security](swe_redux_security.md) covers the source-code security foundation.
    - [DARPA AIxCC](aixcc.md) shows autonomous find-and-fix systems as an engineering discipline.
    - Source-to-sink discovery, FENRIR, and Trail of Bits provide public examples of the staged, evidence-first pattern.

## References

- [Principles for Agentic Security Assurance](agentic_security_principles.md)
- [Software Assurance](software_assurance.md)
- [Software Artifacts](software_artifacts.md)
- [Policy-as-Code Served Pre and Post Coding](pre_post_policy_as_code.md)
- [Software Engineering Security](swe_redux_security.md)
- [DARPA AI Cyber Challenge Tools Comparison](aixcc.md)
- [Anthropic: Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense)
- [Zero Day Clock](https://zerodayclock.com/)
- [Sergej Epp: 8 Minutes to Admin](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/xCtcQkJBReQ_Sergej_Epp_8_Minutes_to_Admin_We_Caught_It_in_the_Wild.md)
- [Scott Behrens and Justice Cassel: Source to Sink](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/bxwEZMhqeR0_Scott_Behrens_Justice_Cassel_Source_to_Sink_Improving_LLM_Vuln_Discovery.md)
- [Meta FENRIR: AI Hunting for AI Zero-Days at Scale](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/c6_bRzHCf3U_Peter_Girnus_Derek_Chen_FENRIR_AI_Hunting_for_AI_Zero-Days_at_Scale.md)
- [Dan Guido: 200 Bugs/Week/Engineer](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/kgwvAyF7qsA_Dan_Guido_200_Bugs_Week_Engineer_How_We_Rebuilt_Trail_of_Bits_Around_AI.md)
- [GitHub: Multi-repository variant analysis](https://github.blog/security/vulnerability-research/multi-repository-variant-analysis-a-new-way-to-perform-security-research/)

## Takeaways

!!! success "Takeaways"

    - The scanner is one stage. The pipeline is the product.
    - In-band scanning protects the flow. Out-of-band intelligence protects the stock.
    - CVE-centric prioritization is necessary, but it misses vulnerabilities that have not been named yet.
    - Source code intelligence, runtime verification, and data intelligence must feed one system.
    - The funnel starts broad and ends narrow: portfolio, intelligence, prioritization, discovery, deduplication, verification, remediation, feedback.
    - Skills are packaged expert judgment: smell model, tool sequence, evidence rule, false-positive memory, and fix guidance.
    - Use Stage A-D to keep the work concrete: churn, archaeology, semantic confirmation, variant analysis.
    - Past vulnerabilities predict future ones; confirmed classes should become search seeds.
    - Use overlap as a signal, but do not expect overlap. Different lenses should find different classes.
    - History feeds variant analysis, and variant findings should be checked against history.
    - The verifier is the trust boundary of the pipeline.
    - Prioritization should reward exploitability and blast radius, not report drama.
    - One verified bug should teach the organization how to find the whole family.
    - If the second run is not smarter than the first, you built a workflow, not a system.
