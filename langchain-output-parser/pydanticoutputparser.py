from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from pydantic import BaseModel, Field

load_dotenv()

# Define the model
llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs=dict(
        do_sample=True,
        temperature=0.5,
        max_new_tokens=250,
        return_full_text=False,
    ),  # inference parameters/ hyper parameter
)

model = ChatHuggingFace(llm=llm)


class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="Name of the city the person belongs to")


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template=(
        "Generate a fictional person from {place}. "
        "Give a realistic first and last name, an age above 18, and their city.\n"
        "{format_instruction}"
    ),
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = template | model | parser

final_result = chain.invoke({"place": "sri lankan"})

# prompt = template.invoke({"place": "pakistan"})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)  # type: ignore

print(final_result)

# print(prompt)
