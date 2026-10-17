from langchain_community.document_loaders import PyPDFLoader

# PyPDFLoader only used for converting the textual pdf , not the others
# like the picture based pdf

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)


print("-----------------The End-------------------")

# from dotenv import load_dotenv
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate
# from langchain_groq import ChatGroq

# load_dotenv()

# model = ChatGroq(model="openai/gpt-oss-120b")

# prompt = PromptTemplate(
#     template="""
#     Organize the following PDF text into a readable,
#     well-structured text format.

#     Preserve headings, paragraphs, numbering, and bullet points.
#     Do not add information that is not present.

#     PDF metadata:
#     {metadata}

#     PDF text:
#     {text}
#     """,
#     input_variables=["text", "metadata"],
# )

# parser = StrOutputParser()

# loader = PyPDFLoader("dl-curriculum.pdf")
# docs = loader.load()

# chain = prompt | model | parser

# result = chain.invoke({"text": docs[0].page_content, "metadata": docs[0].metadata})

# print(result)

# print(docs[0].metadata)