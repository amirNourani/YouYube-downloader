from typing import Dict, ClassVar

import yaml
from pydantic_settings import BaseSettings


class ConfigLoader:
    """Loads configuration from a YAML file based on the environment."""

    def __init__(self) -> None:
        self.config_file = f"config/config.yml"
        self.config_data = self._load_config()

    def _load_config(self) -> Dict:
        """Load the YAML configuration file."""
        try:
            with open(self.config_file, "r") as file:
                return yaml.safe_load(file) or {}
        except FileNotFoundError as e:
            raise e
        except yaml.YAMLError as e:
            raise e

    def get_config_file(self) -> Dict:
        return self.config_data



class Settings(BaseSettings):
    """Configuring the application settings."""

    config: ClassVar = ConfigLoader().get_config_file()

    # App global configuration
    COOKIES_FILE: str = config["app"]["cookiesFile"]
    DEVELOPER: str = config["app"]["developerUsername"]

    # Telegram bot settings
    TELEGRAM_BOT_NAME: str = config["telegramBot"]["name"]
    TELEGRAM_BOT_LINK: str = config["telegramBot"]["link"]
    TELEGRAM_BOT_TOKEN: str = config["telegramBot"]["token"]


settings = Settings()