from typing import Optional

from config import Settings
from output.strategies import JsonFileOutputStrategy
from readers.csv_reader import read_csv


def generate_json(limit: int = 1000, output_path: Optional[str] = None) -> str:
    settings = Settings()
    target_path = output_path or settings.json_output_path
    strategy = JsonFileOutputStrategy(target_path)

    try:
        for record in read_csv(settings.input_csv_path, limit=limit):
            strategy.send(record)
    finally:
        strategy.close()

    return target_path


if __name__ == "__main__":
    result_path = generate_json()
    print(f"JSON generated at: {result_path}")
