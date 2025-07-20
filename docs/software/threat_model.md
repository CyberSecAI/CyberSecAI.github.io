# AI-Powered Threat Modeling for Secure System Design

!!! abstract "Overview"

    This section covers AI-powered threat modeling for secure system design, focusing on open-source tools and prompt-based solutions. Below is a comparison of features across notable open-source tools that assist in early design-time threat modeling.

## Open Source Tools Comparison

Comparison of features and capabilities of open-source AI-driven threat modeling tools (focused on early design-phase usage, except AI Security Analyzer which also supports code-level analysis).

| **Tool**                 | **Focus & Approach**                                                                                                                                                                                                                                          | **Key Features**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **AI / Model Integration**                                                                                                                                                                                                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **AWS Threat Designer**  | Design-phase **automated** threat modeling; Web UI (AWS Cloud stack). Users upload system architecture info (including diagrams) to generate threat models.                                                                                                   | – **Architecture diagram analysis:** Multi-modal LLM analyzes system diagrams to identify components and relationships.<br>– **Threat catalog:** Generates a comprehensive list of potential threats with interactive filtering and refinement.<br>– **Iterative replay:** Allows rerunning the model after design changes to see updated risk postures.<br>– **Exports & history:** Supports exporting results to PDF/DOCX and browsing past models in a catalog.                                                                                                                                                                                                                                                                   | Uses AWS Bedrock with large models (Anthropic Claude 4 Sonnet by default) for NLP and vision; serverless backend. Multimodal **LLM** interprets text and diagrams to generate threats.                                                                                                                 |
| **AWS Threat Composer**  | Design-phase **guided** threat modeling; Web app or VS Code extension. Emphasizes manual brainstorming with structured guidance (“threat model as code”).                                                                                                     | – **Data capture:** Records system description, architecture and dataflow diagrams, assumptions, etc., as part of the model.<br>– **Threat grammar:** Uses a prescriptive template to iteratively craft threat statements (with examples and suggestions) instead of starting from scratch.<br>– **Insights dashboard:** Highlights gaps like threats without mitigations, unprioritized threats, category coverage, etc., to answer “did we do enough?”.<br>– **Packs & export:** Supports reusable threat/mitigation packs for bulk addition (in self-hosted mode), and can generate a consolidated threat model document.                                                                                                         | No built-in generative model – focuses on human-driven input with static guidance. *(Uses local storage; no data leaves the browser. “Threat Grammar” framework provides structure rather than AI generation.)*                                                                                        |
| **StrideGPT**            | Design-phase **automated** STRIDE threat modeling; Streamlit web app or Docker CLI. Given an app description (and optionally diagrams or repo link), it auto-generates a full threat model.                                                                   | – **STRIDE threats generation:** Uses LLM to output threats categorized by STRIDE (Spoofing, Tampering, etc.) for the provided system description.<br>– **Risk & mitigations:** Automatically provides DREAD risk scores and suggests mitigation steps for each identified threat.<br>– **Attack trees & tests:** Produces potential attack paths (attack trees) and even Gherkin-style security test cases based on threats.<br>– **Multi-modal input:** Can accept architecture diagrams or flowcharts for analysis with vision-capable models; also can analyze a project’s repository (e.g. README) to enrich the threat model.<br>– **No data retention:** Does not store inputs or results on the server, focusing on privacy. | Supports multiple **LLMs** via API or local runtime: OpenAI GPT-4 (and newer GPT-4.1), Anthropic Claude 3/4, Google Gemini (2.0/2.5) and others. Also compatible with self-hosted local models (Ollama, LM Studio). This flexible backend allows using the best available model for analysis.          |
| **AI Security Analyzer** | Code-centered **security analyzer** with threat modeling output; CLI tool (Python) that scans an existing codebase to produce security documentation. Geared toward integrating threat modeling in later stages (after code exists) as well as design review. | – **Multi-faceted analysis:** Generates a *Security Design Review* document which includes threat modeling, attack surface analysis, attack trees, mitigation strategies, and identified vulnerabilities.<br>– **Code-aware threat identification:** Parses project source code (multiple languages: Python, Java, JavaScript, Go, Android, etc.) to find assets, entry points, and potential threats specific to the implementation.<br>– **Automated documentation:** Outputs comprehensive Markdown reports (e.g. `security_design.md`) that consolidate the security findings and model.<br>– **Flexible deployment:** Can run via Python (Poetry) or Docker; cross-platform support (Windows, MacOS, Linux).                    | Leverages **LLMs** to analyze code and generate text. Supports multiple model providers: OpenAI API (GPT-4 family), Anthropic (Claude), Google PaLM/Gemini via API, and OpenRouter. The user supplies an API key for the chosen model, and the tool orchestrates prompts to produce the security docs. |



## Open Source Tools Details


### AWS Threat Designer

AWS Threat Designer: AI-powered threat modeling for secure system design.

- See blogpost: [Accelerate threat modeling with generative AI](https://aws.amazon.com/blogs/machine-learning/accelerate-threat-modeling-with-generative-ai/) for an in-depth overview of the solution.


!!! quote

    Effective threat modeling examines data flows, trust boundaries, and potential attack vectors to create a comprehensive security strategy tailored to the specific system.

    In a shift-left approach to security, threat modeling serves as a critical early intervention. By implementing **threat modeling during the design phase—before a single line of code is written**—organizations can identify and address potential vulnerabilities at their inception point. 

    AWS [Accelerate threat modeling with generative AI](https://aws.amazon.com/blogs/machine-learning/accelerate-threat-modeling-with-generative-ai/), JUN 2025 



Each function generates specialized prompts for different phases of the threat modeling process, including:

- Asset identification
- Data flow analysis
- Gap analysis
- Threat identification and improvement
- Response structuring

https://github.com/awslabs/threat-designer/tree/main?tab=readme-ov-file#prerequisites

The backend is written in python: threat-designer/backend/threat_designer/

The associated prompts are https://github.com/awslabs/threat-designer/blob/0554b6a97c08e38bb92504ba13768780adb0301f/backend/threat_designer/prompts.py


#### AWS Threat Composer

A simple threat modeling tool to help humans to reduce time-to-value when threat modeling
https://github.com/awslabs/threat-composer#readme



### STRIDE GPT

!!! quote

    Features:

    - Simple and user-friendly interface
    - Generates threat models based on the STRIDE methodology
    - Multi-modal: Use architecture diagrams, flowcharts, etc. as inputs for threat modelling across all supported vision-capable models
    - Generates attack trees to enumerate possible attack paths
    - Suggests possible mitigations for identified threats
    - Supports DREAD risk scoring for identified threats
    - Generates Gherkin test cases based on identified threats
    - GitHub repository analysis for comprehensive threat modelling
    - No data storage; application details are not saved
    - Supports models accessed via OpenAI API, Azure OpenAI Service, Google AI API, Mistral API, or locally hosted models via Ollama and 🆕 LM Studio Server
    - Available as a Docker container image for easy deployment
    - Environment variable support for secure configuration 

    https://github.com/mrwadams/stride-gpt


The app https://stridegpt.streamlit.app/ has these tabs

- [Threat Model](https://github.com/mrwadams/stride-gpt/blob/master/threat_model.py)
- [Attack Tree](https://github.com/mrwadams/stride-gpt/blob/master/attack_tree.py)
- [Mitigations](https://github.com/mrwadams/stride-gpt/blob/master/mitigations.py)
- [DREAD](https://github.com/mrwadams/stride-gpt/blob/master/dread.py)
- [Test Cases](https://github.com/mrwadams/stride-gpt/blob/master/test_cases.py)

It supports a Bring Your Own LLM Key i.e. you chose the LLM and provide your API key.


### AI Security Analyzer

!!! quote

    AI Security Analyzer is a Python-based tool that analyzes your project's codebase and automatically generates detailed security documentation. It supports multiple analysis types:

    - 🔒 Security Design Documentation
    - 🎯 Threat Modeling
    - 🔍 Attack Surface Analysis
    - 🌳 Attack Tree Analysis
    - 🛡️ Mitigation Strategies
    - 🐛 Vulnerabilities

    https://github.com/xvnpw/ai-security-analyzer


    generate four different types of security documents:

     -  🔒 Security Design Documentation: Generating detailed security design review.
     -  🎯 Threat Modeling: Performing threat modeling analysis.
     -  🔍 Attack Surface Analysis: Identifying potential entry points and vulnerabilities in the project’s attack surface.
     -  🌳 Attack Tree Analysis: Visualizing potential attack vectors and their hierarchies through attack tree.


    https://xvnpw.github.io/posts/scaling-threat-modeling-with-ai/


The associated prompts are 

- https://github.com/xvnpw/ai-security-analyzer/blob/dabfc57b6e5da9d99b3df5229fd496a224dac862/ai_security_analyzer/prompts.py




## Additional Prompt Resources

Beyond full tools, there are also open-source prompt libraries focused on security threat modeling:

* **Fabric by Daniel Miessler:** A crowdsourced collection of AI prompt “patterns.” It includes a [create_stride_threat_model](https://github.com/danielmiessler/Fabric/blob/main/data/patterns/create_stride_threat_model/system.md) pattern to guide an LLM in producing a STRIDE-based threat model from a system description and a [create_threat_scenarios](https://github.com/danielmiessler/Fabric/blob/main/data/patterns/create_threat_scenarios/system.md) pattern for generating detailed attack scenarios. These patterns can be used with various GPT-based systems to jump-start threat modeling exercises.
* **Kornelius Security Audit Prompt:** An [open prompt](https://github.com/scragz/kornelius/blob/main/prompts/audit/security.prompt) (from the Kornelius project) that provides a template for security auditing via LLMs. This prompt script can be adapted to evaluate a system’s security posture by enumerating threats and checks.

Each of the above resources provides ready-made prompt structures that practitioners can use with their AI of choice to conduct threat modeling, complementing the dedicated tools compared in the table.

