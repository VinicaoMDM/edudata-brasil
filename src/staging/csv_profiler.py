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
            )

    columns = []

    for column in dataframe.columns:
        series = dataframe[column]

        columns.append(
            {
                "nome": column,
                "tipo": str(series.dtype),
                "nulos": int(series.isna().sum()),
                "percentual_nulos": float(
                    series.isna().mean() * 100
                ),
            }
        )

    return {
        "linhas_analisadas": len(dataframe),
        "colunas": len(dataframe.columns),
        "detalhes_colunas": columns,
    }
