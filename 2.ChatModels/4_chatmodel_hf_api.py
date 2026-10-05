from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen3.8-27B", task="text-generation") #type: ignore

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)
