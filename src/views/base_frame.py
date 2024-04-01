import flet as ft

from src.style.app_bar import AppBar
from src.style.botton_app_bar import BottomAppBar


class BaseFrame(ft.View):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.appbar = AppBar(page).get_container()
        self.bottom_appbar = BottomAppBar(page).get_container()

    async def start_animate(self):
        pass
