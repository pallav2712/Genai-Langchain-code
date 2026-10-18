from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='/home/mrrobot/projects/genai-langchain-code/langchain-document-loaders-main/books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)

# print(len(docs))

# print(docs[0].page_content)
# print(docs[0].metadata)


# load(): Eager loading — loads all documents into memory at once
# and returns them as a list. Suitable when all documents are
# needed immediately, but may consume more memory for large datasets.
# Use when the dataset is small or all documents are needed upfront.


# lazy_load(): Lazy loading — yields documents one at a time as they
# are requested during iteration, instead of loading all documents
# upfront. Useful for processing large datasets with lower memory usage.
# Use when processing large collections (e.g., 500 PDFs) sequentially to help reduce memory usage.
