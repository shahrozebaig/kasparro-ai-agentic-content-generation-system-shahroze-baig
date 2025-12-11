from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    groq_api_key: str | None = Field(default=None)
    llm_model: str = Field(default="llama-3.1-8b-instant")
    faq_limit: int = Field(default=8)
    outputs_dir: str = Field(default="outputs")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
