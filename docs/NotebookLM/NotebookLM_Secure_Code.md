# NotebookLM Secure Code

!!! abstract "Overview"

    In two separate conversations recently, the topic of using LLMs for secure coding came up.
    One of the concerns that is often raised is that GenAI Code is not secure because GenAI is trained on arbitrary code on the internet.

    I was curious how NotebookLM would work for generating or reviewing secure code i.e. A closed system that has been provide a lot of guidance on secure code (and not arbitrary examples).

    Claude Sonnet 3.5 was also used for comparison.

## Vulnerability Types

[Secure Programming with Static Analysis](http://www.amazon.com/Secure-Programming-Static-Analysis-Brian/dp/0321424778/ref=sr_1_1?s=books&ie=UTF8&qid=1345459967&sr=1-1&keywords=Secure+Programming+with+Static+Analysis), classifies vulnerability types as follows:

<figure markdown>
![](../assets/images/Secure_programming_with_Static_Analysis.png)
</figure>

LLMs go beyond understanding syntax to understanding semantics and may be effective in the 3 quadrants that traditional static analysis isn't.

But in this simple test case below, the focus is on Generic defects visible in the code, as an initial proof of concept.

## Data Sources

Two books I had on Java were loaded to NotebookLM:

1. [The CERT Oracle Secure Coding Standard for Java](https://www.informit.com/store/cert-oracle-secure-coding-standard-for-java-9780321803955)
    1. The same material is available on https://wiki.sei.cmu.edu/confluence/display/java/SEI+CERT+Oracle+Coding+Standard+for+Java
1. [Java Coding Guidelines: 75 Recommendations for Reliable and Secure Programs](https://www.informit.com/store/java-coding-guidelines-75-recommendations-for-reliable-9780133439519)


### Test Data

NIST [Software Assurance Reference Dataset (SARD)](https://samate.nist.gov/SARD/) was used as the test dataset.

!!! quote
    The [Software Assurance Reference Dataset (SARD)](https://samate.nist.gov/SARD/) is a growing collection of test programs with documented weaknesses. Test cases vary from small synthetic programs to large applications. The programs are in C, C++, Java, PHP, and C#, and cover over 150 classes of weaknesses.

e.g. CWE: 191 Integer Underflow https://samate.nist.gov/SARD/test-cases/252126/versions/1.0.0#4


## Setup
1. Import both PDFs into a new NotebookLM.

## Test

### Test Code CWE: 191 Integer Underflow 

<figure markdown>
![](../assets/images/sard_cwe-191.png)
https://samate.nist.gov/SARD/test-cases/252126/versions/1.0.0#4
</figure>


### Review Test Code

Comments are removed from https://samate.nist.gov/SARD/test-cases/252126/versions/1.0.0#4 so the code fits in the prompt window.

<figure markdown>
![](../assets/images/java_review.png)
</figure>

#### Claude 3.5 
<figure markdown>
![](../assets/images/java_review_claude.png)
</figure>



### Generate Code: Write Secure Code to Multiply 2 numbers 


<figure markdown>
![](../assets/images/java_mult.png)
</figure>

#### Use BigInteger Instead

<figure markdown>
![](../assets/images/java_bigint.png)
</figure>


#### Claude 3.5 

<figure markdown>
![](../assets/images/java_claude.png)
</figure>
<figure markdown>
![](../assets/images/java_claude_bigint.png)
</figure>

## Takeaways
  
!!! success "Takeaways" 

    1. NotebookLM with 2 Secure Code Java references performed well in these simple test cases.