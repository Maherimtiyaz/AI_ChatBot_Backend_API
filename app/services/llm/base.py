from abc import ABC, abstractmethod
from typing import List, Dict

# Define an abstract base class for LLM services
class BaseLLM(ABC):

    @abstractmethod
    async def generate(self, messageS: List[Dict[str, str]]) -> str:
        pass