from pathlib import Path

import requests


def download_file(url: str, destination: Path) -> Path:
    """
    Baixa um arquivo de uma URL e salva no caminho informado.
    """

    destination.parent.mkdir(parents=True, exist_ok=True)

    response = requests.get(url, timeout=60)
    response.raise_for_status()

    destination.write_bytes(response.content)

    return destination
