from pathlib import Path

import src.extraction.dataset_extractor as extractor


def test_extract_dataset(monkeypatch, tmp_path):
    destination = tmp_path / "censo.zip"

    def fake_get_version(dataset_id, versao):
        assert dataset_id == 1
        assert versao == "2023"

        return {
            "id": 1,
            "dataset_id": 1,
            "versao": "2023",
            "periodo_referencia": "2023",
            "url_download": "https://example.com/censo.zip",
            "formato": "ZIP",
            "data_extracao": None,
        }

    def fake_download(url, destination):
        assert url == "https://example.com/censo.zip"
        assert destination == tmp_path / "censo.zip"

        destination.write_bytes(b"EduData Brasil")

        return destination

    monkeypatch.setattr(
        extractor,
        "get_dataset_version",
        fake_get_version,
    )

    monkeypatch.setattr(
        extractor,
        "download_file",
        fake_download,
    )

    result = extractor.extract_dataset(
        dataset_id=1,
        versao="2023",
        destination=destination,
    )

    assert result == destination
    assert destination.exists()
    assert destination.read_bytes() == b"EduData Brasil"
