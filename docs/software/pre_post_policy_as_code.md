# Policy-as-Code Served Pre and Post Coding

!!! abstract "Overview"

    This chapter explains how to turn large, static security documents into *working* policy-as-code that GenAI Security Agents can apply during design, coding, and review.
    Instead of asking engineers to memorize external and internal standards and guidance, we:


    - Break large documents into small, testable **rule cards**  
    - Compile those rule cards into reusable **knowledge packs**  
    - Expose the packs through **security agents** and **interactive skills**  
    - Wire them into **software engineering workflows** so guidance appears at the right time and place  

    The end goal is simple: security guidance codes as close as possible to the code to be served automatically at the time of coding as pre-coding guidance, and post-coding checks.



---

## Goals


<figure markdown>
![](../assets/images/continuous_sw_ass.png)
</figure>

The Policy-as-Code engine for GenAI Security Agents is designed to:

* **Operationalise standards**
  Turn external frameworks and internal policies into concrete, testable rules.

* **Embed security into workflows**
  Make security checks first-class citizens in planning, design, coding, and review.

* **Support both pre-code and post-code use**
  Give guidance before the first line of code, and validation once code exists.

* **Provide traceability**
  Make it clear which requirement, from which document, led to each recommendation.

* **Enable incremental adoption**
  Start with pre-built knowledge packs, then extend with your own documentation over time.

---

## Core Concept: From Documents to Rule Cards

The core idea is simple:

> Take large security documents and convert them into small, testable **rule cards** that can be applied by (Claude Code CLI) agents and skills.

### Source Documents

<figure markdown>
![](../assets/images/gen_ai_guidance.png)
</figure>

Typical sources include:

* OWASP and ASVS guidance as used in this example
* Internal security policies and standards
* Regulator rules and industry frameworks
* Architecture decision records and security guidelines

These are treated as **source of truth**, not something the LLM invents.

### Atomic Rule Cards

From those documents we create **atomic rule cards**:

* Each card represents a **single, precise requirement**
  (“API must use OAuth2 with short-lived access tokens”, not “use strong auth”)

* Each card has:

    * A clear **condition** (when it applies)
    * A **requirement** (what must be true)
    * **Rationale / references** (why it matters, where it came from)
    * **Example checks** or questions the agent should ask

!!! tip

    Think of rule cards as “linters for architecture and security design” - small, focused rules that are easy to test and revise.

### Compiled Knowledge Packs

Rule cards are grouped and compiled into **knowledge packs**:

* Packs align with **domains** (authentication, secrets, logging, etc.)
* Each pack can be:

    * Loaded by a **specialist security agent**
    * Queried via **interactive skills** or **semantic search** or **grep**
    * Used in combinations for broader reviews

This compilation step normalises the content into a **machine-friendly format** that agents can load efficiently.

### Agents and Skills

<figure markdown>
![](../assets/images/doc_agents.png)
</figure>

The `.claude/` folder in a project then becomes the delivery vehicle:

* **Security agents**
  Deep specialists for cross-cutting reviews (e.g. “comprehensive security review”, “authentication specialist”).

* **Interactive skills**
  Narrow, predictable commands for developers (e.g. `/authentication-security`, `/secrets-check`, `/logging-review`).

!!! note

    The same underlying rule cards and packs power all of these entry points - you don’t have to duplicate logic across agents and skills.

---

## Access Patterns: Five Ways LLMs Use Security Knowledge

The Policy-as-Code engine exposes **five complementary access patterns**. Each pattern balances:

* How predictable the invocation is
* How much context it needs
* How “deep” the analysis should be

### Summary of Patterns

| Pattern             | How it’s triggered                             | Typical use case                           |
| ------------------- | ---------------------------------------------- | ------------------------------------------ |
| **Skills**          | Deterministic (slash command) or probabilistic | Developer-facing guidance, pre-code checks |
| **Agents**          | Explicit task / tool call                      | Deep, multi-document security analysis     |
| **Semantic Search** | Explicit tool                                  | “What does our standard say about X?”      |
| **Grep**            | Explicit tool                                  | Direct text matches in rules / corpus      |
| **CLAUDE.md flows** | Pattern-based, automatic                       | Enforcing workflow-level security gates    |

### When to Use Which Pattern

* **Skills**
  Use when you want *predictable*, scoped behaviours:

  * A developer calls `/secrets-security` while working on config.
  * An architect asks `/api-authentication-review` on an ADR.

* **Agents**
  Use when you need **broad, cross-cutting security analysis**:

  * “Review this PR against our security standards.”
  * “Assess this architecture document for threats and missing controls.”

* **Semantic Search**
  Use when the question is primarily **research**:

  * “What are our password policies?”
  * “How do we handle multi-tenant isolation?”

* **Grep**
  Use when you need **exact phrase matching**:

  * “Show all rules that mention ‘JWT’.”
  * “Find references to `SAMESITE` cookies.”

* **CLAUDE.md**
  Use to **orchestrate when security runs at all**:

  * Automatically invoke a security agent when certain file types or keywords appear.
  * Ensure security checks become part of the default coding workflow, not an afterthought.


---

## Layered Architecture

The Policy-as-Code engine follows a simple layered architecture:

1. **Source Documents**

      * Raw security content: standards, policies, guidelines.
  
2. **Atomic Rule Cards**

      * Normalised, testable rules with conditions and references.
  
3. **Compiled Rule Sets (Knowledge Packs)**

      * Grouped JSON bundles for efficient loading.
      
4. **Agents & Skills**

      * Human-facing entry points defined in `.claude/`.

This separation is important:

* Security experts can **iterate on rule cards** without touching agent wiring.
* Developers only see the **agents and skills**, not the internal representation.
* You can run **validation** on rule cards and packs independently from model behaviour.

!!! note

    This layout is intentionally compatible with both current Claude Code workflows and other agent frameworks. The rule packs are just data - any agent that can load them can use them.

---

## Two Modes of Adoption

The repository supports two complementary adoption paths.

### 1. Use Pre-Built Security Knowledge

For teams who want **fast value with minimal setup**:

* Copy the provided `.claude/` folder into your project.
* You immediately get:

    * A curated set of **security skills**
    * A suite of **security agents**
    * Pre-populated rule packs aligned to common standards (e.g. OWASP / ASVS families)

Typical uses:

* **Pre-code**
  Use skills while drafting designs, ADRs, and user stories to catch issues early.

* **Post-code**
  Use agents to review pull requests, configuration files, Dockerfiles, etc.


### 2. Build Your Own Knowledge Packs

For organisations with **strong internal standards** or regulatory needs:

* Modify the provided tooling to:

    * Ingest your internal security policies and standards
    * Shard them into rule cards
    * Compile them into custom knowledge packs
    * Wire those packs into new or existing agents and skills

* Requirements (high level):

  * A Python environment
  * The ability to run the build scripts locally or in CI

!!! tip

    Start by extending the existing packs - add a **small number of internal rules** for your most critical risks (e.g. data residency, customer data handling) before attempting a full policy migration.

---

## How It Fits the Software Engineering 1.0 Redux Flow

This engine is designed to plug into the phases already described in the Software Engineering 1.0 Redux sections.

### Pre-Code: Planning and Security Review

* **Planning**

  * Use skills to ensure PRDs and architecture docs include required security content.
  * Architect and Security roles can call targeted skills for authentication, secrets, logging, and data protection.

* **Security Review**

  * Run a comprehensive security agent over:

    * Product brief
    * Architecture document
    * Security stories
  * Generate:

    * Security assessment
    * Threat model
    * Security test cases
    * Security stories to feed into the backlog

### Core Development: Implementation and Code Review

* **During implementation**

  * Developers call skills in-context in their IDE:

    * “Is this JWT handling secure?”
    * “Check this API route for common auth issues.”
  * Agents can be invoked periodically for deeper checks on key modules.

* **Code review**

  * Use a security agent as a specialised reviewer:

    * Run over diffs, not just whole files.
    * Map findings back to the rule cards that were violated.
    * Output concrete, testable recommendations (often directly convertible into security stories and test cases).

!!! note
This keeps the **security source of truth** in one place (rule cards and packs), while letting different roles access it in ways that match their workflows.

---

## Security and Validation Considerations

Even a security agent needs security.

The supporting documentation (security guide, threat model, validation summaries) is used to:

* Identify **threats to the agent itself**:

  * Prompt injection attempts
  * Malicious or poisoned documentation
  * Over-trusting unvalidated scanner output

* Define **mitigations**:

  * Constraining what files / paths agents see
  * Separating “read-only” versus “execution” capabilities
  * Explicitly checking for conflicting or ambiguous rules

* Provide **validation phases**:

  * Early phase: sanity-check that rule cards and packs are being applied consistently.
  * Later phases: assess real-world performance on:

    * Deliberately vulnerable applications
    * Synthetic but realistic security scenarios

!!! tip
Treat the Policy-as-Code engine like any other security-critical component:
- It should have a threat model.
- It should have test cases.
- It should be periodically re-validated as standards and models evolve.

---

## Personas and How They Use It

The same knowledge packs are surfaced differently for different roles:

* **Architect**

  * Uses skills to check architecture documents against security requirements.
  * Invokes a security agent for full design reviews.

* **Product Owner / PM**

  * Ensures security requirements are explicitly captured in PRDs and stories.
  * Uses outputs (security stories, test cases) to plan and track work.

* **Security Engineer / Analyst**

  * Curates rule cards and packs.
  * Owns the security validation of the agents.
  * Reviews high-risk findings and refines the rules.

* **Developer**

  * Uses skills inline in the IDE for quick checks.
  * Treats the security agent as a specialised reviewer alongside human reviewers.

!!! note
This aligns with the broader guide’s stance: **LLMs augment, not replace, the existing roles**. The Policy-as-Code engine simply gives each role a more usable interface to the organisation’s security brain.

---

## Example Workflow: From Policy to Actionable Checks

A concrete end-to-end flow might look like this:

1. **Ingest standards**

   * Security team selects a subset of OWASP / ASVS and internal standards as initial scope.

2. **Create rule cards**

   * Rule cards are authored and reviewed for clarity, conditions, and references.

3. **Build knowledge packs**

   * Packs are compiled by domain (auth, secrets, etc.) and validated.

4. **Wire into agents and skills**

   * Security agents load the full set of relevant packs.
   * Skills are exposed for common queries (“check my auth”, “review my logging”).

5. **Connect to engineering workflows**

   * `.claude/` is added to the repo.
   * CLAUDE.md is updated so that:

     * Certain files trigger automatic security checks.
     * Developers have easy access to security skills.

6. **Iterate based on findings**

   * False positives and gaps feed back into rule card revisions.
   * New standards or guidance become new or updated cards.

!!! success "Success"
Once this loop is running, your security standards stop being static PDFs and become a **living, executable policy-as-code system** that evolves along with your software.

---

## Takeaways

!!! success "Takeaways"
- Large, static security documents are converted into **atomic rule cards** and **knowledge packs**.
- The same packs power **skills**, **agents**, search, and workflow automation via `CLAUDE.md`.
- Teams can start quickly with **pre-built security content** and then extend with internal policies.
- The engine fits naturally into the **Software Engineering 1.0 Redux** lifecycle: planning, design, implementation, and review.
- Security becomes **embedded and executable**, not a separate after-the-fact checklist.

---

## 🔗 References

2. [Claude Skills Deep Dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/)
3. [Claude Code Internals Analysis](https://agiflow.io/blog/claude-code-internals-reverse-engineering-prompt-augmentation/)
4. [Agent Skills for the Real World](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
5. [Technical Deep Dive](https://medium.com/data-science-collective/claude-skills-a-technical-deep-dive-into-context-injection-architecture-ee6bf30cf514)
