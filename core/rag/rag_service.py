from core.rag.vector_store import VectorStore
from core.gemini.gemini_client import GeminiClient


class RAGService:

    def __init__(self):

        self.vector_store = VectorStore()

        self.gemini = GeminiClient()

    def ask(self, question):

        chunks = self.vector_store.search(
            question
        )

        context = "\n".join(chunks)

        prompt = f"""
        You are a document assistant.

        Answer ONLY using the provided context.

        If the answer is not in the context,
        say "Information not found in document."

        Context:
        {context}

        Question:
        {question}
        """

        return self.gemini.ask(prompt)