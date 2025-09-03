# Overview

!!! abstract 

    This section looks at some Claude Code setups I use.



## Claude Code CLI God Mode

I use Claude Code CLI as my main tool. 

I wanted a way to use other models via Claude Code to 

- reduce Claude Code token usage / cost (currently on Pro plan)
- use the best tool for the job but maintain context in Claude Code

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



## Takeaways
  
!!! success "Key Takeaways"

    By instructing Claude Code (via a god-cli Command) to route specific tasks to specific CLI tools (Google Gemini CLI, OpenAI Codex CLI), you get the best tool for the job, while saving $.