from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='/home/mrrobot/projects/genai-langchain-code/langchain-document-loaders-main/Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])