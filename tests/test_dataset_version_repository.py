from src.loading.dataset_version_repository import (
    get_dataset_version,
    get_dataset_versions,
)


def test_get_dataset_versions():
    versions = get_dataset_versions(1)

    assert isinstance(versions, list)
    assert len(versions) >= 1

    version = versions[0]

    assert version["dataset_id"] == 1
    assert version["versao"] == "2023"
    assert version["periodo_referencia"] == "2023"
    assert version["formato"] == "ZIP"


def test_get_dataset_version():
    version = get_dataset_version(1, "2023")

    assert version is not None
    assert version["dataset_id"] == 1
    assert version["versao"] == "2023"
    assert version["periodo_referencia"] == "2023"
    assert version["formato"] == "ZIP"


def test_get_dataset_version_not_found():
    version = get_dataset_version(1, "2099")

    assert version is None
