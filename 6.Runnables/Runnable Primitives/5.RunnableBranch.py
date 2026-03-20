from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough , RunnableSequence , RunnableParallel , RunnableBranch

load_dotenv()


passthrough = RunnablePassthrough()

prompt1 = PromptTemplate(
  template = 'write a detailed report on {topic}',
  input_variables=['topic']
)

prompt2 = PromptTemplate(
  template = 'Summarieze the following text \n  {text}',
  input_variables=['text']
)

model = ChatOpenAI(
  model="openai/gpt-3.5-turbo",
  base_url="https://openrouter.ai/api/v1"
)

parser = StrOutputParser()

report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
  (lambda x: len(str(x).split())>500, RunnableSequence(prompt2, model, parser)),
  RunnablePassthrough()
)

final_Chain = report_gen_chain | branch_chain

result = final_Chain.invoke({'topic' : 'Iran vs Israel'})
# print(result)

final_Chain.get_graph().print_ascii()