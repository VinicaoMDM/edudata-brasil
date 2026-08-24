from sqlalchemy import create_engine, text

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


def check_connection() -> bool:
    engine = get_engine()

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return result.scalar() == 1
