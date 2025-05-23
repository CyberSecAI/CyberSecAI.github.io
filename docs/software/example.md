---
icon: material/play-box-edit-outline 
---

# Example

Research
Requirements
ADRs
Code Reviews


GenAI to generate Acceptance Criteria in Gherkin format (BDD) based on user story description.
https://medium.com/@parserdigital/generative-ai-our-journey-into-a-custom-llm-3c09244544f0

https://andremoniy.medium.com/why-bdd-is-even-more-important-than-automated-tests-and-why-even-llms-still-need-tdd-ce57debfc700

https://kobiton.com/blog/cucumber-testing-a-key-to-generative-ai-in-test-automation/
Feature Files – Written in Gherkin, each feature file ends with the .feature extension and describes an application feature. Within each file, you can have multiple scenarios that represent different behaviors or requirements.

Scenarios – Each scenario outlines a test case using Given-When-Then steps. 


https://cucumber.io/docs/gherkin/reference/

https://cucumber.io/docs/gherkin/reference/#background
```
Feature: Multiple site support
  Only blog owners can post to a blog, except administrators,
  who can post to all blogs.

  Background:
    Given a global administrator named "Greg"
    And a blog named "Greg's anti-tax rants"
    And a customer named "Dr. Bill"
    And a blog named "Expensive Therapy" owned by "Dr. Bill"

  Scenario: Dr. Bill posts to his own blog
    Given I am logged in as Dr. Bill
    When I try to post to "Expensive Therapy"
    Then I should see "Your article was published."

  Scenario: Dr. Bill tries to post to somebody else's blog, and fails
    Given I am logged in as Dr. Bill
    When I try to post to "Greg's anti-tax rants"
    Then I should see "Hey! That's not your blog!"

  Scenario: Greg posts to a client's blog
    Given I am logged in as Greg
    When I try to post to "Expensive Therapy"
    Then I should see "Your article was published."
```


https://arxiv.org/html/2411.04284v1

