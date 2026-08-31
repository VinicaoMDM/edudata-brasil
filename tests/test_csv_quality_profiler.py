import pandas as pd

from src.staging.csv_quality_profiler import profile_quality


def test_profile_quality():
    dataframe = pd.DataFrame(
        {
            "id": [1, 2, 2, 3],
            "nome": ["A", "B", "B", "C"],
            "constante": ["X", "X", "X", "X"],
            "valor": [10, 20, 20, None],
        }
    )

    result = profile_quality(dataframe)

    assert result["linhas"] == 4
    assert result["linhas_duplicadas"] == 1
    assert result["percentual_duplicadas"] == 25.0

    columns = {
        column["nome"]: column
        for column in result["colunas"]
    }

    assert columns["id"]["valores_unicos"] == 3
    assert columns["nome"]["valores_unicos"] == 3

    assert columns["constante"]["constante"] is True

    assert columns["valor"]["nulos"] == 1
    assert columns["valor"]["percentual_nulos"] == 25.0
    assert columns["valor"]["minimo"] == 10.0
    assert columns["valor"]["maximo"] == 20.0

def test_possible_identifier():
    dataframe = pd.DataFrame(
        {
            "id": [1, 2, 3, 4],
            "nome": ["A", "B", "B", "C"],
        }
    )

    result = profile_quality(dataframe)

    columns = {
        column["nome"]: column
        for column in result["colunas"]
    }

    assert columns["id"]["possivel_identificador"] is True
    assert columns["nome"]["possivel_identificador"] is False