import pandas as pd


def profile_quality(dataframe: pd.DataFrame) -> dict:
    total_rows = len(dataframe)

    duplicated_rows = int(dataframe.duplicated().sum())

    columns = []

    for column in dataframe.columns:
        series = dataframe[column]

        profile = {
    "nome": column,
    "tipo": str(series.dtype),
    "nulos": int(series.isna().sum()),
    "percentual_nulos": float(
        series.isna().mean() * 100
    ),
    "valores_unicos": int(
        series.nunique(dropna=True)
    ),
    "constante": bool(
        series.nunique(dropna=True) <= 1
    ),
    "possivel_identificador": bool(
        total_rows > 0
        and series.nunique(dropna=True) > 1
        and series.nunique(dropna=True) / total_rows >= 0.99
    ),
}

        if pd.api.types.is_numeric_dtype(series):
            non_null = series.dropna()

            if not non_null.empty:
                profile["minimo"] = float(non_null.min())
                profile["maximo"] = float(non_null.max())
            else:
                profile["minimo"] = None
                profile["maximo"] = None

        columns.append(profile)

    return {
        "linhas": total_rows,
        "linhas_duplicadas": duplicated_rows,
        "percentual_duplicadas": (
            duplicated_rows / total_rows * 100
            if total_rows
            else 0.0
        ),
        "colunas": columns,
    }
