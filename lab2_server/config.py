import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    input_csv_path: str = os.getenv("INPUT_CSV_PATH", "data.csv")
    output_backend: str = os.getenv("OUTPUT_BACKEND", "console")
    json_output_path: str = os.getenv("JSON_OUTPUT_PATH", "output/payroll_1000.json")
    json_indent: int = int(os.getenv("JSON_INDENT", "0"))

    kafka_bootstrap_servers: str = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    kafka_topic: str = os.getenv("KAFKA_TOPIC", "payroll")

    redis_host: str = os.getenv("REDIS_HOST", "localhost")
    redis_port: int = int(os.getenv("REDIS_PORT", "6379"))
    redis_db: int = int(os.getenv("REDIS_DB", "0"))
    redis_key: str = os.getenv("REDIS_KEY", "payroll_records")

    firebase_database_url: str = os.getenv("FIREBASE_DATABASE_URL", "")
    firebase_auth_token: str = os.getenv("FIREBASE_AUTH_TOKEN", "")
    firebase_path: str = os.getenv("FIREBASE_PATH", "records")
    firebase_service_account_path: str = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH", "")
