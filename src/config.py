"""Файл конфигурации."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Класс настроек."""

    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_pass: str

    class Config:
        """Конфигурация."""

        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def database_url(self):
        return f"postgresql://{self.db_user}:" \
               f"{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()
