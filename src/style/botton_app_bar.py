import flet as ft
import webbrowser as wb

from config import app_settings
from style.container import Container


class BottomAppBar(Container):
    def __init__(self, page: ft.Page):
        self.copyright_text = ft.Row(
            controls=[
                ft.Container(
                    expand=True
                ),
                ft.Container(
                    content=ft.Text(value="BERKYT", text_align=ft.alignment.center),
                    on_click=self.on_click_berkyt,
                ),
                ft.Text(
                    value="&",
                    text_align=ft.alignment.center
                ),
                ft.Container(
                    content=ft.Text(value="XAMEX", text_align=ft.alignment.center),
                    on_click=self.on_click_xamex,
                ),
                ft.Container(
                    expand=True
                ),
            ]
        )
        self.bgcolor = ft.colors.BLUE_800
        self.bottom_app_bar = ft.BottomAppBar(
            content=self.copyright_text, bgcolor=self.bgcolor
        )

    @staticmethod
    def on_click_berkyt(e):
        wb.open_new_tab(app_settings.BERKYT_LINK)

    @staticmethod
    def on_click_xamex(e):
        wb.open_new_tab(app_settings.XAMEX_LINK)

    def get_container(self):
        return self.bottom_app_bar
