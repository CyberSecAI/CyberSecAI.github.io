# Prompt Engineering

!!! abstract "Overview"

    A large part of working LLMs is knowing how to prompt them to get the information you want.

    ChatGPTo will be used here but the techniques apply in general to any LLM.

## Prompt Guides
There are many books, guides, and articles on Prompt Engineering. Some of the better ones are listed here:

1. [Prompt Engineering Guide](https://www.promptingguide.ai/) 
1. [OpenAI Prompt engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) 
1. [Google Gemini Prompting guide 101 - A quick-start handbook for effective prompts, April 2024 edition](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf)
1. [How I Won Singapore’s GPT-4 Prompt Engineering Competition](https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41), Dec 2023
2. [Prompt Engineering for Generative AI](https://www.oreilly.com/library/view/prompt-engineering-for/9781098153427/), May 2024
3. [Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) 




## Useful Prompt Tactics

Some tactics I find particularly useful:

1. Ask the LLM to generate the prompt.
      1. Do this in 2 parts (task decomposition)
         1. Ask the LLM what techniques are best to use for effective prompt engineering
         2. Ask the LLM to create a prompt using these techniques for the objective and example you specify
3. Ask the LLM to provide a confidence score for their answer. 
      1. People can be fooled by the fluency of LLMs aka hallucinations 
      2. LLMs know how confident they are.
      3. So asking an LLM to rate their confidence in the answer can reduce blind trust.
4. Ask the LLM (or a different LLM) to review the answer and provide improvements.


## Ask the LLM to generate the prompt

### Ask the LLM what techniques are best to use for effective prompt engineering?


<figure markdown>
![Guide](../assets/images/prompting1.png)
![Guide](../assets/images/prompting1_2.png)
</figure>


### Ask the LLM to create a prompt using these techniques for the objective and example you specify

<figure markdown>
![Guide](../assets/images/prompting3.png)
</figure>




````
_functions.php in cpCommerce 1.2.x, possibly including 1.2.9, sends a redirect but does not exit when it is called directly, which allows remote attackers to bypass a protection mechanism to conduct remote file inclusion and directory traversal attacks, execute arbitrary PHP code, or read arbitrary files via the GLOBALS[prefix] parameter, a different vector than CVE-2003-1500.


#CVE# _functions.php in cpCommerce 1.2.x, possibly including 1.2.9, sends a redirect but does not exit when it is called directly, which allows remote attackers to bypass a protection mechanism to conduct remote file inclusion and directory traversal attacks, execute arbitrary PHP code, or read arbitrary files via the GLOBALS[prefix] parameter, a different vector than CVE-2003-1500.
#IMPACT# Remote Code Execution, Information Disclosure, Security Bypass
#RATIONALE# The description specifies multiple potential impacts:
1. **Remote Code Execution**: The ability to "execute arbitrary PHP code" directly implies a high severity impact where an attacker can run malicious code on the affected system.
2. **Information Disclosure**: The mention of "read arbitrary files" suggests that attackers can access sensitive information stored in files.
3. **Security Bypass**: The bypass of a protection mechanism to conduct remote file inclusion and directory traversal attacks implies that security controls are being circumvented.
#CONFIDENCE# 95
````



<figure markdown>
![Guide](../assets/images/prompting_classification1.png)
</figure>

### Ask the LLM to review the answer and provide improvements.
<figure markdown>
![Guide](../assets/images/prompting_classification2.png)
</figure>


## Fabric Prompt Collection and Framework

https://github.com/danielmiessler/fabric/tree/main 

!!! quote
    Since the start of 2023 and GenAI we've seen a massive number of AI applications for accomplishing tasks. It's powerful, but it's not easy to integrate this functionality into our lives.

    In other words, AI doesn't have a capabilities problem—it has an integration problem.
    Fabric was created to address this by enabling everyone to granularly apply AI to everyday challenges.


    One of fabric's primary features is helping people collect and integrate prompts, which we call Patterns, into various parts of their lives.


### Fabric Prompts 
https://github.com/danielmiessler/fabric/tree/main/patterns


### Fabric Prompt to Improve Prompts 
https://github.com/danielmiessler/fabric/blob/main/patterns/improve_prompt/system.md




## Takeaways
  
!!! success "Takeaways" 

    1. ToDo
  