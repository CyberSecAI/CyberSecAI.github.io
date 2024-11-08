# Overview

!!! abstract "Overview"
      There are several options to consider when building an LM solution for CWE assignment as described here.
## Approach to using Language Models

### Don't Train A Model On Bad Data!

It is possible to train a Language Model as a Classifier to assign CWEs to a CVE Description - and there are several research papers that took that approach e.g.

* [V2W-BERT: A Framework for Effective Hierarchical Multiclass Classification of Software Vulnerabilities](https://arxiv.org/pdf/2102.11498v1.pdf) 
* [Automated Mapping of CVE Vulnerability Records to MITRE CWE Weaknesses](https://arxiv.org/pdf/2304.11130.pdf)

The problems with this approach:

1. It's delusional based on my research and experience of incorrect assigned CWEs in general - Garbage In Garbage Out
    1. Per [Steve Christey Coley, CWE tech lead](https://www.linkedin.com/feed/update/urn:li:activity:7186373368344920064?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7186373368344920064%2C7186417379470385153%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287186417379470385153%2Curn%3Ali%3Aactivity%3A7186373368344920064%29): 

    !!! quote 
        There has been significant interest in using AI/ML in various applications to use and/or map to CWE, but in my opinion there are a number of significant hurdles, e.g. you can't train on "bad mappings" to learn how to do good mappings.

2. It removes a lot of the context that could be available to an LM by reducing the reference target down to a set of values or classes (for the given input CVE Descriptions)


### Train on Good Data and the Full Standard

We can "train" on "good mappings".

1. The CWE standard includes known "good mappings" e.g. [CWE-917 Observed Examples](https://riskbasedprioritization.github.io/risk/Log4Shell/#mitre-cwe-917) includes CVE-2021-44228 and its Description.
    1. The count of these CVE Observed Examples varies significantly per CWE. 
    2. There's ~3K CVE Observed Examples in the CWE standard.
2. The [Top25 Dataset](https://github.com/CyberSecAI/cwe_top25) of known-good mappings contains ~6K CVEs with known-good [CWE mappings by MITRE](https://www.youtube.com/watch?v=AtBZIAikdL0&list=PLBAUUhONOrO_aB01lOv6XNRTHD4ueFVTp&t=1142s).
3. We can use the full CWE standard and associated known good CWE mappings as the target, allowing an LLM to compare the CVE Description (and other data) to this.
    1. And moreover, prompt the LLM to provide similar CVEs to support its rationale for the CWE assignment

!!! tip
    Rather than train a model on bad data, we can ask a model to assign / validate a CWE based on its understanding of the CWEs available (and its understanding of CWEs assigned to similar CVEs based on the Observed and Top25 Examples for each CWE in the standard).

    We can ask the model to follow the [MITRE CWE Guidance](https://cwe.mitre.org/documents/cwe_usage/guidance.html) when assigning a CWE.

## Closed or Open Model
We can use a Closed or Open Model:

1. a closed-model with access to the CWE specification only (and no other data) e.g. NotebookLM
2. an open-model with access to the CWE specification and other data


## RAG Corpus

Representations of the MITRE CWE Specification:

   1. PDF version of the MITRE CWE Specification 
      1. https://cwe.mitre.org/data/downloads.html 
   2. JSON version of the MITRE CWE Specification 
      1. https://github.com/CWE-CAPEC/REST-API-wg/blob/main/json_repo/cwe.json
   3. JSON version of the modified MITRE CWE Specification to add and remove parts to make it more relevant to CWE assignment for an LLM as described [here](https://github.com/CyberSecAI/cwe_top25/tree/main?tab=readme-ov-file#add-cve-descriptions-to-top-25-and-remove-rationale-and-cwe-entries-that-are-not-a-cwe)
      1. https://github.com/CyberSecAI/cwe_top25/tree/main/data_out/output_jsonl 


    !!! tip
        JSON is preferred over PDF as PDF is generally more lossy because it is less structured.

## GPT setups
Different GPT setups e.g.

   1. [ChatGPT GPT](./cwe_gpt.md)
      1. Requires you and users to have a paid ChatGPT subscription
   2. [NoteBookLM](./NotebookLM_Cwe.md)
      1. Anyone with a Google account can get up and running in 5 minutes for free.
   3. [VertexAI](./vertex_ai.md)
      1. This allows the most customization - but there's more effort to set it up and it is not free.

## Prompts

1. Various Prompts, and [Prompt Engineering Techniques](../prompt_engineering/prompt_engineering.md), can be used depending on what you want.

## Model and Environment

For processing 250K+ CVE Descriptions, speed, latency and cost are important considerations, in addition to accuracy.

Based on [comparing LLMs](../introduction/cybsersecurity.md#comparing-llms) as at September 2024, Gemini 1.5 Flash was chosen.

There are different Google AI Environments:
   - [Google AI Studio](https://aistudio.google.com/prompts/new_chat)
     - lower learning curve and cost and capability
   - [Vertex AI Studio](https://console.cloud.google.com/vertex-ai/studio) or VertexAI in general
