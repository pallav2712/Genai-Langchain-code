from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

load_dotenv()


llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs=dict(
        do_sample=True,
        temperature=0.5,
        max_new_tokens=250,
        return_full_text=False,
    ),
)  # type: ignore

model = ChatHuggingFace(llm=llm)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. \n {text}",
    input_variables=["text"],
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser  # type: ignore

result = chain.invoke({"topic": "black hole"})

print(result)

# Parser -> StrOutputParser
# Reason: model ka output AIMessage object hota hai, plain string nahi.
# Agla stage (template2) ko text chahiye, poora AIMessage object nahi.
# Agar parser nahi lagayenge, to AIMessage seedha template2 mein jaayega
# aur prompt mein content + metadata ka kachra (jaise "content='...' additional_kwargs=...") aa sakta hai,
# ya type mismatch ka error aayega.
# Parser sirf .content nikaal ke clean string deta hai, taaki chain ka agla step sahi chale.

 