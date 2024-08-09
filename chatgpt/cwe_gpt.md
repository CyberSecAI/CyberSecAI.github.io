# ChatGPT CWE GPT

!!! abstract "Overview"

    NotebookLM highlights the benefit of a grounded closed system.

    There are many tools that can be used to build such a system.

    Here we'll use ChatGPT with the MITRE CWE specification to aid mapping CWEs to vulnerability descriptions.

## Recipe
    1. use ChatGPT GPTs ["custom versions of ChatGPT that combine instructions, extra knowledge, and any combination of skills."](https://chatgpt.com/gpts) 
    2. provide the MITRE CWE specification as the "extra knowledge" in JSON format (not PDF)
    3. limit the GPT to that knowledge only i.e. disable web search.


## MITRE CWE Specification
1. Get the MITRE CWE Specification as JSON from https://github.com/CWE-CAPEC/REST-API-wg/blob/main/json_repo/cwe.json
   1. Using a JSON text version instead of PDF 
      1. ensures all the relevant text we want is fed to the model (e.g. text extraction from PDFs can be lossy for tables)
      2. allows us to remove content that is not relevant e.g. "ContentHistory" can contain a lot of text that is not relevant to CWE assignment
2. Remove the "ContentHistory" entries as this is not useful to assign CWEs and is a lot of content
2. Split it into smaller files
   1. because the single file is too large to import
   2. use Claude 3.5 to generate the python code to do this
   

<figure markdown>
![](../assets/images/chatgpt_cwe_gpt.png)
</figure>

