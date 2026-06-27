from core.gemini.gemini_client import GeminiClient
import json

class ResumeAnalyzer:

    def __init__(self):
        self.gemini = GeminiClient()

    def analyze(self, resume_text):

        prompt = f"""
        Analyze the resume below.

        Resume:
        {resume_text}

        Return ONLY valid JSON.

        Format:

        {{
            "ats_score": 0,
            "strengths": [],
            "weaknesses": [],
            "missing_skills": [],
            "placement_readiness": "",
            "recommendations": []
        }}
        """
        result = self.gemini.ask(prompt)

        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

        try:
            result = json.loads(result)
        except:
            pass

        return result