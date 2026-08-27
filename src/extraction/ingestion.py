from pathlib import Path

from src.extraction.dataset_extractor import extract_dataset
from src.loading.dataset_repository import get_datasets
from src.loading.dataset_version_repository import get_dataset_versions


RAW_DIR = Path("data/raw")


def ingest_dataset(dataset_id: int) -> Path:
    datasets = get_datasets()

    dataset = next(
        (item for item in datasets if item["id"] == dataset_id),
        None,
    )

    if dataset is None:
        raise ValueError(
            f"Dataset não encontrado: {dataset_id}"
        )

    versions = get_dataset_versions(dataset_id)

    if not versions:
        raise ValueError(
            f"Nenhuma versão encontrada para o dataset: {dataset_id}"
        )

    version = versions[-1]

    destination = RAW_DIR / f"{dataset_id}_{version['versao']}.zip"

    return extract_dataset(
        dataset_id=dataset_id,
        versao=version["versao"],
        destination=destination,
    )
