from pathlib import Path

from src.staging.csv_profiler import profile_csv_from_zip


ZIP_PATH = Path("data/raw/1_2023.zip")

CSV_PATH = (
    "microdados_censo_escolar_2023/"
    "dados/microdados_ed_basica_2023.csv"
)

NROWS = 10_000


def main() -> None:
    profile = profile_csv_from_zip(
        zip_path=ZIP_PATH,
        csv_path=CSV_PATH,
        nrows=NROWS,
    )

    resumo = profile["resumo"]
    colunas = profile["detalhes_colunas"]

    print("=== Perfil estrutural do CSV ===")
    print()
    print(f"Arquivo: {CSV_PATH}")
    print(f"Linhas analisadas: {profile['linhas_analisadas']:,}")
    print(f"Colunas: {profile['colunas']:,}")

    print()
    print("=== Resumo ===")
    print()
    print(
        f"Colunas numéricas: "
        f"{resumo['colunas_numericas']:,}"
    )
    print(
        f"Colunas de texto: "
        f"{resumo['colunas_texto']:,}"
    )
    print(
        f"Colunas com nulos: "
        f"{resumo['colunas_com_nulos']:,}"
    )
    print(
        f"Colunas sem nulos: "
        f"{resumo['colunas_sem_nulos']:,}"
    )

    print()
    print("=== Colunas com maior percentual de nulos ===")
    print()

    columns_with_nulls = sorted(
        colunas,
        key=lambda column: column["percentual_nulos"],
        reverse=True,
    )

    for column in columns_with_nulls[:20]:
        print(
            f"{column['nome']}: "
            f"{column['percentual_nulos']:.2f}%"
        )

    print()
    print("=== Colunas com tipo object ===")
    print()

    object_columns = [
        column
        for column in colunas
        if column["tipo"] in {"object", "str", "string"}
    ]

    for column in object_columns:
        print(
            f"{column['nome']}: "
            f"nulos={column['nulos']:,}, "
            f"únicos={column['valores_unicos']:,}"
        )


if __name__ == "__main__":
    main()
