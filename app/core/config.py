from pydantic import BaseSettings

class Settings(BaseSettings):
    LLM_PROVIDER: str = "mock"
    GEMINI_API_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()