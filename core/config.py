from pydantic_settings import BaseSettings

from os import environ


class Settings(BaseSettings):
    DATASOURCE_URL: str = environ.get('DATASOURCE_URL', 'postgresql://admin:password@localhost:5432/blog')
    REDIS_URL: str = environ.get('REDIS_URL', 'redis://localhost:6379')

settings = Settings()

if 'postgresql://' not in settings.DATASOURCE_URL:
    settings.DATASOURCE_URL = f'postgresql://admin:password@{settings.DATASOURCE_URL}/blog'
