import pandas as pd
import pytest

from src.staging.csv_normalizer import normalize_columns


def test_normalize_columns_removes_spaces():
    dataframe = pd.DataFrame(
        {
            " id ": [1, 2],
            " nome ": ["A", "B"],
        }
    )

    result = normalize_columns(dataframe)

    assert list(result.columns) == ["id", "nome"]


def test_normalize_columns_rejects_duplicates_after_normalization():
    dataframe = pd.DataFrame(
        {
            "id": [1, 2],
            " id ": [3, 4],
        }
    )

    with pytest.raises(ValueError):
        normalize_columns(dataframe)
