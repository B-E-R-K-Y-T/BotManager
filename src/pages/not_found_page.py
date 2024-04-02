import asyncio

import flet as ft

from pages.base_frame import BaseFramePage


class NotFoundPage(BaseFramePage):
    def __init__(self, page: ft.Page, *args, route, **kwargs):
        super().__init__(page, *args, route=route, **kwargs)

        self.page = page

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.route = route

        self.not_found_text = ft.Text(
                    value="Page Not Found",
                    scale=3,
                    offset=ft.Offset(x=0, y=-int(self.page.height) / 100 * 5),
                    animate_offset=ft.animation.Animation(
                        int(self.page.height),
                        ft.AnimationCurve.BOUNCE_OUT
                    ),
                )

        self.controls += [
            ft.Container(
                alignment=ft.alignment.center,
                content=self.not_found_text,
            )
        ]

    async def start_animate(self):
        self.not_found_text.offset = ft.Offset(x=0, y=0)
        await asyncio.sleep(0.1)
        self.not_found_text.update()
