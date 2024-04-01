import flet as ft

from src.views.base_frame import BaseFrame


class Root(BaseFrame):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(page, *args, **kwargs)
