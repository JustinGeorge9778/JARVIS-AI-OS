from tavily import TavilyClient
from config.config import Config


class SearchEngine:

    def __init__(self):
        self.client = TavilyClient(api_key=Config.TAVILY_API_KEY)

    def search(self, query):

        response = self.client.search(
            query=query,
            search_depth="advanced",
            max_results=5
        )

        sources = []

        for result in response["results"]:

            sources.append(
                {
                    "title": result["title"],
                    "url": result["url"],
                    "content": result["content"]
                }
            )

        return {
            "query": query,
            "sources": sources
        }