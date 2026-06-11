from pypdf import PdfReader


class DocumentLoader:

    def load_pdf(self, file_path):

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text