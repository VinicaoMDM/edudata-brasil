from sqlalchemy import text

from src.loading.database import get_engine


def get_dataset_versions(dataset_id: int) -> list[dict]:
    engine = get_engine()

    query = text(
        """
        SELECT
            id,
            dataset_id,
            versao,
            periodo_referencia,
            url_download,
            formato,
            data_extracao
        FROM core.dataset_versao
        WHERE dataset_id = :dataset_id
        ORDER BY versao
        """
    )

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"dataset_id": dataset_id},
        )

        return [dict(row._mapping) for row in result]


def get_dataset_version(
    dataset_id: int,
    versao: str,
) -> dict | None:
    engine = get_engine()

    query = text(
        """
        SELECT
            id,
            dataset_id,
            versao,
            periodo_referencia,
            url_download,
            formato,
            data_extracao
        FROM core.dataset_versao
        WHERE dataset_id = :dataset_id
          AND versao = :versao
        """
    )

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "dataset_id": dataset_id,
                "versao": versao,
            },
        )

        row = result.fetchone()

        if row is None:
            return None

        return dict(row._mapping)
