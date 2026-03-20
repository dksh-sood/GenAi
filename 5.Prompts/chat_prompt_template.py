from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage

from langchain_core.prompts import ChatPromptTemplate

## Dynamic Set of messages 

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple terms what is {topic}")

    # SystemMessage(content='You are a helpful {domain} expert'), 
    # HumanMessage(conten='Explain in a simple terms, what is {topic}')
])

prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "Dusra"
})

print(prompt)