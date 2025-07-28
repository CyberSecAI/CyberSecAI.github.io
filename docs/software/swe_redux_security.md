---
icon: material/play-box-edit-outline 
---

# Software Engineering 1.0 Redux Security


!!! overview

    This section covers the Core Review Security touchpoint.

    It adds support for this to the BMAD Method by creating a VulnerabilityTech Agent.




!!! quote "Vulnerability Assessment Analyst Tanya"

    "Use for performing security scans, identifying and documenting software vulnerabilities, analyzing code for weaknesses, validating patches, assessing system configurations, verifying compliance with security standards, and generating vulnerability reports for audit or remediation purposes."

    The [original brief](https://discord.com/channels/1377115244018532404/1394851634428903615/1396926639119794497) from a user AVSuun


## Tools and Claude Code Sub-agents

I wanted to give the VulnerabilityTech agent access to tools for 

- Static Analysis Security Testing (SAST) - combining traditional SAST tools with LLM review 
- Dependency checking


I decided to use Claude Code Sub-agents for this (announced a few days ago https://docs.anthropic.com/en/docs/claude-code/sub-agents). 

- I only focused on Claude Code - not other environments that BMAD may work on.


### BMAD Agents vs Claude Code Sub-Agents 

#### Claude Code Sub-Agents 
- **What They Are**: Specialized AI assistants with custom system prompts and tool access
- **Architecture**: Defined as Markdown files with YAML frontmatter in `.claude/agents/`
- **Operation**: Isolated context windows with specific expertise and granular tool permissions
- **Delegation**: Automatic selection by Claude Code or explicit user invocation
- **Benefits**: Focused expertise, faster analysis, parallel processing capabilities

#### BMad Framework Current State
- **12 Specialized Agents**: Comprehensive personas in `bmad-core/agents/`
- **Complex Configuration**: YAML-based with dependencies and external task references
- **Full Context Maintenance**: Complete operating instructions and workflow definitions
- **Command Syntax**: `*command` activation with extensive persona definitions

#### Key Architectural Differences
1. **Complexity**: BMad = comprehensive personas vs Claude = focused sub-agents
2. **Dependencies**: BMad = external task references vs Claude = self-contained
3. **Context**: BMad = full context maintenance vs Claude = isolated context windows
4. **Activation**: BMad = explicit commands vs Claude = automatic delegation


### Claude Code sub-agents Setup

See [how I setup Claude Code sub-agents](https://github.com/CyberSecAI/BMAD-METHOD/blob/feature/claude-code-sub-agents-integration/.claude/README.md) to work with BMAD agents that describes how BMAD agents call Claude Code sub-agents.

Four [Claude Code sub-agents](https://github.com/CyberSecAI/BMAD-METHOD/tree/feature/claude-code-sub-agents-integration/.claude/agents) were added:

| **Claude sub-agent** | **Purpose**                                                                                                 
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **dependency-scanner**   | I am a specialized security analyst focused on third-party component security assessment and supply chain risk analysis. My expertise covers dependency vulnerability scanning, license compliance, and supply chain security validation according to NIST SSDF practices.                                                              |
| **pattern-analyzer**     | I am a specialized security pattern analyst focused on detecting secure and insecure coding patterns across multiple programming languages. My expertise leverages language-specific security knowledge from expansion packs to validate secure coding practices and identify anti-patterns that introduce vulnerabilities.             |
| **security-reviewer**    | I am a Level 2 orchestrator sub-agent that coordinates comprehensive security analysis by leveraging specialized tool sub-agents. My role is to orchestrate hybrid SAST + LLM security analysis for maximum accuracy and coverage, focusing on practical, exploitable security issues that pose real risks to applications and systems. |
| **test-validator**       | I am a specialized security testing analyst focused on validating the quality, coverage, and effectiveness of security tests within software projects. My expertise ensures that security testing meets NIST SSDF standards and provides robust protection against real-world threats.                                                  |



I also added a tests dir to BMAD be able to test this. 

- This includes a [deliberately vulnerable app](https://github.com/CyberSecAI/BMAD-METHOD/tree/feature/claude-code-sub-agents-integration/tests/agents/vulnerabilityTech/fixtures/python/vulnerable_app) to test: 



### VulnerabilityTech Agent Report

!!! success
 
    See example [output report](https://github.com/CyberSecAI/BMAD-METHOD/blob/feature/claude-code-sub-agents-integration/tests/reports/consolidated-security-report.md).

    https://github.com/CyberSecAI/BMAD-METHOD/blob/feature/claude-code-sub-agents-integration/tests/reports/consolidated-security-report.md#%EF%B8%8F-nist-ssdf-compliance-assessment


## Finding Defects

<figure markdown>
![](../assets/images/sast_quad.png)
Image from [Secure Programming with Static Analysis by Brian Chess, Jacob West](https://www.amazon.com/Secure-Programming-Static-Analysis-Brian/dp/0321424778)

The best way to find a particular defect depends on whether it is generic or context specific, and whether 
it is visible in the code or only in the design.
</figure>




## How to use LLMs and SAST Tools Together

**LLMs can compliment the Static analysis sweetspot (Generic defects - Visible in the code)**

- "SAST tools often rely on predefined patterns and rules, which can result in high false-positive rates and an inability to detect novel or context-dependent vulnerabilities" per [ref](https://arxiv.org/html/2409.15735v2).
- Additional context can be given to LLMs to improve their performance e.g. vulnerability reports on similar code
 [LSAST: Enhancing Cybersecurity through LLM-supported Static Application Security Testing](https://arxiv.org/html/2409.15735v2)


!!! quote

    While traditional tools like Bandit are valuable, our results show that LLMs provide a complementary advantage by analyzing fragmented and non-compilable code and detecting complex vulnerability patterns that existing tools may miss. Additionally, the ability of LLMs to generate security tests adds a useful layer of verification, potentially enhancing the accuracy of vulnerability assessments.

    [Leveraging Large Language Models for Command Injection Vulnerability Analysis in Python: An Empirical Study on Popular Open-Source Projects](https://arxiv.org/html/2505.15088v1)



!!! quote

    Our findings indicate that SAST tools exhibit low vulnerability detection ratios while maintaining a low marked function ratio, akin to a low false positive rate. In contrast, LLMs demonstrate high vulnerability detection ratios but are accompanied by elevated marked function ratios (akin to high false positive rates). Through ensemble approaches, we demonstrate that combining SAST tools and LLMs mitigates their respective limitations, resulting in improved overall vulnerability detection performance.

    [Comparison of Static Application Security Testing Tools and Large Language Models for Repo-level Vulnerability Detection](https://arxiv.org/abs/2407.16235)  


!!! quote

    Analysis reveals that the optimal approaches differ across programming languages.
    The best choice will depend on the user’s acceptance of the trade-off between detection ratios and marked function ratios.
    
    [Comparison of Static Application Security Testing Tools and Large Language Models for Repo-level Vulnerability Detection](https://arxiv.org/html/2407.16235v1) 

!!! quote

    The reasoning-oriented models consistently produced fewer false positives, suggesting that their internal steps for “validating” potential vulnerabilities lead to more precise outcomes.
    
    [CASTLE: Benchmarking Dataset for Static Code Analyzers and LLMs towards CWE Detection](https://arxiv.org/html/2503.09433v1)




## References

1. [Secure Programming with Static Analysis by Brian Chess, Jacob West](https://www.amazon.com/Secure-Programming-Static-Analysis-Brian/dp/0321424778)
2. [Software Security: Building Security In, by Gary McGraw](https://www.amazon.com/Software-Security-Building-Gary-McGraw/dp/0321356705)
3. [Towards Effective Complementary Security Analysis using Large Language Models](https://arxiv.org/html/2506.16899v1)
4. [Leveraging Large Language Models for Command Injection Vulnerability Analysis in Python: An Empirical Study on Popular Open-Source Projects](https://arxiv.org/html/2505.15088v1)
1. [LLM vs. SAST: A Technical Analysis on Detecting Coding Bugs of GPT4-Advanced Data Analysis](https://arxiv.org/html/2506.15212v1)
2. [Comparison of Static Application Security Testing Tools and Large Language Models for Repo-level Vulnerability Detection](https://arxiv.org/abs/2407.16235) 
3. [LSAST: Enhancing Cybersecurity through LLM-supported Static Application Security Testing](https://arxiv.org/html/2409.15735v2)
4. [CASTLE: Benchmarking Dataset for Static Code Analyzers and LLMs towards CWE Detection](https://arxiv.org/html/2503.09433v1)

