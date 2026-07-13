from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Non-Profit Decision Intelligence MVP"
    database_url: str = "sqlite:///nonprofit.db"
    ollama_url: str = "http://localhost:11434"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()