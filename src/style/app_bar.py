import flet as ft

from src.config import app_settings
from src.style.container import Container


class AppBar(Container):
    def __init__(self, page: ft.Page, title: str = app_settings.APP_TITLE):
        self.page = page
        self.title: ft.Text = ft.Text(title)
        self.bgcolor = ft.colors.LIGHT_BLUE

        theme_icon = {
            ft.ThemeMode.DARK: ft.icons.LIGHT_MODE,
            ft.ThemeMode.LIGHT: ft.icons.DARK_MODE,
        }

        self.theme_btn = ft.PopupMenuItem(
            icon=theme_icon[self.page.theme_mode],
            text="Сменить тему",
            on_click=self.switch_theme_mode,
        )

        self.settings_btn = ft.PopupMenuButton(
            icon=ft.icons.SETTINGS, items=[self.theme_btn]
        )

        self.app_bar = ft.AppBar(
            title=ft.Container(content=self.title, on_click=self.on_click_title),
            bgcolor=self.bgcolor,
            actions=[
                self.settings_btn,
            ],
        )

    def on_click_title(self, e):
        self.page.route = "/"
        self.page.update()

    def switch_theme_mode(self, e):
        theme = {
            ft.ThemeMode.LIGHT: (ft.ThemeMode.DARK, ft.icons.LIGHT_MODE),
            ft.ThemeMode.DARK: (ft.ThemeMode.LIGHT, ft.icons.DARK_MODE),
        }
        theme_mode = self.page.theme_mode

        if theme_mode in theme.keys():
            self.page.theme_mode, self.theme_btn.icon = theme[theme_mode]

            self.page.update()

    def get_container(self):
        return self.app_bar
