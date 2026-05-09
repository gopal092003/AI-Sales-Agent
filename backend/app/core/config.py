from functools import lru_cache
from typing import List

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    # =========================================================
    # APP
    # =========================================================

    APP_NAME: str = "AI Sales Intelligence Agent"
    APP_ENV: str = "development"
    DEBUG: bool = True

    API_V1_PREFIX: str = "/api"

    # =========================================================
    # SERVER
    # =========================================================

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # =========================================================
    # DATABASE
    # =========================================================

    DATABASE_URL: str = "sqlite:///./sales_agent.db"

    # =========================================================
    # AI / LLM
    # =========================================================

    GROQ_API_KEY: str = ""

    DEFAULT_LLM_MODEL: str = "llama3-70b-8192"

    # =========================================================
    # OLLAMA
    # =========================================================

    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3"

    # =========================================================
    # SCRAPING
    # =========================================================

    REQUEST_TIMEOUT: int = 30
    MAX_RETRIES: int = 3

    USER_AGENT: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )

    # =========================================================
    # CORS
    # =========================================================

    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    # =========================================================
    # LOGGING
    # =========================================================

    LOG_LEVEL: str = "INFO"

    # =========================================================
    # FEATURES
    # =========================================================

    ENABLE_NEWS_SCRAPING: bool = True
    ENABLE_TECHSTACK_DETECTION: bool = True
    ENABLE_HIRING_SIGNALS: bool = True

    # =========================================================
    # PYDANTIC CONFIG
    # =========================================================

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # =========================================================
    # VALIDATORS
    # =========================================================

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, value):
        """
        Convert comma-separated CORS origins string into list.
        """

        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",")]

        return value


@lru_cache
def get_settings() -> Settings:
    """
    Cached settings instance.
    """

    return Settings()


settings = get_settings()