import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    app_name: str = os.getenv("APP_NAME", "AI API")
    app_env: str = os.getenv("APP_ENV", "local")
    debug: bool = os.getenv("DEBUG", "true").lower() == "true"
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@127.0.0.1:15433/ai_doc_analyzer"
    )

settings = Settings()