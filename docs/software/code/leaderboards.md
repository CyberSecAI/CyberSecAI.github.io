# AI Coding Leaderboards

!!! abstract "Overview"

    This page is a list of benchmarks for LLMs that are used to help with coding.
    
    It covers both Coding Assistants and Autonomous Coding Agents

## Leaderboards

| Leaderboard                                                          | Category                  | Tasks                                                                                              | Metrics                                                    |
|----------------------------------------------------------------------|---------------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| [Aider LLM Leaderboards](https://aider.chat/docs/leaderboards/)       | Coding Assistant          | 225 Exercism exercises across C++, Go, Java, JavaScript, Python, Rust                              | Two-pass pass rates; cost per run; edit correctness        |
| [EvalPlus Leaderboard](https://evalplus.github.io/leaderboard.html)   | Coding Assistant          | HumanEval+ (164 hand-verified Python); MBPP+ (399 sanitized Python)                                | pass@1 (greedy); extended efficiency via EvalPerf          |
| [TabbyML Coding LLMs Leaderboard](https://leaderboard.tabbyml.com/)  | Coding Assistant          | Amazon CCEval next-line tasks in Python, JS, Go…                                                   | Next-line accuracy (exact-match of very next line)         |
| [MHPP Leaderboard](https://sparksofagi.github.io/MHPP/)               | Coding Assistant          | 210 “Mostly Hard” multi-step Python problems                                                       | pass@1 (greedy); sampling (T=0.7, 100 runs)                |
| [Copilot Arena](https://github.com/lmarena/copilot-arena)             | Coding Assistant          | Paired autocomplete & inline-editing comparisons                                                   | ELO-style rankings from user votes                         |
| [SWE-bench](https://www.swebench.com/)                                | Autonomous Agent          | 2,294 real-world “Fail-to-Pass” GitHub issues from 12 Python repos                                 | % of issues resolved                                       |
| [HAL (Holistic Agent Leaderboard)](https://hal.cs.princeton.edu/)     | Autonomous Agent          | 13 benchmarks (e.g., SWE-bench Verified, USACO, Cybench, TAU-bench) across many domains            | Cost-controlled evaluations; success rates; Pareto fronts  |
| [TBench](https://www.tbench.ai/)                                      | Autonomous Agent          | Terminal-based complex tasks in realistic environments                                             | Task success rate; command accuracy; time-to-completion    |

## Takeaways
  
!!! success "Key Takeaways"

    Leaderboards are a good way to quantitatively and objectively compare solutions.

    Comparison across multiple metrics and leaderboards avoids solutions that overfit to a benchmark.