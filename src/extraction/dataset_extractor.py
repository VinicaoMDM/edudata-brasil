from pathlib import Path

from src.extraction.downloader import download_file
from src.loading.dataset_version_repository import get_dataset_versions


def extract_dataset(
    dataset_id: int,
    destination: Path,
) -> Path:
    versions = get_dataset_versions(dataset_id)

    if not versions:
        raise ValueError(
            f"Nenhuma versão encontrada para o dataset {dataset_id}."
        )

    version = versions[0]

    url = version["url_download"]

    if not url:
        raise ValueError(
            f"A versão {version['versao']} não possui URL de download."
        )

    return download_file(url, destination)
