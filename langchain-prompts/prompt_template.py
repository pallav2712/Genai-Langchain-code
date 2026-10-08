from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

# detailed way
template2 = PromptTemplate(
    template="Greet this person in 5 languages. The name of the person is {name}",
    input_variables=["name"],
)

# fill the values of the placeholders
prompt = template2.invoke({"name": "pallav"})

result = model.invoke(prompt)

print(result.content)
