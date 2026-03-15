from typing import Optional

from config import Settings
from output.factory import create_output_strategy
from readers.csv_reader import read_csv


def run(limit: Optional[int] = None) -> None:
    settings = Settings()
    strategy = create_output_strategy(
        backend=settings.output_backend,
        json_path=settings.json_output_path,
        json_indent=settings.json_indent,
        kafka_bootstrap_servers=settings.kafka_bootstrap_servers,
        kafka_topic=settings.kafka_topic,
        redis_host=settings.redis_host,
        redis_port=settings.redis_port,
        redis_db=settings.redis_db,
        redis_key=settings.redis_key,
    )

    try:
        for record in read_csv(settings.input_csv_path, limit=limit):
            strategy.send(record)
    finally:
        strategy.close()


if __name__ == "__main__":
    run()
