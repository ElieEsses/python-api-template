from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug_mode: bool = False
    port: int = 8000
    frontend_origins: List[str] = ["http://localhost:3000"]

    db_schema_path: str = "./Project/db/schema.sql"
    db_path: str = "./data.db"

    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore[call-arg]
