import flet as ft

from style.app_bar import AppBar
from style.botton_app_bar import BottomAppBar


class BaseFrame(ft.View):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_bar = AppBar(page)

        self.controls += [
            self.app_bar.get_container()
        ]
        self.bottom_appbar = BottomAppBar().get_container()

    async def start_animate(self):
        pass
