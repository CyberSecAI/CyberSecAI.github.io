# Overview

Overall, there’s different components to the CWE assignment system:

1. RAG Corpus: Representations of the MITRE CWE Specification. 
      1. PDF version of the MITRE CWE Specification 
         1. https://cwe.mitre.org/data/downloads.html 
      2. JSON version of the MITRE CWE Specification 
         1. https://github.com/CWE-CAPEC/REST-API-wg/blob/main/json_repo/cwe.json
      3. JSON version of the modified MITRE CWE Specification to add and remove parts to make it more relevant to CWE assignment for an LLM as described [here](https://github.com/CyberSecAI/cwe_top25/tree/main?tab=readme-ov-file#add-cve-descriptions-to-top-25-and-remove-rationale-and-cwe-entries-that-are-not-a-cwe)
         1. https://github.com/CyberSecAI/cwe_top25/tree/main/data_out/output_jsonl 


    !!! tip
        JSON is preferred over PDF as PDF is lossy.

2. Different GPT setups
      1. ChatGPT GPT
         1. Requires you and users to have a paid ChatGPT subscription
      2. NoteBookLM 
         1. Anyone with a Google account can get up and running in 5 minutes for free.
      3. VertexAI
         1. This allows the most customization - but there's more effort to set it up and it is not free.
3. Prompts: 
      1. Various Prompts can be used depending on what you want
