from core.rag.vector_store import VectorStore

vector_store = VectorStore()

results = vector_store.search(
    "What is Artificial Intelligence?"
)

print(results)