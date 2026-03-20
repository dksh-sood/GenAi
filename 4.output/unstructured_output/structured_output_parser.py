from langchain_openai import ChatOpenAI  # also work with hugging face api
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatOpenAI(
  model="openai/gpt-3.5-turbo",
  base_url="https://openrouter.ai/api/v1"
)


schema = [
  ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
  ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
  ResponseSchema(name='fact_3', description='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
  template = 'Given 3 fact about {topic} \n {format_instruction}',
  input_variables=['topic'],
  partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'topic' : 'black hole'})
chain = template | model | parser
result = chain.invoke({'topic' : 'black hole'})

# final_result = parser.parse(result.content)

# print(final_result)

print(result)