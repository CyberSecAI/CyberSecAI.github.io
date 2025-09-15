# Overview

!!! abstract 

    This section looks at Context Engineering, and gives Prioritized Context Engineering Steps for Agentic AI.

    !!! quote
        
        "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." Andrej Karpathy,
        https://www.youtube.com/watch?v=LCEmiRjPEtQ

  

## Essential Knowledge


!!! tip "The best references covering the Problem and Solutio space" 

    - Reunig, D. (2025, June 22). [*How long contexts fail (and how to fix them).*](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html)  
      Analyzes failure modes of excessively long context windows.  
        **Failure modes:**  
        - **Context poisoning**: When a hallucination makes it into the context  
        - **Context distraction**: When the context overwhelms the training  
        - **Context confusion**: When superfluous context influences the response  
        - **Context clash**: When parts of the context disagree  

    - Reunig, D. (2025, June 26). [*How to fix your context.*](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html)  
      Follow-up article offering tactics to avoid context failure: RAG, tool loadout, context pruning, summarization, and offloading.

    - Martin, R. L. (2025, June 23). [*Context engineering.*](https://rlancemartin.github.io/2025/06/23/context_engineering/)  
      Overview of practical strategies for structuring and optimizing context for LLMs.  
      **Key practices: write, select, compress, isolate**

    - IndyDevDan. (2025, July). [*Elite context engineering with Claude Code*](https://www.youtube.com/watch?v=Kf5-HWJPTIE)  
      Demonstrates advanced context engineering techniques using Claude Code.
      **Core mantra:** **R&D = Reduce + Delegate.**  
      Reduce what the primary agent sees; delegate everything else to sub-agents or background primaries, with crisp contracts and logs  


    
## Prioritized Context Engineering Steps for Agentic AI

### 1) Minimize the Primary Context (treat it like a cache)

* Keep only: **goal**, **immediate instructions**, **tiny retrieved slice**, **output schema**.
* Keep ephemeral scratchpads for step-by-step reasoning; purge after use.
* Offload history, rules, and big docs to external memory or files.
*  🔑 **Impact:** Faster, cheaper, less distracted agent; fewer long-context failure modes.

---

### 2) Write Context Intentionally (don’t just append everything)

* Clear **system message** for goals, rules, constraints, evaluation criteria.
* Define **output schemas** (JSON/table) and acceptance checks.
* Put canonical facts/API contracts in stable references, not the live window.
* Log key decisions so context can be rebuilt if needed.
*  🔑 **Impact:** Prevents bloated prompts; establishes reliable “ground truth”.

---

### 3) Select Context Dynamically (quality > quantity)

* Retrieve only what’s relevant **now** via embeddings/filters.
* Cap retrieval: few high-signal snippets; drop duplicates/stale text.
* Prefer structured facts (tables/JSON) over long prose.
*  🔑 **Impact:** Model focuses on the right information; fewer hallucinations.

---

### 4) Use Context Priming (instead of big always-on memory files)

* Create reusable **prime commands** per task (Purpose → Read/Fetch → Steps → Report).
* Keep a **tiny universal core** (guardrails + IO schema) always loaded.
* Prime on demand for bugfix, feature, research, etc.
*  🔑 **Impact:** Minimal startup tokens with task-specific readiness.

---

### 5) Kill Always-On Baggage (tools/MCP autoloading)

* Don’t preload tool packs/MCP servers by default; load **lazily** per task.
* Unload after use; explicitly justify any autoload.
* Audit startup context and remove dead weight.
*  🔑 **Impact:** Frees large chunks of window; cuts token waste and latency.

---

### 6) Delegate Heavy Work to **Sub-Agents** (properly)

* One sub-agent = **one job** with a tight **system prompt**.
* Let sub-agents consume **their** windows; return **distilled reports** + artifacts.
* Standard report contract: `{summary, key_facts, risks, artifacts[]}`.
*  🔑 **Impact:** Keeps the primary window small while scaling capability.

---

### 7) Delegate Long/Expensive Tasks to **Background Primary Agents**

* Kick off separate agents for crawls, planning, batch edits, evals.
* They write **report files + artifacts**; foreground ingests concise summaries.
* Use this to “get out of the loop” while work continues.
*  🔑 **Impact:** Parallelizes work; maintains a lean, responsive main loop.

!!! tip

    [Claude Code CLI God Mode](../software/claude_code.md#claude-code-cli-god-mode) is an example of this, delegating to a different Primary model (that is the best tool for the job.)


---

### 8) Compress Context (mostly outside the window)

* Rolling conversation summaries; hierarchical notes (facts → decisions → actions).
* Store raw data externally; insert only **pointers + summaries**.
* Heuristic trimming rules (dedupe, last-N, relevance thresholds).
*  🔑 **Impact:** Extends effective history without clogging the window.

---

### 9) Isolate Contexts (sandboxing & pipelines)

* Keep runtime state objects and scratchpads **per agent**.
* Avoid leaking sub-agent history into the primary prompt.
* Build multi-agent pipelines with explicit handoffs.
*  🔑 **Impact:** Reduces poisoning, distraction, and cross-task conflicts.

---

### 10) Log **Context Bundles** for replay/handoff

* Save `{run_id, primes, reads, tool_calls, key_findings, decisions, outputs, next_steps}`.
* Use bundles to reprime new agents after window blow-ups or for continuity.
* Keep bundles concise—no verbatim dumps of huge content.
*  🔑 **Impact:** Reproducibility and seamless continuation across sessions.

---

### 11) Defend Against Context Failure Modes

* **Poisoning:** verify tool outputs; tag trust levels; gate propagation.
* **Confusion:** filter irrelevant turns; dedupe aggressively.
* **Conflict:** detect/resolve contradictions before composing answers.
*  🔑 **Impact:** Higher reliability and fewer cascading errors.

---

### 12) Standardize Schemas & Measure What Matters

* Standard prompt skeletons, report JSON, artifact layout, retrieval policies.
* Track `startup_tokens`, `peak_tokens`, `#agents_spawned`, `attempts_to_success`, `retrieval_hits`.
* Set SLOs (e.g., startup ≤10% window, attempts ≤3) and alert on drift.
*  🔑 **Impact:** Consistency at scale; makes optimization and debugging straightforward.

---



## Context Engineering 101 cheat sheet

<figure markdown>
![](../assets/images/context_cheatsheet.jpeg)

Context Engineering 101 cheat sheet by Lena Hall https://x.com/lenadroid/status/1943685060785524824
</figure>




## References

### Academic Papers

1. Zhang, W., Gupta, R., Müller, F., et al. (2025, July). *A Survey of Context Engineering for Large Language Models*. *arXiv preprint*.

      * **Comprehensive academic survey reviewing context engineering techniques, challenges, and future research directions.**
     [https://arxiv.org/pdf/2507.13334](https://arxiv.org/pdf/2507.13334)

2. Haseeb, M., et al. (2025, August). *Context Engineering for Multi-Agent LLM Code Assistants Using Elicit, NotebookLM, ChatGPT, and Claude Code*. *arXiv preprint*.

      * **Proposes a multi-agent workflow combining intent translation, semantic retrieval, document synthesis, and Claude Code to improve code generation and validation in large codebases.**
     [https://arxiv.org/html/2508.08322v1](https://arxiv.org/html/2508.08322v1)

---

### Blogs & Articles

3. Martin, R. L. (2025, June). *Context Engineering*.

      * **Blog post introducing principles of context engineering for AI systems, including prompt design, retrieval, and orchestration strategies.**
     [https://rlancemartin.github.io/2025/06/23/context\_engineering/](https://rlancemartin.github.io/2025/06/23/context_engineering/)

4. Schmid, P. (2025, June). *Context Engineering: Optimizing Prompts and Retrieval for LLMs*.

      * **Detailed exploration of context engineering patterns and their practical application in LLM development.**
     [https://www.philschmid.de/context-engineering](https://www.philschmid.de/context-engineering)

5. LlamaIndex (2025, June). *Context Engineering – What it is, and techniques to consider*.

      * **Official blog post from LlamaIndex outlining core techniques in context engineering for enterprise AI assistants.**
     [https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider](https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider)

6. Datacamp (2025, June). *Context Engineering: The Next Frontier of AI Development*.

      * **Educational article explaining how context engineering enhances AI reliability, accuracy, and enterprise integration.**
     [https://www.datacamp.com/blog/context-engineering](https://www.datacamp.com/blog/context-engineering)

7. Landgraf, T. (2025, August). *Context Engineering for Claude Code: Mastering Deep Technical Knowledge*.

      * **Medium article introducing advanced context engineering workflows for Claude Code, including knowledge-file creation, project architecture awareness, and technical validation.**
     [https://medium.com/%40tl\_99311/context-engineering-for-claude-code-mastering-deep-technical-knowledge-bae14f158289](https://medium.com/%40tl_99311/context-engineering-for-claude-code-mastering-deep-technical-knowledge-bae14f158289)

---

### Open Source Repositories & Tools

8. Kimai, D. (2025, July). *Context-Engineering (GitHub Repository)*.

      * **Open-source repository providing frameworks and examples for implementing context engineering strategies in real-world projects.**
     [https://github.com/davidkimai/Context-Engineering](https://github.com/davidkimai/Context-Engineering)

9. *Context Engineering Template* (2025, August). *Context-Engineering-Intro (GitHub Repository)*.

      * **Template repository by coleam00 for setting up Claude Code-based context engineering projects, including examples, global rules, and workflows.**
     [https://github.com/coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro)

---

### Media & Visualizations

10. Youtube (2025, September). *Elite Context Engineering with Claude Code* — IndyDevDan \[Video].

    * **Advanced context engineering techniques using Claude Code, as presented by IndyDevDan.**
      [https://www.youtube.com/watch?v=Kf5-HWJPTIE](https://www.youtube.com/watch?v=Kf5-HWJPTIE) (\[YouTube]\[1])

11. Youtube (2025, September). *Context Engineering for Agents — Lance Martin, LangChain* \[Video].

    * **Discussion on context engineering specifically for agent frameworks, by Lance Martin from LangChain.**
      [https://www.youtube.com/watch?v=\_IlTcWciEC4](https://www.youtube.com/watch?v=_IlTcWciEC4) (\[YouTube]\[2])

12. Droid, L. (2025, July). *Context Engineering Visualization*.

    * **Illustrative summary of context engineering techniques, shared via social media.**
      [https://x.com/lenadroid/status/1943685060785524824/photo/1](https://x.com/lenadroid/status/1943685060785524824/photo/1)

13. Youtube (2025, September). *Advanced Context Engineering for Agents — Dexter Horthy* \[Video].

    * **Walks through why naive back-and-forth prompting fails, how spec-first development keeps teams aligned, and why “everything is context engineering.” From compaction strategies to subagents and planning workflows, he shows how intentional context management turns AI coding from prototypes into production.**
      [https://www.youtube.com/watch?v=IS\_y40zY-hc](https://www.youtube.com/watch?v=IS_y40zY-hc) (\[YouTube]\[3])

---




## Takeaways
  
!!! success "Key Takeaways"

    * **Treat the Context Window Like a CPU Cache, Not a Hard Drive:** The core principle is to keep the primary agent's context minimal and focused—containing only the immediate goal, instructions, and a small slice of relevant data. Offload history, large documents, and non-essential tools to external memory to improve speed, reduce cost, and avoid distraction.
    * **Reduce and Delegate, Don't Accumulate:** Instead of bloating a single agent's context, delegate heavy or specialized tasks to sub-agents or background agents. These agents work in their own isolated contexts and return only concise, distilled reports, enabling complex work without overwhelming the primary agent.
    * **Context Must Be Actively Managed, Not Passively Appended:** Implement dynamic strategies like just-in-time retrieval (RAG), summarization, and context isolation to ensure the model always has high-quality, relevant information. Actively defend against common failure modes like poisoning and confusion by verifying inputs and filtering irrelevant data.