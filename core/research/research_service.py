import json

from core.research.search_engine import SearchEngine
from core.research.source_verifier import SourceVerifier
from core.research.report_generator import ReportGenerator
from core.research.prompt_builder import PromptBuilder
from core.gemini.gemini_client import GeminiClient


class ResearchService:

    def __init__(self):

        self.search_engine = SearchEngine()
        self.source_verifier = SourceVerifier()
        self.report_generator = ReportGenerator()
        self.gemini = GeminiClient()

    def research(self, topic):

        # Step 1: Search the internet
        search_results = self.search_engine.search(topic)

        # Step 2: Verify/Clean sources
        verified_sources = self.source_verifier.verify(
            search_results["sources"]
        )

        # Step 3: Build Gemini prompt
        prompt = PromptBuilder.build(
            topic,
            verified_sources
        )

        # Step 4: Gemini analyzes live search results
        analysis = self.gemini.ask(prompt)

        # Step 5: Remove markdown if Gemini returns it
        analysis = analysis.replace("```json", "")
        analysis = analysis.replace("```", "")
        analysis = analysis.strip()

        # Step 6: Convert JSON string to Python dict
        try:
            analysis = json.loads(analysis)
        except Exception:
            pass

        # Step 7: Format final response
        return self.report_generator.generate(
            topic,
            analysis,
            verified_sources
        )