# Four Discovery Modes

!!! abstract "Overview"

    Vulnerability discovery is not one activity.

    A reasoning agent, a policy scan, a history review, and a source-to-sink query are different instruments. They answer different questions and fail in different ways.

    Treating them as one thing leads to bad expectations: too much faith in scanners, too little respect for history, and too much noise handed to engineers.

## The Four Modes

Use four modes:

| Mode | Question | Typical output |
|---|---|---|
| Exploratory reasoning | What is wrong here? | Novel attack paths and missing checks |
| Domain breadth scanning | Which known risk classes appear? | Broad posture findings and repeated patterns |
| Historical intelligence | What did past changes reveal? | Incomplete fixes, regressions, and high-risk hotspots |
| Semantic confirmation and MRVA | Is the path real, and where else does it exist? | Verified source-to-sink paths, variants, and PoCs |

These modes can run independently. They work best as a system.

!!! tip "Coverage principle"

    Do not ask one discovery mode to do all jobs. Diversity is coverage.

!!! observation "Overlap is not the only signal"

    If the modes are healthy, they should not all find the same bugs. Ask what class each mode would miss if you removed it.

## Mode 1: Exploratory Reasoning

Exploratory reasoning is the closest agentic equivalent of a skilled human reviewer walking the code.

It reads the system, forms hypotheses, traces trust boundaries, and tries to build a plausible attack. It is strong when the bug is semantic: the code does what it says, but what it says is unsafe.

It is especially useful for:

- authorization bypasses
- unsafe tool use
- prompt injection paths
- missing confirmation gates
- cross-context data exposure
- logic flaws not represented by a simple source-to-sink rule
- multi-step chains where one harmless-looking action enables the next

| Input | Output |
|---|---|
| Source tree, architecture notes, entrypoints, known risky surfaces | One or more candidate attack paths with source evidence and a proposed proof strategy |

The weakness is coverage. A reasoning pass can be brilliant and still miss the next file. Use it to find the sharp edge, not to prove the whole estate is safe.

## Mode 2: Domain Breadth Scanning

Breadth scanning asks a different question: which known classes appear across the system?

This is where specialized checklists, skills, rule packs, and deterministic tools work well. CI/CD security, supply chain hygiene, container hardening, cloud configuration, logging, secrets, cryptography, dependency posture, and observability all benefit from domain-specific breadth.

Breadth scanning is less elegant than exploit discovery. It is also how you find the boring risks that become incidents.

| Input | Output |
|---|---|
| Domain checklists, policy rules, code/config search, dependency and infrastructure metadata | Posture findings, repeated class candidates, and control gaps |

The weakness is depth. A breadth scan can tell you a dangerous pattern exists. It may not prove that a specific attacker can exploit it. Confirm high-value results with source tracing, runtime testing, or a PoC.

!!! info "Out-of-band scanning"

    Breadth scanning does not have to live only in CI. A portfolio-level scan can clone many codebases, normalize metadata, and look for repeated classes across ownership boundaries. That gives defenders a view attackers do not have: the whole estate at once.

## Mode 3: Historical Intelligence

Git history is security data. So are code smells.

A security fix says: somebody already found a boundary worth changing. The useful question is whether the fix changed the class or only the instance.

Historical intelligence looks for:

- awkward or overly complex code near trust boundaries
- incomplete fixes
- reverted controls
- sibling code paths missed by a patch
- churn in security-sensitive files
- repeated emergency changes near trust boundaries
- old workarounds that became permanent architecture
- security-sensitive files whose risk comes from change velocity, not size

Two sub-modes are useful.

| Sub-mode | Question | Output |
|---|---|---|
| Churn hotspot analysis | Where should expensive review start? | Files or components ranked by churn and security relevance |
| Vulnerability archaeology | Which past fixes imply unfinished work? | Fix patterns, sibling candidates, and regression seeds |

This mode is powerful because the current code can look clean. The history shows why it became that way, and whether the reason was fully addressed.

!!! tip "History as a hypothesis engine"

    Every fix commit is a hypothesis: "the class is fixed." Test that hypothesis.

## Mode 4: Semantic Confirmation and MRVA

Semantic confirmation gives structure to the search. Multi-repo variant analysis (MRVA) gives it scale.

Tools such as CodeQL can model control flow, data flow, sources, sinks, and framework APIs. Agents can then reason over that structured evidence: whether a path is reachable, whether a sanitizer is real, whether an attacker controls the source, and whether a sink actually matters.

Once a finding is confirmed, the same structure supports propagation. Search for equivalent patterns across codebases, templates, services, and frameworks. The goal is not to find the same line of code. The goal is to find the same failed assumption.

For example: a confirmed missing confirmation before an external action should not only produce one fix. It should produce a search for other actions with the same authority boundary, the same missing confirmation, or the same unsafe helper.

### The MRVA Shape

MRVA is a repeatable workflow:

```text
confirmed finding
  -> variant seed
     -> targeted corpus selection
        -> semantic or structural search
           -> LLM/context triage
              -> proximity scoring
                 -> PoC or remediation campaign
```

| Step | Purpose |
|---|---|
| Confirm the seed | Start from a real finding, not a hunch |
| Extract the class | Name the failed assumption and missing control |
| Select targets | Search systems likely to share the API, framework, template, or pattern |
| Run semantic search | Use CodeQL, structural search, or other source-aware tooling |
| Triage with context | Remove mitigated, dead, or unreachable candidates |
| Score proximity | Track how close each candidate is to mechanical exploitation |
| Promote campaigns | Fix the class, not just the first instance |

### Source, Sink, Sanitizer

Most useful semantic security queries reduce to three definitions.

| Component | Question |
|---|---|
| Source | Where does untrusted, remote, user-controlled, or attacker-influenced data enter? |
| Sink | Which operation is dangerous if that data reaches it? |
| Sanitizer or barrier | Which validation, escaping, authorization, confirmation, or deployment control blocks exploitation? |

For MRVA, these definitions should come from confirmed findings whenever possible. A real source-to-sink path teaches you what the generic query should look for.

### Execution Models

There is no single MRVA execution model.

| Model | Best for | Trade-off |
|---|---|---|
| Local CodeQL fan-out | Private, regulated, or offline code where databases must be built locally | Most control, more setup |
| Downloaded pre-built databases | Public or hosted code where CodeQL databases already exist | Fast start, limited by database availability |
| IDE multi-database execution | Interactive query development and analyst review | Excellent for iteration, less ideal for scheduled campaigns |
| Hosted or hybrid MRVA | Large repo-list execution with platform orchestration | Less local control, more built-in orchestration |
| Structural search plus agent triage | Patterns that are not worth a full dataflow query yet | Fast and flexible, weaker proof |

The execution choice is environmental. The assurance pattern is stable: seed, search, verify, score, remediate, feed back.

## Why Overlap Should Be Low

If every mode finds the same things, the system is redundant.

Low overlap is not a failure when the modes are designed to see different surfaces. Exploratory reasoning should find semantic chains. Breadth scanning should find posture gaps. History should find incomplete fixes. Semantic propagation should find variants.

The review question is not "Which mode won?" It is "Which classes would we have missed if we removed this mode?"

## Operating Pattern

A practical run looks like this:

1. Use intelligence to choose targets and themes.
2. Run exploratory reasoning for high-impact chains.
3. Run domain breadth scans for class coverage.
4. Mine history for incomplete fixes and hotspots.
5. Use semantic analysis to confirm paths.
6. Run MRVA to propagate confirmed classes.
7. Feed findings, false positives, and fixes back into the next run.

## References

- [Security Intelligence Pipeline](security_intelligence_pipeline.md)
- [Variant Analysis and Class Eradication](variant_analysis_class_eradication.md)
- [Principles for Agentic Security Assurance](agentic_security_principles.md)
- [Policy-as-Code Served Pre and Post Coding](pre_post_policy_as_code.md)
- [CodeQL documentation](https://codeql.github.com/docs/)
- [GitHub: Multi-repository variant analysis](https://github.blog/security/vulnerability-research/multi-repository-variant-analysis-a-new-way-to-perform-security-research/)
- [Trail of Bits mrva](https://github.com/trailofbits/mrva)

## Takeaways

!!! success "Takeaways"

    - No single discovery mode subsumes the others.
    - Exploratory reasoning finds semantic chains and missing checks.
    - Domain breadth scanning finds posture and policy classes that deep review may never choose.
    - Historical intelligence turns past fixes into current hypotheses.
    - MRVA turns one confirmed finding into a class-level search.
    - Source/sink/sanitizer modeling is the practical heart of semantic security queries.
    - Low overlap between modes is useful when each mode sees a different surface.
    - The operating pattern is portfolio, not pipeline monoculture.
