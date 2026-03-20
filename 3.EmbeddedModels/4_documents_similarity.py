from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about virat kholi"

doc_embeddings = model.encode(documents)
query_embedding = model.encode([query])

scores = cosine_similarity(query_embedding, doc_embeddings)[0]
best_index = np.argmax(scores)

print("Query:", query)
print("Best Match:", documents[best_index])
print("Similarity Score:", scores[best_index])