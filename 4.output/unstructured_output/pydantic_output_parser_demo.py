from langchain_openai import ChatOpenAI  # also work with hugging face api
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
load_dotenv()

model = ChatOpenAI(
  model="openai/gpt-3.5-turbo",
  base_url="https://openrouter.ai/api/v1"
)

class Person(BaseModel):
  name : str = Field(description='Name of the person')
  age :  int = Field(gt=18, description = 'Age of the person')
  city : str = Field(description='name of the city the person belongs to')


parser = PydanticOutputParser(pydantic_object=Person)
template = PromptTemplate(
  template = 'Generate the name , age and city of a fictional {place} person \n {format_instruction}',
  input_variables=['place'],
  partial_variables={'format_instruction':parser.get_format_instructions()}
)


# prompt = template.invoke({'place' : 'england'})

# print(prompt) ## very mess parser make it parse and format

# result = model.invoke(prompt)

chain = template |model |parser
# final_result = parser.parse(result.content)

final_result = chain.invoke({'place' : 'england'})
print(final_result)