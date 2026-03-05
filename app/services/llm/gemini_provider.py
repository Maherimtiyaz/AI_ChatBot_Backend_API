import google.generativeai as genai
from .base import BaseLLM
from .app.core.config import settings

# Gemini LLM provider implementation

class GeminiProvider(BaseLLM):

    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-pro")

    async def generate(self, messages):
        # Convert messages to Gemini format
        prompt = "/n".join([m["content"] for m in messages])

        # Call Gemini API
        response = await self.model.generate_content(prompt)
        return response.text