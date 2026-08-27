from pathlib import Path
from zipfile import ZipFile


ZIP_PATH = Path("data/raw/1_2023.zip")

CSV_NAME = (
    "microdados_censo_escolar_2023/"
    "dados/microdados_ed_basica_2023.csv"
)

BLOCK_SIZE = 1024 * 1024


def inspect_encoding():
    with ZipFile(ZIP_PATH) as archive:
        info = archive.getinfo(CSV_NAME)

        print(f"Arquivo: {info.filename}")
        print(f"Tamanho: {info.file_size:,} bytes")
        print()

        total_bytes = 0
        non_ascii_bytes = 0
        utf8_errors = 0
        examples = []

        with archive.open(CSV_NAME) as file:
            while True:
                block = file.read(BLOCK_SIZE)

                if not block:
                    break

                total_bytes += len(block)

                non_ascii_bytes += sum(
                    1 for byte in block if byte >= 128
                )

                try:
                    block.decode("utf-8")
                except UnicodeDecodeError as exc:
                    utf8_errors += 1

                    if len(examples) < 10:
                        start = max(0, exc.start - 30)
                        end = min(len(block), exc.end + 30)

                        examples.append(
                            block[start:end]
                        )

        print(f"Bytes analisados: {total_bytes:,}")
        print(f"Bytes >= 128: {non_ascii_bytes:,}")
        print(f"Blocos com erro UTF-8: {utf8_errors}")
        print()
        print("Exemplos de bytes próximos aos erros UTF-8:")

        for index, example in enumerate(examples, start=1):
            print()
            print(f"--- Exemplo {index} ---")
            print("HEX:", example.hex(" "))

            print(
                "Latin-1:",
                example.decode("latin-1", errors="replace"),
            )

            print(
                "Windows-1252:",
                example.decode("cp1252", errors="replace"),
            )


if __name__ == "__main__":
    inspect_encoding()
