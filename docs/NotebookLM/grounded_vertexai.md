https://techcommunity.microsoft.com/t5/fasttrack-for-azure/grounding-llms/ba-p/3843857


https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/ground-gemini#private-ground-gemini


If you are starting from scratch, you need to prepare your data for ingestion into Vertex AI Agent Builder. See Prepare data for ingesting to get started.
1. Create a new Cloud Storage bucket
2. Import the split pdf files

[ Create a search data store.](https://cloud.google.com/generative-ai-app-builder/docs/create-data-store-es)



Unstructured documents (PDF, HTML, TXT and more)
Supported file formats: PDF, HTML, TXT (CSV for FAQ, DOCX and PPTX are available in Preview)


Layout parser. Turn on the layout parser for HTML, PDF, or DOCX files if you plan to use Vertex AI Search for RAG. See Chunk documents for RAG for information about this parser and how to turn it on.



Create a search app to link to it and Turn Enterprise edition on.



https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/ground-gemini#generative-ai-gemini-grounding-console


https://github.com/GoogleCloudPlatform/generative-ai/issues/694

I believe that grounding isn't currently supported for Vertex AI Search data stores that use Chunking Modes

takes 20mins to import data to search app