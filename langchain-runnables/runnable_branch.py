from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableBranch,
    RunnableLambda,
    RunnablePassthrough,
    RunnableSequence,
)
from langchain_groq import ChatGroq
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}", input_variables=["text"]
)

model = ChatGroq(model="openai/gpt-oss-120b")

parser = StrOutputParser()

report_gen_chain = prompt1 | model | parser

# branch_chain = RunnableBranch(
#     (lambda x: len(x.split()) > 300, prompt2 | model | parser), RunnablePassthrough()
# )  # you send tuples i.e conditions inside the RunnableBranch

branch_chain = RunnableBranch(
    (
        lambda x: len(x.split()) > 300,
        RunnableLambda(lambda x: {"text": x}) | prompt2 | model | parser,
    ),
    RunnablePassthrough(),
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

console = Console()

console.print(Markdown(final_chain.invoke({"topic": "Russia vs Ukraine"})))

# RunnableSequence = LCEL (lang chain expression langauge) trigger by |
