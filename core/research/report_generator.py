class ReportGenerator:

    def generate(
        self,
        topic,
        analysis,
        sources
    ):

        return {
            "success": True,
            "topic": topic,
            "analysis": analysis,
            "sources": sources
        }