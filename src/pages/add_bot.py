import sqlite3

import flet as ft

from services.database.worker import SQLiteDB
from style.snack_bar import SnackBar
from pages.base_frame import BaseFramePage


class AddBotPage(BaseFramePage):
    def __init__(self, page: ft.Page, *args, route, **kwargs):
        super().__init__(page, *args, **kwargs)

        self.route = route
        self.page = page

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        field_width = self.page.width / 100 * 25
        button_width = self.page.width / 100 * 5

        self.address_field = ft.TextField(
            width=field_width,
            label="Введите адрес бота"
        )
        self.token_field = ft.TextField(
            width=field_width,
            label="Введите токен бота"
        )
        self.name_bot_field = ft.TextField(
            width=field_width,
            label="Введите имя бота"
        )
        self.add_button = ft.IconButton(
            width=button_width,
            icon=ft.icons.ADD,
            on_click=self.add_bot_handler,
        )

        self.add_bot_container = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    ft.Container(
                        expand=True
                    ),
                    ft.Column(
                        controls=[
                            self.address_field,
                            self.token_field,
                            self.name_bot_field,
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        width=field_width / 2 - button_width / 2,
                                        bgcolor=ft.colors.LIGHT_BLUE
                                    ),
                                    self.add_button,
                                ]
                            )
                        ]
                    ),
                    ft.Container(
                        expand=True
                    ),
                ]
            )
        )

        self.controls += [
            self.add_bot_container
        ]

    def add_bot_handler(self, e):
        if not all([self.token_field.value, self.name_bot_field.value]):
            SnackBar(self.page, "Одно из значений пустое.").activate_snack_bar()
            return

        with SQLiteDB() as db:
            try:
                db.insert_data(
                    table_name="bots",
                    data={
                        "address": self.address_field.value,
                        "token": self.token_field.value,
                        "name": self.name_bot_field.value
                    }
                )
                SnackBar(self.page, "Успешно.").activate_snack_bar()
            except sqlite3.Error as e:
                SnackBar(self.page, f"Ошибка. Подробнее: \"{str(e)}\"").activate_snack_bar()
                return
