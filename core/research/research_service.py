from core.research.search_engine import SearchEngine
from core.research.source_verifier import SourceVerifier
from core.research.report_generator import ReportGenerator


class ResearchService:

    def __init__(self):

        self.search_engine = SearchEngine()

        self.source_verifier = SourceVerifier()

        self.report_generator = ReportGenerator()

    def research(self, topic):

        search_results = self.search_engine.search(
            topic
        )

        verified_sources = self.source_verifier.verify(
            search_results["sources"]
        )

        report = self.report_generator.generate_report(
            topic,
            verified_sources
        )

        return {
            "topic": topic,
            "sources": verified_sources,
            "report": report
        }