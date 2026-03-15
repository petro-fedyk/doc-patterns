import json
import os
from typing import Dict, Optional

from .interfaces import OutputStrategy


class ConsoleOutputStrategy(OutputStrategy):
    def send(self, record: Dict[str, str]) -> None:
        print(json.dumps(record, ensure_ascii=False))

    def close(self) -> None:
        return None


class JsonFileOutputStrategy(OutputStrategy):
    def __init__(self, file_path: str, indent: Optional[int] = None) -> None:
        self._file_path = file_path
        self._indent = indent
        self._file = None
        self._first = True
        self._open()

    def _open(self) -> None:
        directory = os.path.dirname(self._file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        self._file = open(self._file_path, "w", encoding="utf-8")
        self._file.write("[")

    def send(self, record: Dict[str, str]) -> None:
        if self._file is None:
            self._open()
        if not self._first:
            self._file.write(",")
        json.dump(record, self._file, ensure_ascii=False, indent=self._indent)
        self._first = False

    def close(self) -> None:
        if self._file:
            self._file.write("]")
            self._file.close()
            self._file = None


class KafkaOutputStrategy(OutputStrategy):
    def __init__(self, bootstrap_servers: str, topic: str) -> None:
        try:
            from kafka import KafkaProducer
        except ImportError as exc:
            raise ImportError(
                "kafka-python is required for KafkaOutputStrategy. "
                "Install it with `pip install kafka-python`."
            ) from exc

        self._topic = topic
        self._producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda value: json.dumps(value, ensure_ascii=False).encode("utf-8"),
        )

    def send(self, record: Dict[str, str]) -> None:
        self._producer.send(self._topic, record)

    def close(self) -> None:
        self._producer.flush()
        self._producer.close()


class RedisOutputStrategy(OutputStrategy):
    def __init__(self, host: str, port: int, db: int, key: str) -> None:
        try:
            import redis
        except ImportError as exc:
            raise ImportError(
                "redis is required for RedisOutputStrategy. Install it with `pip install redis`."
            ) from exc

        self._key = key
        self._client = redis.Redis(host=host, port=port, db=db)

    def send(self, record: Dict[str, str]) -> None:
        payload = json.dumps(record, ensure_ascii=False)
        self._client.rpush(self._key, payload)

    def close(self) -> None:
        try:
            self._client.close()
        except AttributeError:
            pass
