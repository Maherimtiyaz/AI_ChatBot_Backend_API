from .base import BaseLLM

# Mock LLM provider for testing purposes
class MockProvider(BaseLLM):

    async def generate(self, messages):
        # Simulate a response by echoing the last user message
        last_message = messages[-1]["content"]
        return f"[Mock AI] Response to: {last_message}"