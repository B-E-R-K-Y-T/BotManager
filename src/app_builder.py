import flet as ft

from route_manager import RouteManager


class AppBuilder:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.scroll = ft.ScrollMode.ADAPTIVE

    def build(self):
        RouteManager(self.page)
