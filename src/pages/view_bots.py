import flet as ft

from services.database.worker import SQLiteDB
from pages.base_frame import BaseFramePage


def view_bot_menu():
    def params(bot_id: int):
        def on_click_event_handler(e):
            print(bot_id)

        return on_click_event_handler

    return params


class ViewBotsPage(BaseFramePage):
    def __init__(self, page: ft.Page, *args, route, **kwargs):
        super().__init__(page, *args, route=route, **kwargs)

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.page = page
        self.scroll = ft.ScrollMode.ADAPTIVE
        self.route = route
        self.view_bot_on_click = view_bot_menu()

        with SQLiteDB() as db:
            self.bots = db.select_data(
                table_name="bots"
            )
        self.controls += [
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("ID")),
                    ft.DataColumn(ft.Text("Token")),
                    ft.DataColumn(ft.Text("Name")),
                    ft.DataColumn(ft.Text("Menu")),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(bot_id))),
                            ft.DataCell(ft.Text(str(token))),
                            ft.DataCell(ft.Text(str(bot_name))),
                            ft.DataCell(
                                ft.IconButton(
                                    icon=ft.icons.MENU,
                                    on_click=self.view_bot_on_click(bot_id=bot_id)
                                )
                            ),
                        ]
                    ) for bot_id, token, bot_name in self.bots
                ]
            ),
        ]
