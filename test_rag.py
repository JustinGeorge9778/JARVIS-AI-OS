from core.rag.rag_service import RAGService

rag = RAGService()

answer = rag.ask(
    "What is Artificial Intelligence?"
)

print("\nAnswer:\n")
print(answer)