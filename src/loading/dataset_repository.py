from sqlalchemy import text

from src.loading.database import get_engine


def get_datasets() -> list[dict]:
    engine = get_engine()

    query = text(
        """
        SELECT
            id,
            fonte_id,
            nome,
            descricao,
            url,
            periodicidade,
            formato,
            ativo
        FROM core.dataset
        ORDER BY id
        """
    )

    with engine.connect() as connection:
        result = connection.execute(query)

        return [dict(row._mapping) for row in result]
