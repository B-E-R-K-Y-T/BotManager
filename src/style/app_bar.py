from typing import Any

import flet as ft

from config import app_settings
from style.container import Container


class SettingsManager:
    def __init__(self, page: ft.Page):
        self.page = page
        self.parameters = {}

    def add_parameter(self, name: str, parameter: Any):
        self.parameters[name] = parameter

    def switch_theme_mode(self, e):
        theme = {
            ft.ThemeMode.LIGHT: (ft.ThemeMode.DARK, ft.icons.LIGHT_MODE),
            ft.ThemeMode.DARK: (ft.ThemeMode.LIGHT, ft.icons.DARK_MODE),
        }
        theme_mode = self.page.theme_mode

        if theme_mode in theme.keys():
            self.page.theme_mode, self.parameters["theme_btn"].icon = theme[theme_mode]

            self.page.update()

    def add_bot(self, e):
        from urls import Urls

        self.page.route = Urls.ADD_BOT_PAGE.url
        self.page.update()


class AppBar(Container):
    def __init__(self, page: ft.Page, title: str = app_settings.APP_TITLE):
        self.page = page
        self.title: ft.Text = ft.Text(title)
        self.bgcolor = ft.colors.LIGHT_BLUE
        self.settings_manager = SettingsManager(self.page)

        theme_icon = {
            ft.ThemeMode.DARK: ft.icons.LIGHT_MODE,
            ft.ThemeMode.LIGHT: ft.icons.DARK_MODE,
        }

        self.theme_btn = ft.PopupMenuItem(
            icon=theme_icon[self.page.theme_mode],
            text="Сменить тему",
            on_click=self.settings_manager.switch_theme_mode,
        )
        self.add_bot_btn = ft.PopupMenuItem(
            icon=ft.icons.ADD,
            text="Добавить нового бота",
            on_click=self.settings_manager.add_bot,
        )

        self.settings_btn = ft.PopupMenuButton(
            icon=ft.icons.SETTINGS,
            items=[
                self.theme_btn,
                self.add_bot_btn,
            ]
        )

        for btn in [
            ("theme_btn", self.theme_btn),
            ("add_bot_btn", self.add_bot_btn)
        ]:
            self.settings_manager.add_parameter(*btn)

        self.app_bar = ft.AppBar(
            title=ft.Container(
                content=self.title,
                on_click=self.on_click_title
            ),
            bgcolor=self.bgcolor,
            actions=[
                self.settings_btn,
            ],
        )

    def on_click_title(self, e):
        self.page.route = "/"
        self.page.update()

    def get_container(self):
        return self.app_bar
