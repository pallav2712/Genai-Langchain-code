from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

vector = embedding.embed_documents(documents)

print(len(vector))        # 3 (documents ki count)
print(len(vector[0]))     # 384 (dimensions)
print(vector[0][:5])      # pehle 5 numbers

print(str(vector))