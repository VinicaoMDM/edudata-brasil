from pathlib import Path
from zipfile import ZipFile

import pandas as pd


def profile_csv_from_zip(
    zip_path: Path,
    csv_path: str,
    nrows: int = 10_000,
) -> dict:
    with ZipFile(zip_path) as archive:
        with archive.open(csv_path) as file:
            dataframe = pd.read_csv(
                file,
                sep=";",
                encoding="latin-1",
                nrows=nrows,
                low_memory=False,
            )

    columns = []

    for column in dataframe.columns:
        series = dataframe[column]

        non_null = series.dropna()

        sample_values = [
            str(value)
            for value in non_null.head(5).tolist()
        ]

        columns.append(
            {
                "nome": column,
                "tipo": str(series.dtype),
                "nulos": int(series.isna().sum()),
                "percentual_nulos": float(
                    series.isna().mean() * 100
                ),
                "valores_unicos": int(
                    series.nunique(dropna=True)
                ),
                "amostra_valores": sample_values,
            }
        )

    total_columns = len(dataframe.columns)

    columns_with_nulls = sum(
        1
        for column in columns
        if column["nulos"] > 0
    )

    object_columns = sum(
        1
        for column in columns
        if column["tipo"] in {"object", "str", "string"}
    )

    numeric_columns = total_columns - object_columns

    return {
        "linhas_analisadas": len(dataframe),
        "colunas": total_columns,
        "resumo": {
            "colunas_numericas": numeric_columns,
            "colunas_texto": object_columns,
            "colunas_com_nulos": columns_with_nulls,
            "colunas_sem_nulos": (
                total_columns - columns_with_nulls
            ),
        },
        "detalhes_colunas": columns,
    }
