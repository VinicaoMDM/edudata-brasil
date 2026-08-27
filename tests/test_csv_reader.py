from pathlib import Path

import pandas as pd

from src.staging.csv_reader import read_csv_from_zip


def test_read_csv_from_zip(tmp_path):
    zip_path = tmp_path / "dados.zip"

    csv_content = (
        "NU_ANO_CENSO;NO_REGIAO;NO_MUNICIPIO\n"
        "2023;Norte;Rondônia\n"
        "2023;Nordeste;Mossoró\n"
    ).encode("latin-1")

    import zipfile

    with zipfile.ZipFile(zip_path, "w") as z:
        z.writestr(
            "dados.csv",
            csv_content,
        )

    result = read_csv_from_zip(
        zip_path=Path(zip_path),
        csv_path="dados.csv",
        nrows=2,
    )

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert list(result.columns) == [
        "NU_ANO_CENSO",
        "NO_REGIAO",
        "NO_MUNICIPIO",
    ]
    assert result.iloc[0]["NO_MUNICIPIO"] == "Rondônia"
    assert result.iloc[1]["NO_MUNICIPIO"] == "Mossoró"
