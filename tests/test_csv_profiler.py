from pathlib import Path
from zipfile import ZipFile

from src.staging.csv_profiler import profile_csv_from_zip


def test_profile_csv_from_zip(tmp_path):
    zip_path = tmp_path / "dados.zip"

    csv_content = (
        "NU_ANO_CENSO;NO_REGIAO;NO_MUNICIPIO\n"
        "2023;Norte;Rondônia\n"
        "2023;Nordeste;Mossoró\n"
        "2023;;São Paulo\n"
    ).encode("latin-1")

    with ZipFile(zip_path, "w") as archive:
        archive.writestr(
            "dados.csv",
            csv_content,
        )

    result = profile_csv_from_zip(
        zip_path=Path(zip_path),
        csv_path="dados.csv",
        nrows=3,
    )

    assert result["linhas_analisadas"] == 3
    assert result["colunas"] == 3

    assert result["resumo"]["colunas_numericas"] == 1
    assert result["resumo"]["colunas_texto"] == 2
    assert result["resumo"]["colunas_com_nulos"] == 1
    assert result["resumo"]["colunas_sem_nulos"] == 2

    columns = result["detalhes_colunas"]

    assert columns[0]["nome"] == "NU_ANO_CENSO"
    assert columns[1]["nome"] == "NO_REGIAO"
    assert columns[2]["nome"] == "NO_MUNICIPIO"

    assert columns[1]["nulos"] == 1
    assert round(
        columns[1]["percentual_nulos"],
        2,
    ) == 33.33

    assert columns[1]["valores_unicos"] == 2
    assert columns[1]["amostra_valores"] == [
        "Norte",
        "Nordeste",
    ]
