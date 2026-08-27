from pathlib import Path

import pytest

import src.extraction.downloader as downloader


def test_download_file(tmp_path, monkeypatch):
    destination = tmp_path / "arquivo.txt"

    class FakeResponse:
        content = b"EduData Brasil"

        def raise_for_status(self):
            pass

    def fake_get(url, timeout):
        assert url == "https://example.com/arquivo.txt"
        assert timeout == 60
        return FakeResponse()

    monkeypatch.setattr(downloader.requests, "get", fake_get)

    result = downloader.download_file(
        "https://example.com/arquivo.txt",
        destination,
    )

    assert result == destination
    assert destination.exists()
    assert destination.read_bytes() == b"EduData Brasil"


def test_download_file_network_error(tmp_path, monkeypatch):
    destination = tmp_path / "arquivo.txt"

    def fake_get(url, timeout):
        raise downloader.requests.ConnectionError("Erro de conexão")

    monkeypatch.setattr(downloader.requests, "get", fake_get)

    with pytest.raises(RuntimeError, match="Erro ao baixar arquivo"):
        downloader.download_file(
            "https://example.com/arquivo.txt",
            destination,
        )
