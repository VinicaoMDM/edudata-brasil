from src.loading.database import get_database_url


def test_database_url():
    url = get_database_url()

    assert url.startswith("postgresql+psycopg://")
    assert "localhost:5432/edudata" in url
