from google import genai
from config.config import Config


class GeminiClient:

    def __init__(self):
        self.client = genai.Client(
            api_key=Config.GEMINI_API_KEY
        )

    def ask(self, prompt):

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text