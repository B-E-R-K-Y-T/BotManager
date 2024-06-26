import flet as ft

from style.app_bar import AppBar
from style.botton_app_bar import BottomAppBar


class BaseFramePage(ft.View):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.appbar = AppBar(page).get_container()
        self.bottom_appbar = BottomAppBar(page).get_container()

    async def async_init(self, *args, **kwargs):
        pass

    async def start_animate(self):
        pass
