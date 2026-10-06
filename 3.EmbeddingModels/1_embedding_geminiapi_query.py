from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=32)

result = embedding.embed_query("Delhi is the capital of India")

print(len(result))
print(str(result))
