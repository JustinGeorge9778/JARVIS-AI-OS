from core.rag.document_loader import DocumentLoader
from core.resume.resume_analyzer import ResumeAnalyzer


class ResumeService:

    def __init__(self):

        self.loader = DocumentLoader()

        self.analyzer = ResumeAnalyzer()

    def analyze_resume(self, file_path):

        resume_text = self.loader.load_pdf(
            file_path
        )

        result = self.analyzer.analyze(
            resume_text
        )

        return result