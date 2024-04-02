import flet as ft

from views.base_frame import BaseFramePage


class RootPage(BaseFramePage):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(page, *args, **kwargs)
