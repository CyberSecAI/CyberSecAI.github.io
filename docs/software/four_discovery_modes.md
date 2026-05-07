# Four Discovery Modes

!!! abstract "Overview"

    Vulnerability discovery is not one activity.

    Use the R1/R2/R3/R4 frame: exploratory reasoning, context-guided intelligence, invariant verification, and pattern matching. They answer different questions. They also fail differently.

    The mistake is asking one mode to do all jobs. The discipline is measuring what each mode uniquely finds, what it costs, and how much verification it needs.

## The R1-R4 Frame

Use two axes: code-first vs architecture-first, and known-pattern vs novel reasoning.

```text
                Known patterns <--------------------> Novel reasoning

Architecture-     +-------------------+------------------------+
first             | R3: Invariant     | R2: Context-guided     |
                  | verification      | intelligence           |
                  | "Is it safe?"     | "What's unfinished?"   |
                  +-------------------+------------------------+
Code-first        | R4: Pattern       | R1: Exploratory        |
                  | matching          | reasoning              |
                  | "Does it match?" | "What's wrong?"        |
                  +-------------------+------------------------+
```

| Mode | Question | Best output |
|---|---|---|
| R1: Exploratory reasoning | What is wrong here? | Candidate attack paths, missing checks, proof strategy |
| R2: Context-guided intelligence | What is unfinished, risky, or repeated? | Churn hotspots, archaeology seeds, semantic findings, variants |
| R3: Invariant verification | Is the design safe against the stated security properties? | Requirement and architecture violations |
| R4: Pattern matching | Does this match a known risky class? | Breadth findings, posture gaps, policy violations |

!!! observation "The important metric is uniqueness"

    Do not ask which mode "wins." Ask what high-value finding each mode would miss if it were removed. Low overlap can be healthy when the modes are designed to see different surfaces.

## R1: Exploratory Reasoning

R1 is the closest agentic equivalent of a skilled human reviewer walking the code.

It starts code-first. The agent reads entry points, traces trust boundaries, and tries to build a plausible attack. It is strong when the bug is semantic: the code does what it says, but what it says is unsafe.

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
| Source tree, entrypoints, architecture notes, known risky surfaces | Candidate attack paths with source evidence and a proposed proof strategy |

The weakness is coverage. A reasoning pass can be brilliant and still miss the next file. Use R1 to find sharp edges quickly, not to prove the estate is safe.

## R2: Context-Guided Intelligence

R2 is where the intelligence layer has the most leverage.

Give the agent intelligence: churn, history, incomplete fixes, source-to-sink evidence, and confirmed seeds from other systems.

The public evidence points in the same direction. The Source to Sink work argues for structured path evidence over "brick of text" prompting. FENRIR uses a cascade: cheap static filters first, fast model triage second, deep sandbox verification last. Put LLM reasoning where the structured signal is already strong.

R2 has four stages.

| Stage | Capability | Question | Why it matters |
|---|---|---|---|
| A | Code churn hotspot | Where should expensive review start? | High churn near trust boundaries is a routing signal |
| B | Git vulnerability archaeology | What history matters? | Incomplete fixes often leave sibling paths vulnerable |
| C | CodeQL + LLM bridge | Is it semantically real? | Structured dataflow reduces guesswork; context reduces false positives |
| D | Variant analysis | Where else does it exist? | One confirmed issue becomes a class-level search |

!!! observation "Every fix commit is a hypothesis"

    A security fix says, "this class is fixed." Stage B tests that hypothesis. Did the change fix the pattern, or only one instance?

### Stage A: Code Churn Hotspot

Not all files deserve the same attention.

Rank by `churn x security relevance`. A cosmetic rename should not weigh the same as repeated changes to auth logic, parsing, crypto, deserialization, authorization, or outbound actions.

Output: a priority list. Not vulnerabilities. A map of where expensive review is more likely to pay rent.

### Stage B: Vulnerability Archaeology

History doubles as discovery intelligence.

Look for commits that harden validation, patch injection, fix auth, add escaping, or mention security. Then ask whether the same pre-fix pattern still exists in sibling paths.

!!! tip "Archaeology seed"

    A good seed captures the old pattern, the patched pattern, the missing control, the affected framework, and the sibling locations to check.

### Stage C: CodeQL + LLM Bridge

CodeQL gives structure: AST, control flow, data flow, sources, sinks, and path evidence.

Keep CodeQL as the structure. Use LLM/context triage to reason over it:

- Is the path reachable from attacker-controlled input?
- Did the query miss a sanitizer, authorization check, framework escape, or deployment constraint?
- What preconditions are needed?
- What proof would reduce the remaining uncertainty?

This is the bridge: deterministic tooling finds candidate paths; contextual reasoning decides which paths deserve promotion.

This is why the bridge belongs in R2 rather than R4. R4 can match the known pattern. Stage C asks whether the path is live, relevant, and missing a real barrier.

### Stage D: Variant Analysis

A confirmed vulnerability becomes intelligence.

Encode the class as a variant seed, then search for structurally equivalent paths across codebases, frameworks, templates, and generated projects. Look for the same failed assumption, not the same line.

```text
confirmed finding
  -> variant seed
     -> target selection
        -> semantic or structural search
           -> LLM/context triage
              -> proximity scoring
                 -> PoC, fix, or campaign
```

## R3: Invariant Verification

R3 is architecture-first.

It starts from a security property and asks whether the implementation, design, and runtime behavior preserve it. This is where requirements, threat models, ADRs, policy-as-code, and acceptance criteria become active contracts.

Examples of invariants:

- untrusted content must not become instruction
- cross-tenant data must not cross the tenant boundary
- external actions require informed confirmation
- secrets must not be reachable from untrusted execution
- privileged tools must not run from untrusted context
- logging must flow for security-relevant actions

| Input | Output |
|---|---|
| Requirements, threat model, architecture decision, policy rule, runtime trace | Evidence that the invariant holds, fails, or needs a narrower test |

R3 finds compositional failures. The code may look correct in isolation while the system violates the property.

## R4: Pattern Matching and Breadth

R4 is known-pattern breadth.

This is where domain skills, rule packs, Semgrep, CodeQL query suites, dependency scanning, IaC checks, secrets scanning, container checks, logging checks, and cloud posture rules earn their keep.

It also connects back to [Policy-as-Code Served Pre and Post Coding](pre_post_policy_as_code.md): repeated review lessons should become standing rules where the rule is clear enough to enforce.

R4 is less elegant than exploit discovery. It is also how you find the boring risks that become incidents.

| Strength | Weakness |
|---|---|
| Broad coverage of known classes | Can generate high volume and detection-level findings |
| Cheap to repeat once rules exist | Struggles with missing code and design intent |
| Good for compliance and hygiene | Needs verification before promotion |

!!! warning "Do not scale breadth before signal"

    Pattern matching is valuable, but high-volume detection without a verifier creates a queue, not a programme. Establish signal and verification first, then expand breadth.

## Operating Pattern

A practical run preserves the R1-R4 distinction:

1. Use R1 to get fast exploratory signal on a high-risk target.
2. Use R2 to direct attention with churn, history, semantic evidence, and variants.
3. Use R3 to test the actual security invariants.
4. Use R4 to broaden coverage across known classes.
5. Compare unique findings, cost per verified finding, false-positive rate, and campaign yield.

The result should be an evidence-backed portfolio, not a single scanner score.

## References

- [Security Intelligence Pipeline](security_intelligence_pipeline.md)
- [Variant Analysis and Class Eradication](variant_analysis_class_eradication.md)
- [Principles for Agentic Security Assurance](agentic_security_principles.md)
- [Policy-as-Code Served Pre and Post Coding](pre_post_policy_as_code.md)
- [Software Engineering Security](swe_redux_security.md)
- [DARPA AI Cyber Challenge Tools Comparison](aixcc.md)
- [CodeQL documentation](https://codeql.github.com/docs/)
- [GitHub: Multi-repository variant analysis](https://github.blog/security/vulnerability-research/multi-repository-variant-analysis-a-new-way-to-perform-security-research/)
- [Trail of Bits mrva](https://github.com/trailofbits/mrva)
- [Scott Behrens and Justice Cassel: Source to Sink](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/bxwEZMhqeR0_Scott_Behrens_Justice_Cassel_Source_to_Sink_Improving_LLM_Vuln_Discovery.md)
- [Meta FENRIR: AI Hunting for AI Zero-Days at Scale](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/c6_bRzHCf3U_Peter_Girnus_Derek_Chen_FENRIR_AI_Hunting_for_AI_Zero-Days_at_Scale.md)
- [Jenny Guanni Qu: Why Most ML Vulnerability Detection Fails](https://github.com/CyberSecAI/unprompted_2026/blob/master/insights/93jhfuL-ndo_Jenny_Guanni_Qu_Why_Most_ML_Vulnerability_Detection_Fails.md)

## Takeaways

!!! success "Takeaways"

    - Use the R1/R2/R3/R4 frame; do not collapse discovery into one generic scan.
    - R1 finds sharp semantic paths quickly, but it does not prove coverage.
    - R2 is the intelligence engine: churn, archaeology, semantic confirmation, variant propagation.
    - R3 tests whether the system preserves its security invariants.
    - R4 gives breadth across known classes, but it needs verification discipline.
    - Stage B treats every fix commit as a hypothesis; Stage D turns every confirmed finding into a class search.
    - Measure unique findings, false-positive rate, cost per verified finding, and campaign yield.
