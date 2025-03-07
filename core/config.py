from pydantic_settings import BaseSettings

from os import environ


class Settings(BaseSettings):
    DATASOURCE_URL: str = environ.get('DATASOURCE_URL', 'postgres://localhost:5432')
    REDIS_URL: str = environ.get('REDIS_URL', 'redis://localhost:6379')

settings = Settings()
