# Fabric

!!! abstract "Overview"

     One of Fabric's primary features is helping people collect and integrate prompts



## Fabric Prompt Collection and Framework

https://github.com/danielmiessler/fabric/tree/main 

!!! quote
    Since the start of 2023 and GenAI we've seen a massive number of AI applications for accomplishing tasks. It's powerful, but it's not easy to integrate this functionality into our lives.

    In other words, AI doesn't have a capabilities problem—it has an integration problem.
    Fabric was created to address this by enabling everyone to granularly apply AI to everyday challenges.

    One of fabric's primary features is helping people collect and integrate prompts, which we call Patterns, into various parts of their lives.

The prompts (aka Patterns) are available at https://github.com/danielmiessler/fabric/tree/main/patterns


### Fabric Prompts for CyberSecurity

Fabric has Prompts that are specific to CyberSecurity e.g.

* https://github.com/danielmiessler/fabric/blob/main/patterns/create_threat_model/system.md
* https://github.com/danielmiessler/fabric/blob/main/patterns/analyze_logs/system.md
* https://github.com/danielmiessler/fabric/blob/main/patterns/analyze_malware/system.md
* https://github.com/danielmiessler/fabric/blob/main/patterns/analyze_threat_report/system.md
* https://github.com/danielmiessler/fabric/blob/main/patterns/analyze_threat_report_trends/system.md
* https://github.com/danielmiessler/fabric/blob/main/patterns/write_hackerone_report/system.md
* https://github.com/danielmiessler/fabric/blob/main/patterns/write_semgrep_rule/system.md 

### Fabric Prompt to Improve Prompts 
https://github.com/danielmiessler/fabric/blob/main/patterns/improve_prompt/system.md

### Process Youtube Transcripts

Fabric, and LLMs in general, can process Youtube Transcripts (which are text).

The Youtube Transcript for a video can be retrieved in different ways e.g. https://www.youtube.com/watch?v=oMZN810xfck:

* Click the Transcript button under a video and copy and paste, or download, to a text file
* Use Fabric helper function: [installer/client/cli/yt.py](https://github.com/danielmiessler/fabric/blob/main/installer/client/cli/yt.py) (or other tool)

````
yt --transcript https://www.youtube.com/watch?v=oMZN810xfck
````
The text can then be processed with an LLM.

This download and processing can be done in one command with Fabric
````
yt --transcript https://www.youtube.com/watch?v=oMZN810xfck | fabric -sp extract_wisdom
````
where

* -s is for streaming
* -p is for pattern
* [extract_wisdom](https://github.com/danielmiessler/fabric/tree/main/patterns/extract_wisdom) is the Fabric prompt that extracts wisdom from any text. It addresses the problem of too much content and too little time.


## Takeaways
  
!!! success "Takeaways" 

    1. Fabric is a good resource for prompts with many being related to CyberSecurity.
  
