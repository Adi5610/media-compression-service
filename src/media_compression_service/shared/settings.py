from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[3]

class Settings(BaseSettings):
    aws_region: str
    s3_bucket_name: str
    upload_url_expiration: int = 900

    model_config = SettingsConfigDict(
        env_file= PROJECT_ROOT/".env",
        extra="ignore",
    )

settings = Settings()