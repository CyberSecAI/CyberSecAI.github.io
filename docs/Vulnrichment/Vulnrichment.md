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

    1. no-code using the browser chat interface of 3 LLMs: 
        1. ChatGPT4o (subscription)
        2. Gemini 1.5 Pro (subscription)
        3. Claude 3.5 Sonnet (no subscription)
    2. code: [OpenAI Batch API](https://platform.openai.com/docs/guides/batch/overview)



## CISA Vulnrichment

!!! quote
    The CISA Vulnrichment project is the public repository of CISA's enrichment of public CVE records through CISA's ADP (Authorized Data Publisher) container. In this phase of the project, CISA is assessing new and recent CVEs and adding key SSVC decision points. Once scored, some higher-risk CVEs will also receive enrichment of CWE, CVSS, and CPE data points, where possible.

    https://github.com/cisagov/vulnrichment

I have great admiration for CISA and their pragmatic initiatives like [CISA KEV](https://riskbasedprioritization.github.io/cisa_kev/cisa_kev/) and [SSVC](https://riskbasedprioritization.github.io/ssvc/SSVC/).

One of the many benefits of this Vulnrichment project is that feedback can be provided as GitHub issues and the team is responsive.

!!! Tip
    My overall goal here was to show 

    * that LLMs could augment human analysts where vulnerability enrichment today is largely done manually.
    * how to use them for this purpose

## Get CVEs Enriched by CISA ADP


## Validate with LLMs

### Create a Prompt

We only want the rationale if there is disagreement. This saves on tokens.

### Prompt LLMs

#### Gemini 1.5 Pro Browser Chat Interface

#### Claude 3.5 Sonnet Browser Chat Interface


#### [OpenAI Batch API](https://platform.openai.com/docs/guides/batch/overview)


## Takeaways
  
!!! success "Takeaways" 

    1. I 