# Variant Analysis and Class Eradication

!!! abstract "Overview"

    Fixing one vulnerability is necessary. Finding the family is leverage.

    A confirmed bug tells you more than "this line is wrong." It reveals a failed assumption that may exist elsewhere: in sibling code, shared helpers, copied templates, generated projects, infrastructure modules, or agent tools that reuse the same trust model.

## From Instance to Class

The first task after confirmation is abstraction.

Ask what class the finding belongs to:

- missing authorization check
- unsafe parser assumption
- incomplete sanitization
- cross-context data exposure
- tool action without confirmation
- secret or token reachable from the wrong boundary
- fail-open safety control
- untrusted content treated as instruction

The class is what you propagate. The instance is only the first witness.

## Build a Variant Seed

A useful variant seed is structured.

It should capture enough detail for another reviewer or agent to search without rediscovering the whole issue.

| Seed field | Purpose |
|---|---|
| Class | The failed security assumption |
| Source shape | Where untrusted input, state, or authority enters |
| Sink shape | What dangerous action, disclosure, or state change occurs |
| Missing control | The check, isolation, validation, or confirmation that should exist |
| Preconditions | What must be true for exploitation |
| False-positive clues | Patterns that look similar but are safe |
| Remediation shape | The preferred class-level fix |

!!! tip "Seed discipline"

    Variant analysis improves when seeds describe structure, not just keywords.

## MRVA: Multi-Repo Variant Analysis

Multi-repo variant analysis takes a confirmed vulnerability class and searches owned codebases for structurally equivalent instances.

It is not just search. It is search plus evidence. A good MRVA run keeps the original proof, adapts the pattern to each target, and independently verifies every promoted candidate.

```text
confirmed seed
  -> source/sink/barrier model
     -> target selection
        -> query or structural search
           -> contextual triage
              -> proximity score
                 -> ticket, fix, test, or campaign
```

| MRVA stage | What happens |
|---|---|
| Seed | Start from a confirmed finding with evidence |
| Model | Extract the source, sink, missing control, and false-positive clues |
| Target | Choose likely repos, services, languages, frameworks, or templates |
| Search | Run CodeQL, structural queries, text search, or agent-assisted review |
| Triage | Remove mitigated, unreachable, test-only, or dead-code matches |
| Score | Assign proximity based on exploitation distance |
| Act | Produce a fix, regression test, policy rule, or class campaign |

## Source, Sink, Barrier

The practical heart of MRVA is source, sink, and barrier modeling.

| Element | Question | Example categories |
|---|---|---|
| Source | Where does attacker-influenced data or authority enter? | request fields, uploaded files, headers, tool results, untrusted content, config |
| Sink | What becomes dangerous if reached? | execution, deserialization, query construction, rendering, navigation, logging, outbound communication |
| Barrier | What should stop exploitation? | sanitizer, parser, authorization, confirmation, isolation, framework default, deployment policy |

The barrier matters as much as the source and sink. Many false positives are really barrier misunderstandings: a framework escape, a route-level authorization check, a disabled code path, or a deployment constraint.

## Execution Models

MRVA can run several ways. The right model depends on data sensitivity, database availability, and analyst workflow.

| Model | Best for | Watch out for |
|---|---|---|
| Local CodeQL fan-out | Private, regulated, or offline code | Database build cost and language build requirements |
| Downloaded pre-built databases | Public or hosted code with existing CodeQL databases | Database availability and freshness |
| IDE multi-database execution | Interactive query development | Harder to schedule as a recurring campaign |
| Hosted or hybrid MRVA | Large repo-list orchestration | More platform coupling and less local control |
| Structural search plus agent triage | Early exploration before a full semantic query exists | Weaker proof and more manual verification |

!!! info "Execution principle"

    The orchestration can vary. The assurance contract should not: seed, search, verify, score, remediate, feed back.

## Query Development Lifecycle

For semantic MRVA, query development should be staged.

1. Start with the confirmed finding and write the smallest query that rediscovers it.
2. Add sources and sinks for the relevant framework or library.
3. Add sanitizer or barrier logic to remove known-safe flows.
4. Run against a small corpus and inspect false positives.
5. Promote to broader fan-out only when the query returns useful signal.
6. Feed confirmed variants and false positives back into the query.

| Query style | Good for | Cost |
|---|---|---|
| Pattern query | API misuse, missing check, dangerous call | Low |
| Local dataflow | Same-function or nearby source-to-sink paths | Medium |
| Global dataflow | Cross-function and framework-mediated flows | Higher |

Path-heavy queries are powerful but expensive. Use intelligence and target selection to avoid running the heaviest query everywhere.

## Search Broadly, Verify Narrowly

Variant search should be broad. Variant promotion should be strict.

Use text search, semantic search, CodeQL, framework-specific queries, dependency graphs, and agent review to find candidates. Then verify each candidate independently. Similar code is not automatically vulnerable.

| Search method | Good use |
|---|---|
| Text search | Fast keyword and API discovery |
| Structural search | Similar call patterns and wrappers |
| CodeQL or static analysis | Source-to-sink propagation |
| Agent review | Framework adaptation and missing-code reasoning |
| Runtime test | Behavior under realistic preconditions |

## Fix the Class, Not the Symptom

Instance fixes are sometimes unavoidable. They should not be the default.

A class fix changes the shared abstraction, default, policy, generator, template, rule pack, or test harness so the same issue becomes harder to recreate.

| Symptom fix | Class fix |
|---|---|
| Add one missing check | Move the check into the shared authorization layer |
| Escape one rendering path | Centralize safe rendering and ban unsafe bypasses |
| Patch one parser bypass | Replace ad hoc parsing with a real parser |
| Add one confirmation | Define action-risk levels and enforce confirmation centrally |
| Fix one template | Update the generator and scan generated outputs |

## Regression Checks Keep the Class Dead

A class is not eradicated until it is hard to reintroduce.

Regression can take several forms:

- unit tests for the old payload
- integration tests for the old chain
- static rules for the unsafe pattern
- policy-as-code rule cards
- architecture checklist updates
- generator/template changes
- code review guidance

This is where [Policy-as-Code Served Pre and Post Coding](pre_post_policy_as_code.md) becomes practical. A lesson from one bug becomes a reusable rule that can guide design and review before the next bug exists.

## Campaigns Beat Whack-a-Mole

When a variant search finds a repeated class, treat it as a campaign.

A campaign has a defined class, scope, owner, remediation pattern, verification method, and closure criteria. It should not be a loose collection of tickets.

| Campaign element | Question |
|---|---|
| Class definition | What exact failed assumption are we eradicating? |
| Scope | Which systems, languages, templates, or workflows are in bounds? |
| Detection | How do we find candidates? |
| Verification | How do we prove real risk? |
| Remediation | What is the preferred class-level fix? |
| Prevention | Which rule, test, or design change keeps it from returning? |

## References

- [Security Intelligence Pipeline](security_intelligence_pipeline.md)
- [Four Discovery Modes](four_discovery_modes.md)
- [Verification Is the Bottleneck](verification_bottleneck.md)
- [Policy-as-Code Served Pre and Post Coding](pre_post_policy_as_code.md)
- [CodeQL documentation](https://codeql.github.com/docs/)
- [GitHub: Multi-repository variant analysis](https://github.blog/security/vulnerability-research/multi-repository-variant-analysis-a-new-way-to-perform-security-research/)
- [Trail of Bits mrva](https://github.com/trailofbits/mrva)

## Takeaways

!!! success "Takeaways"

    - Name the failed assumption before writing the fix.
    - A variant seed should describe structure: source, sink, missing control, preconditions, and false-positive clues.
    - MRVA is search plus evidence, not keyword matching at scale.
    - Source/sink/barrier modeling is the practical heart of semantic variant analysis.
    - Execution models vary; the assurance contract stays the same.
    - Start with the smallest query that rediscovers the seed, then broaden carefully.
    - Cast a wide net, then apply the same verification standard to every candidate.
    - Prefer the fix that removes the unsafe pattern from future code.
    - Fixes decay. Regression checks preserve the lesson.
    - One-off fixes reduce backlog. Campaigns reduce future vulnerability supply.
