from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough , RunnableSequence , RunnableParallel

load_dotenv()

passthrough = RunnablePassthrough()

prompt1 = PromptTemplate(
  template = 'write a joke about {topic}',
  input_variables=['topic']
)

model = ChatOpenAI(
  model="openai/gpt-3.5-turbo",
  base_url="https://openrouter.ai/api/v1"
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
  template = 'explain the following joke - {text}',
  input_variables=['text']

)

joke_gen_chain = RunnableSequence(prompt1 , model , parser)

chain2 = RunnableSequence(prompt2 , model , parser)

parallel_chain = RunnableParallel({
  'joke' : RunnablePassthrough(),
  'explanation' : chain2
})

final_chain = RunnableSequence(joke_gen_chain , parallel_chain)

print(final_chain)