from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
  template = 'generate a detailed report on {topic}',
  input_variables= ['topic']
)

prompt2 = PromptTemplate(
  template='generate a 5 pointer summary from the following text \n {text}',
  input_variables=['text']
)

model = ChatOpenAI(
  model="openai/gpt-3.5-turbo",
  base_url="https://openrouter.ai/api/v1"
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({'topic':'unemployment in india'})

# print(result)

chain.get_graph().print_ascii()