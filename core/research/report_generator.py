from core.gemini.gemini_client import GeminiClient

gemini = GeminiClient()


class ReportGenerator:

    def generate_report(
        self,
        topic,
        sources
    ):

        prompt = f"""
        Topic:
        {topic}

        Sources:
        {sources}

        Generate:

        Executive Summary

        Key Findings

        Recommendations

        Conclusion
        """

        return gemini.ask(prompt)