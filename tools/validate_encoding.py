from pathlib import Path
from zipfile import ZipFile


ZIP_PATH = Path("data/raw/1_2023.zip")

CSV_PATH = (
    "microdados_censo_escolar_2023/"
    "dados/microdados_ed_basica_2023.csv"
)

SAMPLE_SIZE = 1024 * 1024


def validate_encoding() -> None:
    with ZipFile(ZIP_PATH) as z:
        info = z.getinfo(CSV_PATH)

        print(f"Arquivo: {info.filename}")
        print(f"Tamanho: {info.file_size:,} bytes")
        print()

        positions = [
            0,
            info.file_size // 4,
            info.file_size // 2,
            (info.file_size * 3) // 4,
            max(0, info.file_size - SAMPLE_SIZE),
        ]

        with z.open(CSV_PATH) as file:
            for position in positions:
                file.seek(position)

                data = file.read(SAMPLE_SIZE)

                print(f"--- Posição {position:,} ---")
                print(f"Bytes lidos: {len(data):,}")

                for encoding in ("utf-8", "latin-1", "cp1252"):
                    try:
                        text = data.decode(encoding)

                        print(
                            f"{encoding}: OK "
                            f"({len(text):,} caracteres)"
                        )

                        if encoding != "utf-8":
                            preview = text[:300].replace("\n", " ")
                            print(f"  Amostra: {preview}")

                    except UnicodeDecodeError as exc:
                        print(
                            f"{encoding}: ERRO "
                            f"(posição relativa {exc.start})"
                        )

                print()


if __name__ == "__main__":
    validate_encoding()
