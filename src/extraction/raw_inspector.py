from pathlib import Path
from zipfile import ZipFile


def inspect_csv_in_zip(
    zip_path: Path,
    csv_name: str,
    sample_size: int = 10_000,
) -> dict:
    with ZipFile(zip_path) as archive:
        info = archive.getinfo(csv_name)

        with archive.open(csv_name) as file:
            sample = file.read(sample_size)

    return {
        "nome": info.filename,
        "tamanho_bytes": info.file_size,
        "tamanho_comprimido_bytes": info.compress_size,
        "amostra": sample,
    }


def sample_csv_in_zip(
    zip_path: Path,
    csv_name: str,
    block_size: int = 1024 * 1024,
    number_of_samples: int = 5,
) -> list[bytes]:
    samples = []

    with ZipFile(zip_path) as archive:
        with archive.open(csv_name) as file:
            total_size = archive.getinfo(csv_name).file_size

            positions = [
                int(total_size * i / (number_of_samples - 1))
                for i in range(number_of_samples)
            ]

            for position in positions:
                file.seek(position)

                if position > 0:
                    file.readline()

                sample = file.read(block_size)

                samples.append(sample)

    return samples
