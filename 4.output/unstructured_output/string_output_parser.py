from langchain_openai import ChatOpenAI  # also work with hugging face api
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(
  model="openai/gpt-3.5-turbo",
  base_url="https://openrouter.ai/api/v1"
)


## 1st prompt --> detail prompt
template1 = PromptTemplate(
  template='write a detail report on {topic}',
  input_variables=['topic']
)

## 2nd prompt --> summary line

template2 = PromptTemplate(
  template='write a 5 line summary on the following text . /n {text}',
  input_variables=['text']
)

parser = StrOutputParser()

chain = template1 |model | parser | template2 | model | parser  ## entire chain floow

result = chain.invoke({'topic' : 'black hole'})

print(result)