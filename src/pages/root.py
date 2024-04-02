import asyncio
import random

import flet as ft

from pages.base_frame import BaseFramePage


class RootPage(BaseFramePage):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(page, *args, **kwargs)

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.logo = ft.Column(
            alignment=ft.alignment.center,
            controls=[
                ft.Image(
                    src="favicon.png",
                    width=150,
                    height=150
                )
            ],
            scale=ft.transform.Scale(scale=1),
            offset=ft.transform.Offset(0, 0),
            animate_scale=ft.animation.Animation(500, ft.AnimationCurve.BOUNCE_OUT),
            animate_offset=ft.animation.Animation(300, ft.AnimationCurve.EASE_IN)
        )

        self.controls += [
            self.logo
        ]

    async def start_animate(self):
        while True:
            self.logo.scale = (ft.transform.Scale(scale=1.2))
            self.logo.offset = ft.transform.Offset(random.randrange(-4, 5), random.randrange(-1, 2))
            self.logo.update()
            await asyncio.sleep(1)

            self.logo.scale = ft.transform.Scale(scale=1)
            self.logo.update()
            await asyncio.sleep(0.4)
