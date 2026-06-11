import google.generativeai as genai
from config.config import Config

class GeminiClient:

    def __init__(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def ask(self, prompt):

        response = self.model.generate_content(
            prompt
        )

        return response.text