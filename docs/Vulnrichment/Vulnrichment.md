---
icon: material/play-box-edit-outline 
---

# CISA Vulnrichment

!!! abstract "Overview"

    I was reading a [post on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7214295735440187393?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7214295735440187393%2C7214365350828613632%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287214365350828613632%2Curn%3Ali%3Aactivity%3A7214295735440187393%29) and the CWE assigned by CISA ADP looked wrong so...

    * I used my NotebookML CWE notebook, and other LLMs, to determine the appropriate CWE.
    * I then raised an issue: https://github.com/cisagov/vulnrichment/issues/84.

    I then decided to dig a bit more into this... specifically the CWEs assigned by CISA ADP

    * I created [3 Issues initially](https://github.com/cisagov/vulnrichment/issues/created_by/Crashedmind) (though there are likely a lot more based on the results) 
        * These issues were found automatically by a consensus of 3 LLMs: ChatGPT4o, Gemini 1.5 Pro, Claude 3.5 Sonnet who were asked to review CWEs assigned to CVEs assigned by CISA ADP.
        * The output was then reviewed by a human (me).

    This section shows the different approaches used:

    1. no-code using the browser chat interface: 
        2. Gemini 1.5 Pro (subscription)
        3. Claude 3.5 Sonnet (no subscription)
    2. code: 
        1. ChatGPT4o [OpenAI Batch API](https://platform.openai.com/docs/guides/batch/overview)



## CISA Vulnrichment

!!! quote
    The CISA Vulnrichment project is the public repository of CISA's enrichment of public CVE records through CISA's ADP (Authorized Data Publisher) container. In this phase of the project, CISA is assessing new and recent CVEs and adding key SSVC decision points. Once scored, some higher-risk CVEs will also receive enrichment of CWE, CVSS, and CPE data points, where possible.

    https://github.com/cisagov/vulnrichment

I have great admiration for CISA and their pragmatic initiatives like [CISA KEV](https://riskbasedprioritization.github.io/cisa_kev/cisa_kev/) and [SSVC](https://riskbasedprioritization.github.io/ssvc/SSVC/).



!!! Tip
    One of the many benefits of this Vulnrichment project is that feedback can be provided as GitHub issues and the team is responsive.

    My overall goal here was to 

    * show that LLMs could augment human analysts where vulnerability enrichment today is largely done manually.
    * show how to use them for this purpose.
    * get people to use LLMs to improve the quality of the CVE data in general, and in this specific example case, the CWE data.

## Get CVEs Enriched by CISA ADP


## Validate with LLMs
Different approaches are possible when providing the CVE Description to the LLM:

1. provide the CWE assigned as part of the CVE, and ask the LLM if it agrees or not, and if not why
2. ask the LLM to assign one or more CWEs

The first approach is easier and simpler and cheaper (in terms of token use i.e. shorter output prompts), and better as a first pass option to get the low hanging fruit.

The second approach could be used at the time of CWE assignment to get a second opinion.

### Create a Prompt

The prompt consists of these parts:
1. Role + Task: which is the same for the Chat and API interface
2. Output format: which is different for the Chat and API interface

#### Chat Interface - Table Ouput

````
caption_system_prompt =
You are a cybersecurity expert specializing in identifying Common Weakness Enumeration (CWE) IDs from CVE descriptions.
Your goal is is to say if you Agree with the assigned CWE ID or not.
You will be provided with a CVE ID and description amd a CWE ID that has been assigned to that CVE description.

Please provide the response in a table 'cve_id', 'CWE_ID', 'Agree'. "Rationale", Confidence' where
1. Agree: string // Yes or No
2. Rationale: string // Only if you do not Agree, provide a rationale why not
3. Confidence: string // a confidence score between 0 and 1
````

#### Batch API Interface - JSON Ouput


````
caption_system_prompt =
You are a cybersecurity expert specializing in identifying Common Weakness Enumeration (CWE) IDs from CVE descriptions.
Your goal is is to say if you Agree with the assigned CWE ID or not.
You will be provided with a CVE ID and description amd a CWE ID that has been assigned to that CVE description.

You will output a json object containing the following information:
{
    Agree: string // Yes or No
    Rationale: string // Only if you do not Agree, provide a rationale why not
    Confidence: string // a confidence score between 0 and 1
}
````

!!! note
    It is possible to submit multiple CVEs in one prompt for each batch entry i.e. similar to what is done when using the Chat interface.
    But this is not done in this example; each batch request contains a single CVE only.


Prompt features:

1. A binary value Agree is requested
2. The rationale only if there is disagreement. This saves on ouput tokens.
3. A Confidence score to limit impacts of hallucinations, and as a way to assess and prioritize responses by confidence.
4. No (Few-shot) examples are provided. 


### Prompt LLMs

#### Gemini 1.5 Pro Browser Chat Interface

The chat interface was used in this example submitting multiple CVEs in one prompt.

#### Claude 3.5 Sonnet Browser Chat Interface

##### Model
Currently: Claude 3.5 Sonnet was used as it has the best performance vs cost for Claude models.

<figure markdown>
![](../assets/images/claude.png)
https://docs.anthropic.com/en/docs/welcome 
</figure>

##### Interface
Currently: Claude does not support a native [Batch API interface](https://www.anthropic.com/pricing#anthropic-api) - though 
[Amazon Bedrock](https://aws.amazon.com/bedrock/pricing/) supports batching of prompts to models including Claude.

The chat interface was used in this example submitting multiple CVEs in one prompt.




#### [OpenAI Batch API](https://platform.openai.com/docs/guides/batch/overview)

##### Model
gpt-4o

##### Plan
The Plus plan subscription was used.

!!! quote
    
    There are some restrictions:

       * The file can contain up to 50,000 requests.
       * The file cannot be more than 100 MB in size.

    Enqueued token limit reached for gpt-4o in organization XYZ. Limit: 90,000 enqueued tokens. Please try again once some in_progress batches have been completed.'


##### Interface
Batch Interface API
The ~1500 ADP CVE-CWE pairs were split into 15 files of 100 CVE-CWE pair prompts to comfortably fit under this token limit.

* very little effort was spent to optimize the file size (number of prompts per batch), or the prompt size.
* The cost to process the ~1500 ADP CVE-CWE pairs: ~$1.50.



## Takeaways
  
!!! success "Takeaways" 

    1. I 