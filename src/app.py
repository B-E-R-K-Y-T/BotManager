import flet as ft

from app_builder import AppBuilder
from services.database.init import init_database


async def main(page: ft.Page):
    init_database()

    app_builder = AppBuilder(page)
    app_builder.build()


if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER
    )
