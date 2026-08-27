from pathlib import Path

import src.extraction.ingestion as ingestion


def test_ingest_dataset(monkeypatch, tmp_path):
    def fake_get_datasets():
        return [
            {
                "id": 1,
                "fonte_id": 1,
                "nome": "Censo Escolar da Educação Básica",
                "descricao": "Dataset de teste",
                "url": "https://example.com",
                "periodicidade": "Anual",
                "formato": "CSV/XLSX/ZIP",
                "ativo": True,
            }
        ]

    def fake_get_dataset_versions(dataset_id):
        assert dataset_id == 1

        return [
            {
                "id": 1,
                "dataset_id": 1,
                "versao": "2023",
                "periodo_referencia": "2023",
                "url_download": "https://example.com/censo.zip",
                "formato": "ZIP",
                "data_extracao": None,
            }
        ]

    def fake_extract_dataset(dataset_id, versao, destination):
        assert dataset_id == 1
        assert versao == "2023"
        assert destination == Path("data/raw/1_2023.zip")

        destination = tmp_path / "1_2023.zip"
        destination.write_bytes(b"EduData Brasil")

        return destination

    monkeypatch.setattr(
        ingestion,
        "get_datasets",
        fake_get_datasets,
    )

    monkeypatch.setattr(
        ingestion,
        "get_dataset_versions",
        fake_get_dataset_versions,
    )

    monkeypatch.setattr(
        ingestion,
        "extract_dataset",
        fake_extract_dataset,
    )

    result = ingestion.ingest_dataset(1)

    assert result == tmp_path / "1_2023.zip"
    assert result.exists()
    assert result.read_bytes() == b"EduData Brasil"
