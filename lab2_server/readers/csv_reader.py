import csv
from typing import Dict, Iterator, Optional


def read_csv(path: str, limit: Optional[int] = None) -> Iterator[Dict[str, str]]:
    """Read CSV rows as dictionaries.

    Reading is isolated from any output logic to satisfy Strategy separation.
    """
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for index, row in enumerate(reader, start=1):
            yield row
            if limit is not None and index >= limit:
                break
