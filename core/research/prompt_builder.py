class PromptBuilder:

    @staticmethod
    def build(topic, sources):

        source_text = ""

        for source in sources:

            source_text += f"""

Title:
{source['title']}

Content:
{source['content']}

URL:
{source['url']}

"""

        return f"""
You are an expert AI Research Assistant.

Research Topic:
{topic}

Below are live internet search results.

{source_text}

Analyze these search results and return ONLY valid JSON.

Return this format:

{{
    "executive_summary": "...",

    "key_findings": [
        "...",
        "..."
    ],

    "recommendations": [
        "...",
        "..."
    ]
}}

Do not include markdown.
Do not include ```json.
Return only JSON.
"""