from pathlib import Path

import requests


def download_file(url: str, destination: Path) -> Path:
    """
    Baixa um arquivo de uma URL e salva no caminho informado.
    """

    destination.parent.mkdir(parents=True, exist_ok=True)

    try:
        response = requests.get(
            url,
            timeout=60,
            stream=True,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Erro ao baixar arquivo: {url}") from exc

    with destination.open("wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

    return destination
