from src.loading.dataset_repository import get_datasets


def test_get_datasets():
    datasets = get_datasets()

    assert isinstance(datasets, list)
    assert len(datasets) >= 1

    dataset = datasets[0]

    assert dataset["nome"] == "Censo Escolar da Educação Básica"
    assert dataset["periodicidade"] == "Anual"
    assert dataset["formato"] == "CSV/XLSX/ZIP"
    assert dataset["ativo"] is True
