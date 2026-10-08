from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)
