from pathlib import Path
from zipfile import ZipFile

import pandas as pd


def read_csv_from_zip(
    zip_path: Path,
    csv_path: str,
    nrows: int = 100,
) -> pd.DataFrame:
    with ZipFile(zip_path) as z:
        with z.open(csv_path) as file:
            return pd.read_csv(
                file,
                sep=";",
                encoding="latin-1",
                nrows=nrows,
            )
