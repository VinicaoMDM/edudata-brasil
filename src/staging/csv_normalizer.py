import pandas as pd


def normalize_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    normalized_columns = [
        str(column).strip()
        for column in dataframe.columns
    ]

    if len(normalized_columns) != len(set(normalized_columns)):
        raise ValueError(
            "Existem nomes de colunas duplicados após a normalização."
        )

    result = dataframe.copy()
    result.columns = normalized_columns

    return result
