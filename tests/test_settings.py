import src.config.settings as settings


def test_default_settings():
    assert settings.POSTGRES_HOST == "localhost"
    assert settings.POSTGRES_PORT == 5432
    assert settings.POSTGRES_DB == "edudata"
    assert settings.POSTGRES_USER == "postgres"
