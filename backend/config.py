from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_prefix = ""

settings = Settings()