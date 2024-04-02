import flet as ft

from config import app_settings, ThemeMode
from services.route_manage.manager import RouteManager


class AppBuilder:
    def __init__(self, page: ft.Page):
        self.page = page

        if app_settings.THEME_MODE == ThemeMode.dark:
            self.page.theme_mode = ft.ThemeMode.DARK
        elif app_settings.THEME_MODE == ThemeMode.light:
            self.page.theme_mode = ft.ThemeMode.LIGHT
        else:
            self.page.theme_mode = ft.ThemeMode.SYSTEM

        self.page.scroll = ft.ScrollMode.ADAPTIVE

    def build(self):
        RouteManager(self.page)
