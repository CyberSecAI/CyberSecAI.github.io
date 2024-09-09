
# Agents



## Why Agents?

[Why agents are the next frontier of generative AI, July 2024](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/why-agents-are-the-next-frontier-of-generative-ai)




!!! quote "Using Agents can significantly improve performance"
   
    <figure markdown>
    ![](../assets/images/agents.webp)
    </figure>


    GPT-3.5 (zero shot) was 48.1% correct. GPT-4 (zero shot) does better at 67.0%. However, the improvement from GPT-3.5 to GPT-4 is dwarfed by incorporating an iterative agent workflow. Indeed, wrapped in an agent loop, GPT-3.5 achieves up to 95.1%.
     https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance

    An agentic workflow in which the LLM is prompted to focus on one thing at a time can give better performance.
    https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/

!!! quote "Agentic AI Design Patterns"
    1. **[Reflection](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection?ref=dl-staging-website.ghost.io)**: The LLM examines its own work to come up with ways to improve it. 
    2. **[Tool Use](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use)**: The LLM is given tools such as web search, code execution, or any other function to help it gather information, take action, or process data.
    3. **[Planning](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/?ref=dl-staging-website.ghost.io)**: The LLM comes up with, and executes, a multistep plan to achieve a goal (for example, writing an outline for an essay, then doing online research, then writing a draft, and so on).
    4. **[Multi-agent collaboration](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/?ref=dl-staging-website.ghost.io)**: More than one AI agent work together, splitting up tasks and discussing and debating ideas, to come up with better solutions than a single agent would.

    https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance


!!! quote "Reflection using a multi-agent framework" 
    Further, we can implement Reflection using a multi-agent framework. I've found it convenient to create two different agents, one prompted to generate good outputs and the other prompted to give constructive criticism of the first agent's output. The resulting discussion between the two agents leads to improved responses.

    https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/


    Like the design pattern of Planning, I find the output quality of multi-agent collaboration hard to predict, especially when allowing agents to interact freely and providing them with multiple tools. The more mature patterns of Reflection and Tool Use are more reliable.
    
    https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/