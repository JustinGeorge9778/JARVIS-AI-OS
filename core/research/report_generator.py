from core.gemini.gemini_client import GeminiClient

gemini = GeminiClient()


class ReportGenerator:

    def generate_report(self, topic):

        prompt = f"""
        Create a professional research report about:

        {topic}

        Format:

        Executive Summary

        Key Findings

        Recommendations

        Conclusion
        """

        return gemini.ask(prompt)