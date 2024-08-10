# Grounding


!!! abstract "Overview"

    NotebookLM highlights the benefits of a grounded closed system - and it provides links to the content it references in the data sources.

    There are many tools that can be used to build such a system.

    In this section, we'll explore different solutions, using MITRE CWE as the data source.

    This section gives some examples:

    1. [ChatGPT GPT](./cwe_gpt.md)
    2. [Vertex AI Agent](./vertex_ai.md)


## Grounding Overview

https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview
https://stratechery.com/2024/gemini-1-5-and-googles-nature/ 


!!! quote
    You can ground language models to your own text data using Vertex AI Search as a datastore. With Vertex AI Search you integrate your own data, regardless of format, to refine the model output. Supported data types include:

    * Website data: Directly use content from your website.
    * Unstructured data: Utilize raw, unformatted data.

    When you ground to your specific data the model can perform beyond its training data. By linking to designated data stores within Vertex AI Search, the grounded model can produce more accurate and relevant responses, and responses directly related to your use case.

    https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview#ground-private