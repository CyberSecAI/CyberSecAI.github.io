---
icon: material/play-box-edit-outline 
---

# CISA Vulnrichment

!!! abstract "Overview"

    I was reading a [post on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7214295735440187393?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7214295735440187393%2C7214365350828613632%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287214365350828613632%2Curn%3Ali%3Aactivity%3A7214295735440187393%29) and the CWE assigned by CISA ADP looked wrong so...

    * I used my NotebookML CWE notebook, and other LLMs, to determine the appropriate CWE.
    * I then raised an issue: https://github.com/cisagov/vulnrichment/issues/84.

    I then decided to dig a bit more into this... specifically the CWEs assigned by CISA ADP.

    I used a consensus of LLMs to review all CWEs assigned by CISA ADP to find issues:

    * These issues were found automatically by a consensus of 3 LLMs: ChatGPT4o, Gemini 1.5 Pro, Claude 3.5 Sonnet who were asked to review CWEs assigned to CVEs assigned by CISA ADP.
    * The consensus output was then reviewed by a human (me).
    * I created [3 Issues initially](https://github.com/cisagov/vulnrichment/issues/created_by/Crashedmind) (though there are a lot more) 

    This section shows the different approaches used (and the subscription plan used):

    1. no-code using the browser chat interface: 
        1. Gemini 1.5 Pro (subscription)
        2. Claude 3.5 Sonnet (no subscription)
    2. code: 
        1. ChatGPT4o [OpenAI Batch API](https://platform.openai.com/docs/guides/batch/overview) (Plus Plan)



## CISA Vulnrichment

!!! quote
    The CISA Vulnrichment project is the public repository of CISA's enrichment of public CVE records through CISA's ADP (Authorized Data Publisher) container. In this phase of the project, CISA is assessing new and recent CVEs and adding key SSVC decision points. Once scored, some higher-risk CVEs will also receive enrichment of CWE, CVSS, and CPE data points, where possible.

    https://github.com/cisagov/vulnrichment

I have great admiration for CISA and their pragmatic initiatives like [CISA KEV](https://riskbasedprioritization.github.io/cisa_kev/cisa_kev/) and [SSVC](https://riskbasedprioritization.github.io/ssvc/SSVC/) and have [spoken about them](https://riskbasedprioritization.github.io/talks/talks/) and applied them in production.

!!! Tip
    One of the many benefits of this Vulnrichment project is that feedback can be provided as GitHub issues and the team is responsive.
    
    * The 'Bug' label was assigned same day to the 3 issues I submitted: https://github.com/cisagov/vulnrichment/issues/created_by/Crashedmind 

    My overall goal here was to 

    * Show that LLMs could augment human analysts where vulnerability enrichment today is largely done manually.
    * Show how to use them for this purpose.
    * Get people to use LLMs to improve the quality of the CVE data in general, and in this specific example case, the CWE data.
    * Maximize the quality and value of the CISA ADP data and enrichment.

## Get CVEs Enriched by CISA ADP


## Approach to using LLMs
The recipe focuses on Time-To-Value - and minimization of human effort - to find the most inappropriate assigned CWEs ASAP.

* A more complete and costly approach would be to submit all CVE Descriptions to all 3 LLMs.

### Don't Train A Model On Bad Data!
It is possible to train a Language Model as a Classifier to assign CWEs to a CVE - and there are several research papers that took that approach (with limited success).

This approach is delusional based on my research and experience of assigned CWEs.

Per [Steve Christey Coley, CWE tech lead](https://www.linkedin.com/feed/update/urn:li:activity:7186373368344920064?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7186373368344920064%2C7186417379470385153%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287186417379470385153%2Curn%3Ali%3Aactivity%3A7186373368344920064%29):

!!! quote 
    There has been significant interest in using AI/ML in various applications to use and/or map to CWE, but in my opinion there are a number of significant hurdles, e.g. you can't train on "bad mappings" to learn how to do good mappings.

So, rather than train a model on bad data, we can ask a model to assign / validate a CWE based on its understanding of the CWEs available e.g.

1. a closed-model with access to the CWE specification only (and no other data)
2. an open-model with access to the CWE specification and other data



### Validate with LLMs

Different approaches are possible when providing the CVE Description to the LLM:

1. provide the CWE assigned as part of the CVE, and ask the LLM if it agrees or not, and if not why
2. ask the LLM to assign one or more CWEs

The first approach is easier and simpler and cheaper (in terms of token use i.e. shorter response output), and better as a first pass option to get the low hanging fruit.

The second approach could be used at the time of CWE assignment to get a second opinion.


### Consensus

To minimize human effort, 3 LLMs are used and the consensus is reviewed
      
* The LLMs are state-of-the-art models from different providers i.e. the best available and reasonably independent.
* The results are sorted by consensus i.e. 3 models in agreement, then 2 models in agreement,....
* A Human (me) then reviewed (sorted by consensus) and made the final decision.



### Recipe

1. Get the Vulnrichment subset of CVEs where CISA ADP assigned a CWE (regardless of whether the CWE was the same or different than that assigned by the CNA)
      1. ~1.5K (CISA ADP Assigned CWEs) of ~~8K CVEs (in Vulnrichment)
2. Ask ChatGPT4o (via Batch API) to Agree (Yes/No) with the assigned CWE (and provide a Confidence score, and rationale if not)
      1. ~700 (No) of ~1.5K 
      2. Sort these by Confidence score i.e. start with the highest Confidence ones.
3. For the subset where ChatGPT4o disagrees, ask Gemini and Claude.

### Create a Prompt
#### Chat Interface - Table Output

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

The table output allows copy-and-pasting by a human into a sheet.

#### Batch API Interface - JSON Output


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
The JSON output allows processing by machines.


!!! note
    It is possible to submit multiple CVEs in one prompt for each batch entry i.e. similar to what is done when using the Chat interface.

    * But this is not done in this example; each batch request contains a single CVE only (per the [OpenAI Batch API](https://platform.openai.com/docs/guides/batch/overview) example)

The prompt consists of these parts:

1. Role + Task: which is the same for the Chat and API interface
2. Output format: which is different for the Chat and API interface
3. A binary value Agree is requested
4. The rationale only if there is disagreement. This saves on output tokens.
5. A Confidence score to limit impacts of hallucinations, and as a way to assess and prioritize responses by confidence.
6. No (Few-shot) examples are provided. Based on the results, these were not necessary.
      1. If Few-shot examples were required, I'd submit multiple CVEs in a single batch request (because putting the examples in each single CVE request would add a LOT of input tokens)


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
Batch Interface API.

The ~1500 ADP CVE-CWE pairs were split into 15 files of 100 CVE-CWE pair prompts to comfortably fit under this token limit.

* very little effort was spent to optimize the file size (number of prompts per batch), or the prompt size.
* The cost to process the ~1500 ADP CVE-CWE pairs: ~$1.50.



## Takeaways
  
!!! success "Takeaways" 

    1. The value of CVE data depends on its quality. 
    2. For all published CVEs to date, [the quality of CWEs assigned is questionable](https://www.linkedin.com/feed/update/urn:li:activity:7186373368344920064?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7186373368344920064%2C7186417379470385153%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287186417379470385153%2Curn%3Ali%3Aactivity%3A7186373368344920064%29).
    3. A large part of that is that humans can't grok 1000+ CWEs. LLMs can.
    4. Using LLMs to suggest or validate CWEs can reduce the manual effort and error in CVE assignment.
    5. LLMs can validate CWEs at scale e.g. using Batch mode, or multiple CVEs per prompt, or both.
    6. LLMs perform well at this task and, given they can be automated, can augment the human manual effort, and improve the quality of assigned CWEs.