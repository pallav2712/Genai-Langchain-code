from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableSequence,
)
from langchain_groq import ChatGroq
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

model = ChatGroq(model="openai/gpt-oss-120b")

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}", input_variables=["text"]
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explanation": RunnableSequence(prompt2, model, parser),
    }
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "cricket"})



console = Console()

console.print("Joke: ", result["joke"])

print("---------------------------")

console.print("Explanation: ", Markdown(result["explanation"]))

# with open('output.md', "w", encoding="utf-8") as f:
#     f.write(result['explanation'])


# runnable passthrough: returns the same input as output
