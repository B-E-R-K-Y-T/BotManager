import flet as ft

from services.database.connector import SQLiteDB
from views.base_frame import BaseFramePage


class ViewBotsPage(BaseFramePage):
    def __init__(self, page: ft.Page, *args, route, **kwargs):
        super().__init__(page, *args, route=route, **kwargs)

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.page = page
        self.scroll = ft.ScrollMode.ADAPTIVE
        self.route = route

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
                            ft.DataCell(ft.IconButton(icon=ft.icons.MENU)),
                        ]
                    ) for bot_id, token, bot_name in self.bots
                ]
            ),
        ]
