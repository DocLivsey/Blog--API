from pydantic_settings import BaseSettings

from os import environ


class Settings(BaseSettings):
    DATASOURCE_URL: str = environ.get('DATASOURCE_URL', 'postgresql://admin:password@db:5432/blog')
    REDIS_URL: str = environ.get('REDIS_URL', 'redis://localhost:6379')

settings = Settings()
