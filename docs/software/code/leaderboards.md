# AI Coding Leaderboards

!!! abstract "Overview"

    This page is a list of benchmarks for LLMs that are used to help with coding.
    
    It covers both Coding Assistants and Autonomous Coding Agents

## Leaderboards

### Coding Assistant: [Aider LLM Leaderboards](https://aider.chat/docs/leaderboards/)

* **Polyglot Coding Benchmark**

  * **Tasks:** 225 Exercism exercises across C++, Go, Java, JavaScript, Python, and Rust
  * **Metrics:** Two-pass pass rates, cost per run, edit format correctness
  * **Example Top Result:** o3 (high) + gpt-4.1 achieves 82.7% correct at a total cost of \$69.29 ([aider.chat][1])


### Autonomous Coding Agents

* **[SWE-bench](https://www.swebench.com/original.html)**

  * **Tasks:** 2,294 real-world “Fail-to-Pass” GitHub issues from 12 popular Python repositories
  * **Metric:** Percentage of issues successfully resolved by an AI agent (e.g., SWE-agent 1.0 (Claude 3.7 Sonnet): 33.83%) ([SWEbench][2])

* **HAL: [Holistic Agent Leaderboard](https://hal.cs.princeton.edu/)**

  * **Coverage:** 13 benchmarks (including SWE-bench Verified, USACO, Cybench, TAU-bench) and 122 agents
  * **Features:** Cost-controlled, standardized, third-party evaluations; detailed failure analysis via the HAL harness; cost-performance Pareto frontiers ([hal.cs.princeton.edu][3])
