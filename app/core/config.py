from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    MONGO_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "ai_chatbot_db"

    # JWT
    JWT_SECRET: str = "super_secure_ai_chatbot_backend_secret_key_2026"
    JWT_ALGORITHM: str = "HS256"


    # LLM
    LLM_PROVIDER: str = "mock"
    GEMINI_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()