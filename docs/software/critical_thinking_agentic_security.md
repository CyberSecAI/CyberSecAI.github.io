# Critical Thinking for Agentic Security

!!! abstract "Overview"

    Agentic security work needs structured skepticism.

    Models are fluent. Security evidence is not. The job is to keep those two facts separate.

    Critical thinking is the discipline that prevents speed from turning into false confidence. It frames the problem, labels evidence, tests objections, and feeds the lesson back into the system.

## Step 1: Frame the Problem

Start by naming the real problem before choosing the tool.

Ask:

- What security property are we testing?
- Who is the attacker?
- What boundary matters?
- What outcome are we trying to prevent?
- What is explicitly out of scope?
- What would count as success?

Bad framing: "Run an AI security scan."

Better framing: "Find whether untrusted content can cause an agent to disclose data or perform an external action without informed user confirmation."

!!! tip "Framing rule"

    The sharper the problem frame, the less likely the agent is to produce impressive but irrelevant work.

## Step 2: Separate Evidence From Assumption

Every claim needs a label.

| Label | Meaning |
|---|---|
| Verified | Directly supported by source, test, trace, or reproducible behavior |
| Inferred | Reasonable conclusion from evidence, but not directly proven |
| User-claimed | Provided by a human, not independently checked |
| Unknown | Decision-relevant and not yet answered |
| Contradicted | Evidence points in different directions |

This prevents the common failure mode where a plausible inference becomes a stated fact two paragraphs later.

## Step 3: Analyze Options

Security decisions are trade-offs.

For each option, compare:

- risk reduction
- implementation cost
- developer friction
- user experience impact
- operational burden
- failure mode
- rollback path

Example:

| Option | Benefit | Risk |
|---|---|---|
| Block the tool entirely | Strong containment | Breaks useful workflows |
| Require confirmation | Preserves utility | Confirmation fatigue |
| Add policy outside the model | Stronger authority boundary | More engineering work |
| Monitor only | Fast deployment | Does not prevent harm |

Never present a security control without its trade-off.

## Step 4: Make the Strongest Objection

Before finalizing, argue against yourself.

Ask:

- Where could this finding be wrong?
- What mitigating control did we not inspect?
- What stakeholder would object?
- Are we ranking by exploitability or by novelty?
- Are we overfitting to one example?
- What evidence would change the recommendation?

This is especially important with agent-generated findings. The model may produce a coherent narrative around a weak path. The critic's job is to break the narrative if the evidence does not hold.

## Step 5: Define the Learning Loop

A good security decision includes a feedback loop.

Define:

- leading indicators
- lagging indicators
- review triggers
- owners
- time horizon
- reversal conditions

For agentic security, useful indicators include false-positive rate, confirmed finding rate, time to verification, time to remediation, proximity distribution, repeated vulnerability classes, regression failures, and the number of findings converted into reusable rules or tests.

!!! info "Compounding loop"

    ```text
    decision -> outcome -> evidence -> rule/test/seed -> next decision
    ```

If there is no feedback loop, the decision will age badly.

## A Lightweight Review Template

Use this for findings, design reviews, and remediation plans.

| Section | Prompt |
|---|---|
| Problem | What security property is at stake? |
| Evidence | What is verified, inferred, user-claimed, contradicted, or unknown? |
| Options | What could we do, and what are the trade-offs? |
| Objections | Why might our conclusion be wrong? |
| Decision | What are we doing now, and why? |
| Feedback | What will tell us to continue, change, or reverse? |

## Apply It to Agentic Findings

Agentic findings need a specific review posture.

The review should not ask whether the report sounds plausible. It should ask what evidence would survive an adversarial reader.

| Agent claim | Critical-thinking check |
|---|---|
| "This input reaches a dangerous sink" | Show the path and identify any barriers. |
| "The model can be manipulated" | Specify the untrusted content, instruction boundary, and tool consequence. |
| "This is high severity" | State impact, preconditions, and proximity. |
| "The fix works" | Replay the old path and verify intended behavior still works. |
| "This class exists elsewhere" | Extract the failed assumption and run variant analysis. |

The discipline is simple: label the claim, test the objection, then decide what evidence is still missing.

## References

- [Principles for Agentic Security Assurance](agentic_security_principles.md)
- [Verification Is the Bottleneck](verification_bottleneck.md)
- [Software Assurance](software_assurance.md)
- [Security Intelligence Pipeline](security_intelligence_pipeline.md)
- [Software Artifacts](software_artifacts.md)

## Takeaways

!!! success "Takeaways"

    - Critical thinking keeps agentic speed attached to reality.
    - Frame the security property before choosing the tool.
    - Label evidence and assumptions explicitly.
    - Compare controls by trade-off, not preference.
    - Put the strongest objection in the review, not the postmortem.
    - Every decision should define how it will learn.
    - For agentic findings, proximity, preconditions, and reproducibility matter more than narrative polish.
