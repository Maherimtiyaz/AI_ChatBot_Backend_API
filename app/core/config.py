from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    MONGO_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "ai_chatbot_db"

    # JWT
    JWT_SECRET: str = "secret"
    JWT_ALGORITHM: str = "HS256"


    # LLM
    LLM_PROVIDER: str = "mock"
    GEMINI_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()