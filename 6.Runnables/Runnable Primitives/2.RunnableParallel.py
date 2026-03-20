from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
  template = 'generate a tweet about {topic}',
  input_variables=['topic']
)

prompt2 = PromptTemplate(
  template = 'generate a linkdin post about {topic}',
  input_variables=['topic']
)

model = ChatOpenAI(
  model="openai/gpt-3.5-turbo",
  base_url="https://openrouter.ai/api/v1"
)

parser = StrOutputParser()

chain1 = prompt1 | model | parser
chain2 = prompt2 | model | parser

parallel_chain = RunnableParallel({
  'tweet':chain1,
  'linkdin': chain2
})

result = parallel_chain.invoke({'topic':'ai'})

print(result['tweet'])
print(result['linkdin'])