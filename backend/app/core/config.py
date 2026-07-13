from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Non-Profit Decision Intelligence MVP"


settings = Settings()