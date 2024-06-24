# NotebookML

!!! abstract "Overview"

    LLMs change the information retrieval paradigm. Instead of searching for information where **we go to the information**, we can chat with our documents and ask questions of them, so that **the information comes to us** in the form of an answer. 

    In this chapter, we'll use [NotebookLM](https://notebooklm.google.com/) to quickly and easily build such a system.



## [NotebookLM](https://notebooklm.google.com/)


!!! quote
    [NotebookLM](https://notebooklm.google.com/) lets you read, take notes, ask questions, organize your ideas, and much more -- all with the power of Google AI helping you at every step of the way.

!!! quote
    It runs on the company’s Gemini 1.5 Pro model, the same AI that powers the Gemini Advanced chatbot. 
    ([ref](https://www.techradar.com/computing/artificial-intelligence/googles-notebooklm-is-now-an-even-smarter-assistant-and-better-fact-checker))

### Document Loading

Documents are loaded via GoogleDrive, PDFs, Text files, Copied text, Web page URL.

!!! tip 
    Any sources can be used e.g. Books in PDF format, websites, text files.

    Using a file of site content (if available) e.g.a PDF, is generally more reliable than using a URL to that site; it ensures all the content is ingested.

### Closed System

These documents become the corpus where information is retrieved from, with references to the document(s) the information was retrieved from.

!!! quote
    “NotebookLM is a closed system.” This means the AI won’t perform any web searches beyond what you, the user, give it in a prompt. Every response it generates pertains only to the information it has on hand.
    ([ref](https://www.techradar.com/computing/artificial-intelligence/googles-notebooklm-is-now-an-even-smarter-assistant-and-better-fact-checker))


### Sharing
Unlike Google Docs, it is not possible to share a NotebookLM publicly - sharing is done directly via email addresses.

## References

1. https://www.techradar.com/computing/artificial-intelligence googles-notebooklm-is-now-an-even-smarter-assistant-and-better-fact-checker
2. https://www.kdnuggets.com/using-google-notebooklm-for-data-science-a-comprehensive-guide
3. https://www.computerworld.com/article/1611774/google-notebooklm-generative-ai-notes-app.html



  

  
