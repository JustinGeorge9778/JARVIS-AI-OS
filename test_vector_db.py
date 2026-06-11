from core.rag.document_loader import DocumentLoader
from core.rag.text_splitter import TextSplitter
from core.rag.vector_store import VectorStore

loader = DocumentLoader()
splitter = TextSplitter()
vector_store = VectorStore()

text = loader.load_pdf(
    "uploads/sample.pdf"
)

chunks = splitter.split_text(text)

vector_store.add_chunks(chunks)

print("Stored in ChromaDB successfully!")