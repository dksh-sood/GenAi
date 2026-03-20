from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

documents = [
  "delhi is the capital of india ",
  "kolkata is the capital of west bengal",
  "pune is the caqpital of maharashtra"
]

result = embedding.embed_query(documents)

print(str(result))