from langchain_openai import ChatOpenAi
from dotenv import load_dotenv

load_dotenv()

model = chatOpenAI(model='gpt-4',temperature=1.8 , max_compltion_tokens=10  )

result = model.invoke("what is the capital of india")

print(result.content)