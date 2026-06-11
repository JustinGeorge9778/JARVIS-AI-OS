import chromadb


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="vector_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="jarvis_docs"
        )

    def add_chunks(self, chunks):

        for index, chunk in enumerate(chunks):

            self.collection.add(
                ids=[str(index)],
                documents=[chunk]
            )

        print("Chunks stored successfully!")

    def search(self, query):

        results = self.collection.query(
            query_texts=[query],
            n_results=3
        )

        return results["documents"][0]    