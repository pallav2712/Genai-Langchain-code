from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs=dict(
        do_sample=True,
        temperature=0.5,
        max_new_tokens=250,
        return_full_text=False,
    ),
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me 5 facts about {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

def clean_facts(result):
    cleaned = []
    for item in result["facts"]:
        if isinstance(item, dict):
            cleaned.append(item.get("description") or item.get("name"))
        else:
            cleaned.append(item)
    return cleaned


chain = template | model | parser | clean_facts

result = chain.invoke({"topic": "Death"})

print(result)
