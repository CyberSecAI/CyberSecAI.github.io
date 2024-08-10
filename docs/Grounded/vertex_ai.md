# Google Vertex AI Agent Builder

!!! abstract "Overview"

    Here we'll use Vertex AI Agent Builder with the MITRE CWE specification to aid mapping CWEs to vulnerability descriptions.

    This is a no-code option.

    We'll attempt to implement a closed grounded system to ensure the accuracy of the data (and mitigate hallucinations)cwe_gpt

    2. **Grounded**: content is provided to inform the answers
    1. **Closed system**: answers come from only the documents you provide

!!! success "Result"
    The result is that we have a grounded closed system.

    But we don't have reference links to the source content in the response.


## Grounding Confidence

!!! quote
      For each response generated from the content of your connected data stores, the agent evaluates a confidence level, which gauges the confidence that all information in the response is supported by information in the data stores. You can customize which responses to allow by selecting the lowest confidence level you are comfortable with. Only responses at or above that confidence level will be shown.

      There are 5 confidence levels to choose from: VERY_LOW, LOW, MEDIUM, HIGH, and VERY_HIGH.

      https://cloud.google.com/dialogflow/vertex/docs/concept/tools
      

!!! quote
      To create a data store and connect it to your app, you can use the Tools link in the left navigation of the console. Follow the instructions to create a data store.
      https://cloud.google.com/dialogflow/vertex/docs/concept/tools


## Recipe
Same recipe as [before](./cwe_gpt.md#recipe) but we'll use [Google Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder)





## MITRE CWE Specification
Same [MITRE CWE Specification](./cwe_gpt.md#mitre-cwe-specification) as the data source.
   
## Build Vertex AI Agent 

1. [Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder?hl=en) 
2. Create App 
3. Select app type
      1. Agent (preview) "Built using natural language, agents can answer questions from data, connect with business systems through tools and more"
4. Configure [Data Store in Tools ](https://cloud.google.com/dialogflow/vertex/docs/concept/tools#data-store)
      1. [Chunking is not used because it is not currently supported by grounding](https://github.com/GoogleCloudPlatform/generative-ai/issues/694#issuecomment-2148309711).  
5. I used both the local Data Store and the MITRE CWE website for evaluation purposes.
6. There are lots of other Settings available like Logging, Git integration to push/pull agents from a Github repo, or just download the JSON file that represents the agent.
7. The built agent supports [Interactions with the API ](https://cloud.google.com/dialogflow/vertex/docs/quick/api).


!!! quote
      Note: Conversation history is used as context during tool invocation. Learn more


<figure markdown>
![](../assets/images/vertex_ai_agent1.png)
</figure>

<figure markdown>
![](../assets/images/vertex_ai_agent2.png)
</figure>



## Check if the System is Closed

!!! quote
   
      What is a dog?


      <figure markdown>
      ![](../assets/images/vertex_ai_what_is_a_dog.png)
      </figure>

!!! success
      The system is closed because the GPT can't answer the question because there is no information about dogs in the MITRE CWE specification.

## What are the different types of XSS?

<figure markdown>
![](../assets/images/vertex_ai_xss_types.png)
</figure>


## What CWE IDs Relate To XSS?

<figure markdown>
![](../assets/images/vertex_ai_xss.png)
</figure>

## What Is The Parent Weakness Or CWE For XSS And CSRF?

<figure markdown>
![](../assets/images/vertex_ai_parent.png)
</figure>



## What CWE IDs Relate To Path Or Directory Traversal?  List All CWE IDs And Their Description In A Table

<figure markdown>
![](../assets/images/vertex_ai_path_traversal.png)
</figure>



## What is the CWE Associated With CVE

!!! quote
      
      What is the CWE associated with CVE-2021-27104 "Accellion FTA OS Command Injection Vulnerability"

      What is the CWE associated with "Cisco Small Business RV320 and RV325 Routers Information Disclosure Vulnerability"

<figure markdown>
![](../assets/images/vertex_ai_cves.png)
</figure>

## Example Usage: CWE-1394
!!! quote

      what is the best CWE to describe the root cause weakness in CVE "ProductX contains a default SSH public key in the authorized_keys file. A remote attacker could use this key to gain root privileges.". 

<figure markdown>
![](../assets/images/vertex_ai_ssh.png)
</figure>


## Example Usage: CWE-502

!!! quote
      
      what is the best CWE to describe the root cause weakness in CVE "an issue in the Pickle Python library of some product allows attackers to execute arbitrary commands". 

<figure markdown>
![](../assets/images/vertex_ai_pickle.png)
</figure>

## Other App Builder Docs 

There were not used or required but listing here as I found them informative.

1. https://codelabs.developers.google.com/codelabs/vertex-ai-conversation#0
2. https://codelabs.developers.google.com/build-google-quality-rag#0
3. https://github.com/GoogleCloudPlatform/generative-ai/tree/main
4. https://github.com/GoogleCloudPlatform/generative-ai/tree/main/conversation/chat-app
5. https://cloud.google.com/generative-ai-app-builder/docs/samples?language=python
6. https://cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-multi-turn-search?hl=en
7. https://cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-import-documents?hl=en
8. https://www.googlecloudcommunity.com/gc/Community-Blogs/Building-and-Deploying-AI-Agents-with-LangChain-on-Vertex-AI/bc-p/750793#M415
9. https://medium.com/google-cloud/gen-ai-grounding-with-vertex-ai-llm-3cb1cbe9f9d2
10. https://medium.com/google-cloud/designing-data-store-hybrid-agents-with-dialogflow-cx-vertex-ai-agents-070082f07cb4
11. https://www.cloudskillsboost.google/paths/236/course_templates/978/labs/488165
12. https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/2d22382cf72840dcde313db2f2feb2115f9fbd70/gemini/grounding/intro-grounding-gemini.ipynb?hl=es-419
13. https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/
14. https://saschaheyer.medium.com/vertex-ai-grounding-large-language-models-8335f838990f

## Takeaways

!!! success "Takeaways" 

    1. Google Vertex AI Agent Builder allows/requires more control over the agent than the [ChatGPT GPTs](./cwe_gpt.md) currently. 
    2. Google Vertex AI Agent Builder supports a Closed System with Grounding and [Grounding Confidence threshold](./vertex_ai.md#grounding-confidence) unlike [ChatGPT GPTs](./cwe_gpt.md) currently.
    3. This comes close to [NotebookLM](../NotebookLM/NotebookLM.md) but 
          1. does not provide references from the original documents from which the answer was determined.
          2. NotebookLM responses were more detailed and felt better overall
