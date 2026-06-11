from core.rag.document_loader import DocumentLoader
from core.rag.text_splitter import TextSplitter

loader = DocumentLoader()
splitter = TextSplitter()

text = loader.load_pdf(
    "uploads/sample.pdf"
)

chunks = splitter.split_text(text)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])