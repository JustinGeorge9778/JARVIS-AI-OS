from core.rag.document_loader import DocumentLoader

loader = DocumentLoader()

text = loader.load_pdf(
    "uploads/sample.pdf"
)

print(text[:1000])