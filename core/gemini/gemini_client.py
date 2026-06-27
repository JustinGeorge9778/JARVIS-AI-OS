from google import genai
from config.config import Config
import time

class GeminiClient:

    def __init__(self):
        self.client = genai.Client(
            api_key=Config.GEMINI_API_KEY
        )

    def ask(self, prompt):

        retries = 5

        for attempt in range(retries):

            try:

                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                return response.text

            except Exception as e:

                print(f"Attempt {attempt+1} failed")

                if attempt < retries - 1:
                    time.sleep(10)
                else:
                    raise e
    def research(self, prompt):

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text           
