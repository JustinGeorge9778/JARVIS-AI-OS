class SearchEngine:

    def search(self, query):

        return {
            "query": query,
            "sources": [
                {
                    "title": "Source 1",
                    "url": "https://example.com"
                }
            ]
        }