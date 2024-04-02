import os
from enum import Enum

from pydantic_settings import SettingsConfigDict, BaseSettings

# Корень проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ThemeMode(Enum):
    dark = "Dark"
    light = "Light"


class AppSettings(BaseSettings):
    APP_TITLE: str = "DefaultTitleApp"
    THEME_MODE: ThemeMode

    DATABASE_NAME: str

    BERKYT_LINK: str = "https://github.com/B-E-R-K-Y-T"
    XAMEX_LINK: str = "https://t.me/AKhametzyanov"

    WEB_APP: bool = True

    HOST: str
    PORT: int

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")


app_settings = AppSettings()
