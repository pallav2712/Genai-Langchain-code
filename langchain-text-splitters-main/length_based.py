from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader(
    "/home/mrrobot/projects/genai-langchain-code/langchain-text-splitters-main/dl-curriculum.pdf"
)

docs = loader.load()

for d in docs:
    d.page_content = " ".join(d.page_content.split())


splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0, separator="")

result = splitter.split_documents(docs)

print(result[1])

# print(result)
