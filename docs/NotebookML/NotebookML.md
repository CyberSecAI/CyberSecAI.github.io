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

!!! quote 
    
    **“source-grounded AI”**: you define a set of documents that are important to your work—called “sources” in the NotebookLM parlance—and from that point on, you can have an open-ended conversation with the language model where its answers will be “grounded” in the information you’ve selected. It is as if you are giving the AI instant expertise in whatever domain you happen to be working in. ([ref](https://adjacentpossible.substack.com/p/introducing-notebooklm))

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

### How To Use NotebookLM


<iframe width="560" height="315" src="https://www.youtube.com/embed/iWPjBwXy_Io?si=0Z0e0u_ni0R4tAM-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## References

1. [Introducing NotebookLM](https://adjacentpossible.substack.com/p/introducing-notebooklm), Oct 19, 2023, Steven Johnson who contributed to NotebookLM
2. [Getting The Most Out Of Notes In NotebookLM](https://medium.com/@stevenbjohnson/getting-the-most-out-of-notes-in-notebooklm-d9d70316b780), Mar 18, 2024, Steven Johnson
3. [How To Use NotebookLM As A Research Tool](https://stevenberlinjohnson.com/how-to-use-notebooklm-as-a-research-tool-6ad5c3a227cc), Feb 19, 2024, Steven Johnson
4. [Google's NotebookLM is now an even smarter assistant and better fact-checker](https://www.techradar.com/computing/artificial-intelligence/googles-notebooklm-is-now-an-even-smarter-assistant-and-better-fact-checker), June 7, 2024 
5. [Using Google’s NotebookLM for Data Science: A Comprehensive Guide](https://www.kdnuggets.com/using-google-notebooklm-for-data-science-a-comprehensive-guide), Dec 7, 2023 
6. [How to use Google’s genAI-powered note-taking app](https://www.computerworld.com/article/1611774/google-notebooklm-generative-ai-notes-app.html), Feb 15, 2024 



## Takeaways
  
!!! success "Takeaways" 

    1. 

  
