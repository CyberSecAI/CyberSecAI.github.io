# NotebookLM Secure Code

!!! abstract "Overview"

    In two separate conversations recently, the topic of using LLMs for secure coding came up.

    I was curious how NotebookLM would work for generating or reviewing secure code.

    Claude Sonnet 3.5 was also used for comparison.

## Data Sources

Two books I had on Java were used:

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

### Review Code

#### Claude 3.5 
### Generate Code


#### Claude 3.5 

## Takeaways
  
!!! success "Takeaways" 

    1. I 