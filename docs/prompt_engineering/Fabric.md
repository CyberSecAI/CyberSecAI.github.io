# Fabric

!!! abstract "Overview"

     One of Fabric's primary features is helping people collect and integrate prompts



## Fabric Prompt Collection and Framework

https://github.com/danielmiessler/fabric/tree/main 

!!! quote
    Since the start of 2023 and GenAI we've seen a massive number of AI applications for accomplishing tasks. It's powerful, but it's not easy to integrate this functionality into our lives.

    In other words, AI doesn't have a capabilities problem—it has an integration problem.
    Fabric was created to address this by enabling everyone to granularly apply AI to everyday challenges.

    One of fabric's primary features is helping people collect and integrate prompts, which we call Patterns, into various parts of their lives.

The prompts (aka Patterns) are available at https://github.com/danielmiessler/fabric/tree/main/patterns


### Fabric Prompts for CyberSecurity

Fabric has Prompts that are specific to CyberSecurity e.g.

* https://github.com/danielmiessler/fabric/blob/main/patterns/create_threat_model/system.md
* https://github.com/danielmiessler/fabric/blob/main/patterns/analyze_logs/system.md
* https://github.com/danielmiessler/fabric/blob/main/patterns/analyze_malware/system.md
* https://github.com/danielmiessler/fabric/blob/main/patterns/analyze_threat_report/system.md
* https://github.com/danielmiessler/fabric/blob/main/patterns/analyze_threat_report_trends/system.md
* https://github.com/danielmiessler/fabric/blob/main/patterns/write_hackerone_report/system.md
* https://github.com/danielmiessler/fabric/blob/main/patterns/write_semgrep_rule/system.md 

### Fabric Prompt to Improve Prompts 
https://github.com/danielmiessler/fabric/blob/main/patterns/improve_prompt/system.md

### Fabric Extract Wisdom

We'll take [Goldman Sachs, Top of Mind, Gen AI: Too Much Spend, Too Little Benefit?](https://www.goldmansachs.com/intelligence/pages/gs-research/gen-ai-too-much-spend-too-little-benefit/report.pdf), June 2024 as the example content to extract wisdom from. It's a 30 page report that is dense and varied.

Below the summary by Claude 3.5 Sonnet using the [extract_article_wisdom prompt](https://github.com/danielmiessler/fabric/blob/main/patterns/extract_article_wisdom/system.md).   


````
SUMMARY
Goldman Sachs analyzes AI's economic impact, discussing potential benefits, challenges, and investment implications in their "Top of Mind" report.

IDEAS

AI could increase US productivity by 9% and GDP growth by 6.1% over the next decade.
The current AI investment boom may be unsustainable, with potential for a market correction.
Power demand from AI data centers could lead to a significant energy crunch in the coming years.
AI's economic impact may be more limited than many expect, with only 4.6% of tasks potentially automated within a decade.
The semiconductor industry faces supply constraints that could limit AI growth in the near term.
Utilities companies are emerging as unexpected beneficiaries of the AI boom due to increased power demand.
AI technology may struggle to replicate human cognitive abilities, limiting its transformative potential.
The cost of AI infrastructure is currently high, raising questions about return on investment.
AI's impact on corporate profitability will be crucial for long-term equity returns.
The AI theme in the stock market may have room to run despite recent gains.
Data centers could consume up to 8% of total US power demand by 2030.
AI development is outpacing the ability of power infrastructure to support it.
The US may struggle to build the necessary infrastructure to support AI growth.
AI spending by tech giants is not seen as irrational exuberance by some analysts.
The AI investment cycle is still in the infrastructure buildout phase, with applications yet to emerge.
European power demand could increase by 40-50% over the next decade due to AI and electrification.
AI data centers can consume up to 10 times more energy than traditional data centers.
The US utility industry has not experienced significant load growth in almost two decades.
AI chip demand is outstripping supply, particularly for High-Bandwidth Memory technology.
The pace of AI model improvements may be slower than many anticipate.

QUOTES

"Given the focus and architecture of generative AI technology today... truly transformative changes won't happen quickly and few—if any—will likely occur within the next 10 years." - Daron Acemoglu
"AI technology is exceptionally expensive, and to justify those costs, the technology must be able to solve complex problems, which it isn't designed to do." - Jim Covello
"Spending is certainly high today in absolute dollar terms. But this capex cycle seems more promising than even previous capex cycles." - Kash Rangan
"The devil is ultimately in the details. So, I don't have a strong prior as to how much of the current investment boom will be wasted vs. productive. But I expect both will happen." - Daron Acemoglu
"Until we reach a level of saturation in terms of human capacity to consume data, any amount of efficiency gains will undoubtedly be gobbled up by even more demand." - Brian Janous
"The risk that our children or grandchildren in 2074 accuse us of moving too slowly in 2024 at the expense of growth seems far lower than the risk that we end up moving too quickly and destroy institutions, democracy, and beyond in the process." - Daron Acemoglu
"I'm loathe to use the word 'bubble' because I don't believe that AI is a bubble, but most bubbles in history ended either because the cost of capital changed dramatically or end-demand deteriorated and affected companies' ability to deploy capital, not because companies retreated from investing in a technology where the payoff was taking longer than expected." - Eric Sheridan
"Utilities have not experienced a period of load growth in almost two decades and are not prepared for—or even capable of matching—the speed at which AI technology is developing." - Brian Janous
"The US has unfortunately lost the ability to build large infrastructure projects—this is a task better suited for 1930s America, not 2030s America." - Brian Janous
"Every human invention should be celebrated, and generative AI is a true human invention. But too much optimism and hype may lead to the premature use of technologies that are not yet ready for prime time." - Daron Acemoglu

FACTS

Data centers currently account for only about 1% of global power demand.
The US utility industry has not experienced significant load growth in almost two decades.
60% of workers today are employed in occupations that did not exist in 1940.
The US corporate profit share of GDP is near its highest levels since World War II.
Northern Virginia is home to the most data centers in the US.
Commercial power consumption in Virginia rose 37% from 2016 to 2023.
AI data centers can consume up to 10 times more energy than traditional data centers.
The average power usage effectiveness (PUE) of cloud data centers declined by only 0.2 over the course of a decade.
Wait times for power projects to connect to the grid currently range from 40-70 months.
The High-Bandwidth Memory market is expected to grow at a ~100% compound annual growth rate over the next few years.
The S&P 500 Shiller P/E ratio is currently in the 97th percentile since 1900.
Utilities returned 16% between March and May, making them the best-performing sector in the S&P 500.
European electricity consumption has declined by around 10% from its 2008 peak.
TSMC's Chip-on-Wafer-on-Substrate packaging capacity is expected to more than double in 2024.
The US is expected to add nearly 800 gigawatts of wind and solar over the coming 10-15 years.

REFERENCES

ChatGPT
Global Macro Research by Goldman Sachs
MIT's Daron Acemoglu's research
Jim Covello's analysis
Joseph Briggs' economic forecasts
Kash Rangan and Eric Sheridan's market analysis
Brian Janous' insights on power infrastructure
Carly Davenport's utility sector analysis
Toshiya Hari, Anmol Makkar, and David Balaban's semiconductor industry research
Ryan Hammond's equity market analysis
Christian Mueller-Glissmann's long-term return forecasting framework
Alberto Gandolfi's European utilities analysis
Hongcen Wei's power consumption analysis
David Autor's research on technological innovation and employment
Robert Shiller's P/E ratio data
EIA (Energy Information Administration) data
Census Bureau data
FactSet financial data
TSMC's capacity projections
REPowerEU Plan

RECOMMENDATIONS

Investors should remain invested in AI infrastructure providers despite high valuations.
Utilities companies should find ways to extract more efficiencies from the current power system.
Policymakers should focus on investing in America's transmission infrastructure.
Companies should tie AI spending to visible revenue growth to maintain investor confidence.
Investors should consider "Electrification Compounders" in the utilities sector as potential beneficiaries of AI growth.
The US should prioritize expanding long-duration energy storage to meet growing power demand.
Tech companies should prepare for potential power constraints when planning AI infrastructure.
Investors should monitor the emergence of AI's "killer application" as a sign of the technology's maturity.
Policymakers should address regulatory lags and interconnection constraints in the power sector.
Companies should be cautious about premature use of AI technologies that are not yet fully developed.
Investors should watch for signs of corporate profitability decline as a potential trigger for reduced AI spending.
The semiconductor industry should focus on expanding High-Bandwidth Memory and advanced packaging capacity.
Utilities should prepare for a potential doubling of grid capacity in some regions over the next decade.
Investors should consider the impact of AI on corporate profitability when assessing long-term equity returns.
Policymakers should balance the need for AI innovation with potential risks to institutions and democracy.
````

### Process Youtube Transcripts

Fabric, and LLMs in general, can process Youtube Transcripts (which are text).

The Youtube Transcript for a video can be retrieved in different ways e.g. https://www.youtube.com/watch?v=oMZN810xfck:

* Click the Transcript button under a video and copy and paste, or download, to a text file
* Use Fabric helper function: [installer/client/cli/yt.py](https://github.com/danielmiessler/fabric/blob/main/installer/client/cli/yt.py) (or other tool)

````
yt --transcript https://www.youtube.com/watch?v=oMZN810xfck
````
The text can then be processed with an LLM.

This download and processing can be done in one command with Fabric
````
yt --transcript https://www.youtube.com/watch?v=oMZN810xfck | fabric -sp extract_wisdom
````
where

* -s is for streaming
* -p is for pattern
* [extract_wisdom](https://github.com/danielmiessler/fabric/tree/main/patterns/extract_wisdom) is the Fabric prompt that extracts wisdom from any text. It addresses the problem of too much content and too little time.



## Takeaways
  
!!! success "Takeaways" 

    1. Fabric is a good resource for prompts with many being related to CyberSecurity.
  
