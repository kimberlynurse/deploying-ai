# Assignment 2

The goal of this assignment is to design and implement an AI system with a conversational interface.

Before you begin, keep in mind that meeting the requirements is important, but more important is that you solve the technical problems associated with the implementation. The assignment is fairly open-ended and can easily become an expansive project. My recommendation is that you implement a simplified version of the services, before moving to more complex implementation. Remember to test your code constantly.  

## Services

This implementation is based on LangGraph's tools. 

The file main.py contains the llm model calls that controls the chat. Tools are in the files tools_*.py.

### Service 1: API Calls

+ This service uses an API as its back end.
+ 'Search Recipes' (https://spoonacular.com/food-api/docs#Search-Recipes-Complex) was chosen from the list of [public and free APIs on GitHub](https://github.com/public-apis/public-apis). 
+ Additional information can be found in tools_recipes.py.
+ The tool is imported to main and included in the list `tools`.
+ The tool's node uses LangGraph's `ToolNode` class and `tools_condition` is the standard tool stopping criteria.
+ All restrictions as well as conversation style and tone requirements are in the instructions prompt. You can find this in prompts.py.

### Service 2: Semantic Query

+ This service implementation is based on our in-class Pitchfork exercise (questions are resolved through a semantic search).
+ The tool is imported from its tools_*.py file (tools_music.py).
+ A [ChromaDB instance with file persistence](https://docs.trychroma.com/docs/run-chroma/persistent-client) was used. This is similar to the first implementation used in class but smaller and easier to host than the Docker-based version.
+ All restrictions as well as conversation style and tone requirements can be found in prompts.py.

### Service 3: Function Calling 

+ This service calls the get_weather function referenced in OpenAI for developers: [Function Calling](https://platform.openai.com/docs/guides/function-calling).
+ The tool is imported from its tools_*.py file (tools_weather.py).
+ All restrictions as well as conversation style and tone requirements can be found in prompts.py.

## User Interface

+ The system includes a chat-based interface, implemented with Gradio.
+ The chat client should maintain a natural conversation style with a friendly and engaging tone.

---

## Guardrails and Other Limitations

* Guardrails have been included that prevent users from:

  * Accessing or revealing the system prompt.
  * Modifying the system prompt directly.

* The model is not allowed to respond to questions on certain restricted topics:

  * Cats or dogs
  * Horoscopes or Zodiac Signs
  * Taylor Swift

## Implementation

+ Code is implemented in the folder `./05_src/assignment_chat`.
+ This `readme.md` explains the nature of the chat client, the serivices that it provides, and any decisions made related to the implementation.
+ The standard setup of the course was used (no additional libraries are required).

---

# Submission Information

**Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

## Submission Parameters

- The Submission Due Date is indicated in the [readme](../README.md#schedule) file.
- The branch name for your repo should be: assignment-2
- What to submit for this assignment:
    + Projects files.
- What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/deploying-ai/pull/<pr_id>`
    + Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

## Checklist

+ Created a branch with the correct naming convention.
+ Ensured that the repository is public.
+ Reviewed the PR description guidelines and adhered to them.
+ Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
