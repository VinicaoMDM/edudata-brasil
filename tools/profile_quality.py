from pathlib import Path
from zipfile import ZipFile

from src.staging.csv_quality_profiler import profile_quality


ZIP_PATH = Path("data/raw/1_2023.zip")

CSV_PATH = (
    "microdados_censo_escolar_2023/"
    "dados/microdados_ed_basica_2023.csv"
)

NROWS = 10_000


def main() -> None:
    import pandas as pd

    with ZipFile(ZIP_PATH) as archive:
        with archive.open(CSV_PATH) as file:
            dataframe = pd.read_csv(
                file,
                sep=";",
                encoding="latin-1",
                nrows=NROWS,
                low_memory=False,
            )

    profile = profile_quality(dataframe)

    print("=== Perfil de qualidade ===")
    print()
    print(f"Linhas analisadas: {profile['linhas']:,}")
    print(
        f"Linhas duplicadas: "
        f"{profile['linhas_duplicadas']:,}"
    )
    print(
        f"Percentual duplicado: "
        f"{profile['percentual_duplicadas']:.2f}%"
    )

    columns = profile["colunas"]

    print()
    print("=== Colunas constantes ===")
    print()

    constant_columns = [
        column
        for column in columns
        if column["constante"]
    ]

    for column in constant_columns:
        print(
            f"{column['nome']}: "
            f"{column['valores_unicos']} valor(es)"
        )

    print()
    print("=== Maior cardinalidade ===")
    print()

    highest_cardinality = sorted(
        columns,
        key=lambda column: column["valores_unicos"],
        reverse=True,
    )

    for column in highest_cardinality[:20]:
        print(
            f"{column['nome']}: "
            f"{column['valores_unicos']:,} valores únicos"
        )

    print()
    print("=== Menor cardinalidade ===")
    print()

    lowest_cardinality = sorted(
        columns,
        key=lambda column: column["valores_unicos"],
    )

    for column in lowest_cardinality[:20]:
        print(
            f"{column['nome']}: "
            f"{column['valores_unicos']:,} valores únicos"
        )

    print()
    print("=== Faixas numéricas ===")
    print()

    numeric_columns = [
        column
        for column in columns
        if "minimo" in column
    ]

    for column in numeric_columns[:20]:
        print(
            f"{column['nome']}: "
            f"min={column['minimo']}, "
            f"max={column['maximo']}"
        )


if __name__ == "__main__":
    main()
