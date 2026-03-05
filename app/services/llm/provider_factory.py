from app.core.config import settings
from .mock_provider import MockProvider
from .gemini_provider import GeminiProvider

# Factory to create LLM provider instances based on configuration
def get_llm_provider():
    if settings.LLM_PROVIDER == "gemini":
        return GeminiProvider()
    
    return MockProvider()