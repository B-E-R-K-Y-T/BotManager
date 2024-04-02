import flet as ft

from services.app_build.builder import AppBuilder
from config import app_settings
from services.database.init import init_database


async def main(page: ft.Page):
    init_database()

    app_builder = AppBuilder(page)
    app_builder.build()


if __name__ == "__main__":
    if app_settings.WEB_APP:
        ft.app(
            target=main,
            view=ft.AppView.WEB_BROWSER,
            host=app_settings.HOST,
            port=app_settings.PORT
        )
    else:
        ft.app(target=main)
