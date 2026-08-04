from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    aws_region: str
    s3_bucket: str
    dynamodb_table: str
    event_bus: str
    sns_topic: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()