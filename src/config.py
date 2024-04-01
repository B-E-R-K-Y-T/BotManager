import os

from pydantic_settings import SettingsConfigDict, BaseSettings

# Корень проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class AppSettings(BaseSettings):
    APP_TITLE: str = "DefaultTitleApp"

    DATABASE_NAME: str

    BERKYT_LINK: str = "https://github.com/B-E-R-K-Y-T"
    XAMEX_LINK: str = "https://t.me/AKhametzyanov"

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")


app_settings = AppSettings()
