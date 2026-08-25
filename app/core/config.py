import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    app_name: str = os.getenv("APP_NAME", "AI API")
    app_env: str = os.getenv("APP_ENV", "local")
    debug: bool = os.getenv("DEBUG", "true").lower() == "true"

settings = Settings()