from typing import Optional

from .interfaces import OutputStrategy
from .strategies import (
    ConsoleOutputStrategy,
    JsonFileOutputStrategy,
    KafkaOutputStrategy,
    RedisOutputStrategy,
)


def create_output_strategy(
    backend: str,
    json_path: Optional[str] = None,
    json_indent: Optional[int] = None,
    kafka_bootstrap_servers: Optional[str] = None,
    kafka_topic: Optional[str] = None,
    redis_host: Optional[str] = None,
    redis_port: Optional[int] = None,
    redis_db: Optional[int] = None,
    redis_key: Optional[str] = None,
) -> OutputStrategy:
    backend = backend.lower()

    if backend == "console":
        return ConsoleOutputStrategy()
    if backend == "json":
        if not json_path:
            raise ValueError("JSON output path is required for JSON backend")
        indent = json_indent if json_indent and json_indent > 0 else None
        return JsonFileOutputStrategy(json_path, indent=indent)
    if backend == "kafka":
        if not kafka_bootstrap_servers or not kafka_topic:
            raise ValueError("Kafka settings are required for Kafka backend")
        return KafkaOutputStrategy(kafka_bootstrap_servers, kafka_topic)
    if backend == "redis":
        if not redis_host or redis_port is None or redis_db is None or not redis_key:
            raise ValueError("Redis settings are required for Redis backend")
        return RedisOutputStrategy(redis_host, redis_port, redis_db, redis_key)

    raise ValueError(f"Unsupported output backend: {backend}")
