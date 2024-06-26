import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class Config(BaseSettings):
    load_dotenv()

    UVICORN_HOST: str = os.getenv("UVICORN_HOST")
    UVICORN_PORT: int = os.getenv("UVICORN_PORT")
    POSTGRES_DSN: str = os.getenv("POSTGRES_DSN")
    JWT_KEY: str = os.getenv("JWT_KEY")
    JWT_ALG: str = os.getenv("JWT_ALG")
    JWT_EXP: int = os.getenv("JWT_EXP")
    DEFAULT_USERNAME: str = os.getenv("DEFAULT_USERNAME")
    DEFAULT_PASSWORD: str = os.getenv("DEFAULT_PASSWORD")


config = Config()
