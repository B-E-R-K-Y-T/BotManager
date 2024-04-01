import flet as ft

from style.container import Container


class AppBar(Container):
    def __init__(self, page: ft.Page, title: str = "Bot Manager"):
        self.page = page
        self.title: ft.Text = ft.Text(title)
        self.bgcolor = ft.colors.BLUE

        theme_icon = {
            ft.ThemeMode.DARK: ft.icons.LIGHT_MODE,
            ft.ThemeMode.LIGHT: ft.icons.DARK_MODE,
        }

        self.theme_btn = ft.IconButton(
            icon=theme_icon[self.page.theme_mode],
            on_click=self.switch_theme_mode

        )
        self.app_bar = ft.AppBar(
            title=self.title,
            bgcolor=self.bgcolor,
            actions=[
                self.theme_btn
            ]
        )

    async def switch_theme_mode(self, e):
        theme = {
            ft.ThemeMode.LIGHT: (ft.ThemeMode.DARK, ft.icons.LIGHT_MODE),
            ft.ThemeMode.DARK: (ft.ThemeMode.LIGHT, ft.icons.DARK_MODE)
        }
        theme_mode = self.page.theme_mode

        if theme_mode in theme.keys():
            self.page.theme_mode, self.theme_btn.icon = theme[theme_mode]

            self.page.update()

    def get_container(self):
        return self.app_bar
