from pathlib import Path

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
