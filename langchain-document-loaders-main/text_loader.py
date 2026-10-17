from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

prompt = PromptTemplate(
    template="Write a summary for the following poem - \n {poem}",
    input_variables=["poem"],
)

parser = StrOutputParser()

loader = TextLoader("cricket.txt", encoding="utf-8")

docs = loader.load()   # load return type is list of document.

print(type(docs))

print(len(docs))

# print(docs)

# print(docs[0].page_content)

# print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({"poem": docs[0].page_content}))
