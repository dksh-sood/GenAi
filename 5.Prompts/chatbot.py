from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, BaseMessage
##  basemsg give the standart format to write the msg
load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    base_url="https://openrouter.ai/api/v1"
)

chat_history: list[BaseMessage]= [
    SystemMessage(content="You are a helpful AI assistant.")
]

while True:
    user_input = input("You: ")

    if user_input.strip().lower() == "exit":
        break

    # add user message
    chat_history.append(HumanMessage(content=user_input))

    # send full conversation
    result = model.invoke(chat_history)

    # add AI response to history
    chat_history.append(AIMessage(content=result.content))

    print("AI:", result.content)

print("\nFull Chat History:\n")
for msg in chat_history:
    print(msg)

# without chat history
# this chatbot donot have any context and they donot have a knowledge to learn from the history every cmd has a particular ans not a previous recall

# we  have all the msg but we dont know who send the msg ?
# its cause prblm like after too long chat ai frogot this text is send by me or user  --> solved by langchain