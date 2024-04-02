import flet as ft

from views.base_frame import BaseFramePage


class AddBotPage(BaseFramePage):
    def __init__(self, page: ft.Page, *args, route, **kwargs):
        super().__init__(page, *args, **kwargs)

        self.route = route
        self.page = page

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.token_field = ft.TextField(
            label="Введите токен бота"
        )
        self.name_bot_field = ft.TextField(
            label="Введите имя бота"
        )
        self.add_button = ft.IconButton(
            icon=ft.icons.ADD
        )

        self.add_bot_container = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    ft.Container(
                        expand=True
                    ),
                    self.token_field,
                    self.name_bot_field,
                    self.add_button,
                    ft.Container(
                        expand=True
                    ),
                ]
            )
        )

        self.controls += [
            self.add_bot_container
        ]
