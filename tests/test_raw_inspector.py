from pathlib import Path
from zipfile import ZipFile

from src.extraction.raw_inspector import inspect_csv_in_zip


def test_inspect_csv_in_zip(tmp_path):
    zip_path = tmp_path / "teste.zip"

    csv_name = "dados/teste.csv"
    csv_content = (
        "NU_ANO_CENSO;NO_UF;CO_UF\n"
        "2023;São Paulo;35\n"
    ).encode("utf-8")

    with ZipFile(zip_path, "w") as archive:
        archive.writestr(csv_name, csv_content)

    result = inspect_csv_in_zip(
        zip_path=zip_path,
        csv_name=csv_name,
    )

    assert result["nome"] == csv_name
    assert result["tamanho_bytes"] == len(csv_content)
    assert result["tamanho_comprimido_bytes"] > 0
    assert result["amostra"] == csv_content
