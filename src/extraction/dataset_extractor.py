from pathlib import Path

from src.extraction.downloader import download_file
from src.loading.dataset_version_repository import get_dataset_version


def extract_dataset(
    dataset_id: int,
    versao: str,
    destination: Path,
) -> Path:
    version = get_dataset_version(dataset_id, versao)

    if version is None:
        raise ValueError(
            f"Versão {versao} não encontrada para o dataset {dataset_id}."
        )

    url = version["url_download"]

    if not url:
        raise ValueError(
            f"A versão {version['versao']} não possui URL de download."
        )

    return download_file(url, destination)
