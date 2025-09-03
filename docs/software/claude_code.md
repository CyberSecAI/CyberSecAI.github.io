# Overview

!!! abstract 

    This section looks at some Claude Code setups I use.

    I'll add more over time when I'm done playing with them...

## Claude Code CLI God Mode

I use Claude Code CLI as my main tool. 

I wanted a way to use other models via Claude Code to 

- reduce Claude Code token usage / cost (currently on Pro plan)
- use the [best tool for the job](../introduction/models.md) but maintain context in Claude Code

    - Gemini is good for large code bases or data given its large context window
    - ChatGPT is good for debugging 

There are different ways to achieve this:

- using proxy routers per https://youtu.be/EkNfythQNRg
- using Claude Code as the router via a [Claude Code command](https://github.com/alexsmedile/god-cli/blob/main/god-cli.md)

Having played with the former, I settled on the latter as it worked better 



!!!quote "Highlights from the Reddit Community"

    “Gemini CLI feels like garbage… but it has that huge context window we all love. So I added instructions to CLAUDE.md to have Claude use [Gemini CLI in non‑interactive mode] when it needs to gather information about a large part of the codebase.” 

    “Gemini is good at explaining single, independent things … Claude is good at doing complex tasks that require a lot of memory, deep thinking, reasoning.” 

    https://www.reddit.com/r/ChatGPTCoding/comments/1lm3fxq/gemini_cli_is_awesome_but_only_when_you_make


This was then extended as a Claude Code command `god-cli` to support OpenAI Codex also
https://github.com/alexsmedile/god-cli/blob/main/god-cli.md.

So a "[Map repo architecture, find cause of memory leak, and propose a precise patch](https://github.com/alexsmedile/god-cli/blob/main/TEST.md#test-3--multi-agent-sequence)" prompt to Claude Code would 

- Route to Gemini → architecture map.
- Route to Codex → debugging/diagnosis.
- Route to Claude → minimal diff patch.


## Breakthrough Method of Agile AI-Driven Development

I researched and evaluated different Agent-Based Frameworks for Software Engineering.
[Breakthrough Method of Agile AI-Driven Development](./swe_agents_report.md) was the one I selected as being closest to my [views](introduction/#software-10-redux).

[Software Engineering 1.0 Redux](./swe_redux.md) shows this in action with the inputs, chat history, output artifacts.

I added several features that I will merge back:

- a security architect (Chris)
- a vulnerability tech (Tanja) for code analysis
    - uses sub-agents to combine traditional SAST, Dependency tools with LLMs


## CLAUDE.md

This [CLAUDE.md](https://gist.githubusercontent.com/dwillitzer/d3d103b850a1ef8ddc14e9b5d99a46f1/raw/3ae752ac06e4c6c07e81d38b98bc566887a58f3b/claude_development_policy.md) addresses some of the undesirable behaviors I observed:

1. sycophancy - I prefer my reality raw 
2. code without test - so TDD approach
3. code without checking for existing code or being overly eager to code
4. doing something to get the job done - but not the actual documented plan e.g. 
      1. mocks or stubs 
      2. instead of installing a documented needed dependency, working around it with a lesser alternative.

## Takeaways
  
!!! success "Key Takeaways"

    1. By instructing Claude Code (via a god-cli Command) to route specific tasks to specific CLI tools (Google Gemini CLI, OpenAI Codex CLI), you get the best tool for the job, while saving $.
    2. Breakthrough Method of Agile AI-Driven Development (with my security additions) fits my current views of Software Engineering with GenAI.
    3. [CLAUDE.md](https://gist.githubusercontent.com/dwillitzer/d3d103b850a1ef8ddc14e9b5d99a46f1/raw/3ae752ac06e4c6c07e81d38b98bc566887a58f3b/claude_development_policy.md) addresses some of the undesirable behaviors I observed.