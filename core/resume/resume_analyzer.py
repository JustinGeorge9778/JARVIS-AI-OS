from core.gemini.gemini_client import GeminiClient


class ResumeAnalyzer:

    def __init__(self):
        self.gemini = GeminiClient()

    def analyze(self, resume_text):

        prompt = f"""
        Analyze the following resume.

        Resume:
        {resume_text}

        Give:

        1. ATS Score (0-100)
        2. Strengths
        3. Weaknesses
        4. Missing Skills
        5. Placement Readiness
        6. Improvement Suggestions

        Format the response clearly.
        """

        return self.gemini.ask(prompt)