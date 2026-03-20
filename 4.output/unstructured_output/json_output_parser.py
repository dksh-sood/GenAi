from langchain_openai import ChatOpenAI  # also work with hugging face api
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatOpenAI(
  model="openai/gpt-3.5-turbo",
  base_url="https://openrouter.ai/api/v1"
)

parser = JsonOutputParser()

template = PromptTemplate(
  template= 'give me the name , age and city of a fictional person \n {format_instruction}',  # It automatically fills {format_instruction} before runtime.
  input_variables=[],
  partial_variables={'format_instruction':parser.get_format_instructions()}  # fail before runtime
)

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = template | model | parser

result = chain.invoke({})

# print(final_result)
# print(type(final_result))

print(result)