from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite",temperature=0.5)

# temperature se control hota hai ki model ka output kitna random/creative ho.
# Low (0 - 0.3): focused aur consistent, facts, code aur RAG ke liye best.
# High (0.8+): zyada varied aur creative, story aur brainstorming ke liye best.

result = model.invoke("Write a 5 line poem on cricket")

print(result.text)
