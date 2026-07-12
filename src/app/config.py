from importlib.metadata import metadata
from typing import List

from pydantic_settings import BaseSettings

_meta = metadata("python-api-template")


class Settings(BaseSettings):
    debug_mode: bool = False
    port: int = 8000
    frontend_origins: List[str] = ["http://localhost:3000"]

    db_schema_path: str = "./src/app/db/schema.sql"
    db_path: str = "sqlite:///data.db"

    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"


APP_NAME = _meta["Name"]
APP_VERSION = _meta["Version"]
APP_DESCRIPTION = _meta.get("Summary", "")

settings = Settings()  # type: ignore[call-arg]
