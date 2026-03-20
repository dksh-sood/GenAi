from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
  template = 'generate 5 intresting facts about {topic}',
  input_variables=['topic']
)


model = ChatOpenAI(
  model="openai/gpt-3.5-turbo",
  base_url="https://openrouter.ai/api/v1"
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

# print(result)

chain.get_graph().print_ascii()  # get the chain flow