import flet as ft

from app_builder import AppBuilder


async def main(page: ft.Page):
    app_builder = AppBuilder(page)
    app_builder.build()


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
