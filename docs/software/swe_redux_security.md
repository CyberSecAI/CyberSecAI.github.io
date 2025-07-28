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


### Claude Code sub-agents

See [how I setup Claude Code sub-agents](https://github.com/CyberSecAI/BMAD-METHOD/blob/feature/claude-code-sub-agents-integration/.claude/README.md) to work with BMAD agents that describes how BMAD agents call Claude Code sub-agents.

4 [Claude Code sub-agents](https://github.com/CyberSecAI/BMAD-METHOD/tree/feature/claude-code-sub-agents-integration/.claude/agents) were added:
| **Claude sub-agent** | **Purpose**                                                                                                                                                                                                                                                                                                                             |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dependency-scanner   | I am a specialized security analyst focused on third-party component security assessment and supply chain risk analysis. My expertise covers dependency vulnerability scanning, license compliance, and supply chain security validation according to NIST SSDF practices.                                                              |
| pattern-analyzer     | I am a specialized security pattern analyst focused on detecting secure and insecure coding patterns across multiple programming languages. My expertise leverages language-specific security knowledge from expansion packs to validate secure coding practices and identify anti-patterns that introduce vulnerabilities.             |
| security-reviewer    | I am a Level 2 orchestrator sub-agent that coordinates comprehensive security analysis by leveraging specialized tool sub-agents. My role is to orchestrate hybrid SAST + LLM security analysis for maximum accuracy and coverage, focusing on practical, exploitable security issues that pose real risks to applications and systems. |
| test-validator       | I am a specialized security testing analyst focused on validating the quality, coverage, and effectiveness of security tests within software projects. My expertise ensures that security testing meets NIST SSDF standards and provides robust protection against real-world threats.                                                  |



I also added a tests dir to BMAD be able to test this. 

- This includes a [deliberately vulnerable app](https://github.com/CyberSecAI/BMAD-METHOD/tree/feature/claude-code-sub-agents-integration/tests/agents/vulnerabilityTech/fixtures/python/vulnerable_app) to test: 



## VulnerabilityTech Agent Report

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




llm paper sast vs llm

paper guidance






## References

1. [Secure Programming with Static Analysis by Brian Chess, Jacob West](https://www.amazon.com/Secure-Programming-Static-Analysis-Brian/dp/0321424778)
2. [Software Security: Building Security In, by Gary McGraw](https://www.amazon.com/Software-Security-Building-Gary-McGraw/dp/0321356705)