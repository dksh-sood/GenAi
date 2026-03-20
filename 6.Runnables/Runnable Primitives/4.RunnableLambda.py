from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough , RunnableSequence , RunnableParallel , RunnableLambda

load_dotenv()

def word_count(text):
  return len(text.split())

passthrough = RunnablePassthrough()

prompt = PromptTemplate(
  template = 'write a joke about {topic}',
  input_variables=['topic']
)

model = ChatOpenAI(
  model="openai/gpt-3.5-turbo",
  base_url="https://openrouter.ai/api/v1"
)

parser = StrOutputParser()

joke_gen_word = RunnableSequence(prompt , model , parser)

parallel_chain = RunnableParallel({
  'jokes': RunnablePassthrough(),
  'word_counter': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_word, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

final_result = """ {} \n word count -> {}""".format(result['jokes'], result['word_counter'])