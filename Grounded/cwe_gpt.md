# ChatGPT CWE GPT

!!! abstract "Overview"

    NotebookLM highlights the benefit of a grounded closed system.

    There are many tools that can be used to build such a system.

    Here we'll use ChatGPT with the MITRE CWE specification to aid mapping CWEs to vulnerability descriptions.

    This is a no-code option.

## Recipe
    1. Use ChatGPT GPTs ["custom versions of ChatGPT that combine instructions, extra knowledge, and any combination of skills."](https://chatgpt.com/gpts) 
    2. Provide the MITRE CWE specification as the "extra knowledge" in JSON format (not PDF)
    3. Limit the GPT to that knowledge only i.e. disable web search.


## MITRE CWE Specification
1. Get the MITRE CWE Specification as JSON from https://github.com/CWE-CAPEC/REST-API-wg/blob/main/json_repo/cwe.json
   1. Using a JSON text version instead of PDF 
      1. ensures all the relevant text we want is fed to the model (e.g. text extraction from PDFs can be lossy for tables)
      2. allows us to remove content that is not relevant e.g. "ContentHistory" can contain a lot of text that is not relevant to CWE assignment
2. Remove the "ContentHistory" entries as this is not useful to assign CWEs and is a lot of content
2. Split it into smaller files
   1. because the single file is too large to import
   2. use Claude 3.5 to generate the python code to do this
   
## Configure ChatGPT CWE GPT
1. Import the MITRE CWE Specification as split JSON files
2. Disable all capabilities.
   1. Web browsing is disabled so the answers come from the imported MITRE CWE Specification
3. Provide example starter prompts
   1. what is the best CWE to describe the root cause weakness in CVE "an issue in the Pickle Python library of some product allows attackers to execute arbitrary commands". Provide CVEs with the most similar root cause to support your answer.
   2. what is the best CWE to describe the root cause weakness in CVE "ProductX contains a default SSH public key in the authorized_keys file. A remote attacker could use this key to gain root privileges.". Provide CVEs with the most similar root cause to support your answer.
   3. what cwe ids are associated with xss. list them all
   4. what cwe ids are associated with path or directory traversal. list them all

<figure markdown>
![](../assets/images/chatgpt_cwe_gpt.png)
</figure>

  
!!! success "Takeaways" 

    1.
