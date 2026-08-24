from sqlalchemy import create_engine

from src.config import settings


def get_database_url() -> str:
    return (
        f"postgresql+psycopg://"
        f"{settings.POSTGRES_USER}:"
        f"{settings.POSTGRES_PASSWORD}@"
        f"{settings.POSTGRES_HOST}:"
        f"{settings.POSTGRES_PORT}/"
        f"{settings.POSTGRES_DB}"
    )


def get_engine():
    return create_engine(get_database_url())
