from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
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

prompt1 = template1.invoke({'topic' : 'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

result1 = model.invoke(prompt2)

print(result1.content)