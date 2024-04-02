import flet as ft

from style.container import Container


class SnackBar(Container):
    def __init__(self, page: ft.Page, text: str):
        self.page = page
        self.text = text
        self.shack_bar = ft.SnackBar(
            content=ft.Text(self.text)
        )

    def get_container(self):
        return self.shack_bar

    def activate_snack_bar(self):
        self.page.snack_bar = self.shack_bar
        self.page.snack_bar.open = True
        self.page.update()

    def __del__(self):
        self.page.snack_bar.open = False
        self.page.snack_bar = None
