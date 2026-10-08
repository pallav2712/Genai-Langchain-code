from dotenv import load_dotenv
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq

load_dotenv()  # .env se GROQ_API_KEY load karta hai

model = ChatGroq(
    model="openai/gpt-oss-120b"
)  # model name Groq console ke models page se verify kar lena

chat_history: list[BaseMessage] = [SystemMessage("You are an AI assistant")]

while True:

    user_input = input("You: ")

    if user_input.strip().lower() == "exit":
        break

    # result = model.invoke(chat_history)
    # chat_history.append(result.content)
    # print("AI: ",result.text)

    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)
