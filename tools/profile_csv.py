from pathlib import Path

from src.staging.csv_profiler import profile_csv_from_zip


ZIP_PATH = Path("data/raw/1_2023.zip")

CSV_PATH = (
    "microdados_censo_escolar_2023/"
    "dados/microdados_ed_basica_2023.csv"
)

SAMPLE_SIZE = 10_000


def main() -> None:
    result = profile_csv_from_zip(
        zip_path=ZIP_PATH,
        csv_path=CSV_PATH,
        nrows=SAMPLE_SIZE,
    )

    print("=== Perfil do CSV ===")
    print()
    print(f"Arquivo: {CSV_PATH}")
    print(f"Linhas analisadas: {result['linhas_analisadas']:,}")
    print(f"Colunas: {result['colunas']}")
    print()

    print("=== Colunas ===")
    print()

    for column in result["detalhes_colunas"]:
        print(
            f"{column['nome']}: "
            f"tipo={column['tipo']}, "
            f"nulos={column['nulos']:,}, "
            f"nulos%={column['percentual_nulos']:.2f}%"
        )


if __name__ == "__main__":
    main()
