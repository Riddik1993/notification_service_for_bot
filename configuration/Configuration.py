import os
from dataclasses import dataclass


@dataclass
class TelegramApi:
    token: str

@dataclass
class DatabaseConfig:
    dsn: str


@dataclass
class Configuration:
    telegram: TelegramApi
    db: DatabaseConfig


def load_config() -> Configuration:
    token = os.environ.get("BOT_TOKEN")
    tg_api = TelegramApi(token)
    db_dsn = os.environ.get("DB_DSN")
    db_config = DatabaseConfig(db_dsn)
    return Configuration(telegram=tg_api, db=db_config)
