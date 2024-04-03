import asyncio
import random

import flet as ft
from flet_core import AdaptiveControl
from flet_core.form_field_control import FormFieldControl

from pages.base_frame import BaseFramePage
from services.api_worker.api import ApiWorker
from services.database.worker import SQLiteDB
from services.util import draw_snack_bar_exception_info, async_draw_snack_bar_exception_info


class Item(FormFieldControl, AdaptiveControl):
    pass


class StateItemCollector:
    field_type = Item

    @classmethod
    def fields(cls) -> list[dict]:
        res = []

        for name_attr, type_ in cls.__dict__["__annotations__"].items():
            if type_ is cls.field_type:
                field = getattr(cls, name_attr)

                res.append(field)

        return res


class ItemsSendMessageState(StateItemCollector):
    field: Item = ft.TextField(
        label="Отравить сообщение в чат: {chat_name}",
        visible=False
    )
    send_button: Item = ft.Container(
        content=ft.TextButton(
            content=ft.Text("Отправить"),
            on_click=lambda: None
        ),
        visible=False
    )

    @classmethod
    def items(cls):
        return cls.fields()


def send_message_handler(chat_id, client):
    async def send(e):
        msg = ItemsSendMessageState.field.value
        return await client.chat_send_message(chat_id=chat_id, message=msg)

    return send


def send_message_state_draw():
    def params(chat_id: int, chat_name: str, page: ft.Page, self, client):
        field_label = ItemsSendMessageState.field.label
        send = send_message_handler(chat_id, client)

        def on_click_event_handler(e):
            ItemsSendMessageState.field.visible = True
            ItemsSendMessageState.field.width = page.width / 100 * 75
            ItemsSendMessageState.field.label = field_label.format(chat_name=chat_name)

            ItemsSendMessageState.send_button.visible = True
            ItemsSendMessageState.send_button.content.on_click = send

            ItemsSendMessageState.field.update()
            ItemsSendMessageState.send_button.update()

        return on_click_event_handler

    return params


class BotMenuPage(BaseFramePage):
    def __init__(self, page: ft.Page, *args, route, bot_id: int, **kwargs):
        super().__init__(page, *args, **kwargs)

        self.chats = None
        self.client = None
        self.menu = None
        self.chats_id = None

        self.page = page
        self.route = route
        self.bot_id = bot_id

        self.send_message_handler = send_message_state_draw()

    async def init_chats(self):
        self.chats = []
        height_avatars = 0

        for chat_id in self.chats_id:
            chat_name = await self.client.get_chat_name(chat_id)
            avatar = ft.CircleAvatar(
                content=ft.Text(chat_name[0]),
                color=ft.colors.BLACK87,
                bgcolor=random.choice(
                    [
                        ft.colors.YELLOW_200,
                        ft.colors.GREEN_200,
                        ft.colors.PINK_200,
                        ft.colors.BLUE_200,
                        ft.colors.AMBER_200
                    ]
                ),
                height=self.page.height / 100 * 5
            )

            height_avatars += avatar.height

            self.chats.append(
                ft.PopupMenuButton(
                    offset=ft.Offset(-2, 0),
                    animate_offset=ft.animation.Animation(
                        int(self.page.height) // 2,
                        ft.AnimationCurve.FAST_OUT_SLOWIN
                    ),
                    content=ft.Row(
                        controls=[
                            avatar,
                            ft.Text(chat_name)
                        ]
                    ),
                    items=[
                        ft.PopupMenuItem(
                            icon=ft.icons.SMS,
                            text="Отравить сообщение",
                            on_click=self.send_message_handler(chat_id, chat_name, self.page, self, self.client)
                        )
                    ]
                )
            )

        self.menu = ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        *self.chats,
                        ft.Container(
                            height=self.page.height - height_avatars
                        )
                    ]
                ),
                ft.Container(
                    width=2,
                    height=self.page.height,
                    bgcolor=ft.colors.BLUE_600
                )
            ]
        )

    async def async_init(self):
        with SQLiteDB() as db:
            bot = db.select_data(
                table_name="bots",
                condition=f"id={self.bot_id}"
            )[0]

            _, address, token, _ = bot

            self.client = draw_snack_bar_exception_info(
                self.page,
                ApiWorker,
                address,
                token
            )

        self.chats_id = await async_draw_snack_bar_exception_info(self.page, self.client.get_chats)

        await self.init_chats()

        self.controls += [

            ft.Row(
                controls=[
                    ft.Column(
                        alignment=ft.alignment.top_left,
                        controls=[
                            self.menu
                        ]
                    ),
                    ft.Column(
                        controls=[
                            *ItemsSendMessageState.items(),
                            ft.Container(
                                height=self.page.height / 2
                            )
                        ]
                    )
                ]
            )
        ]

    def check_bot_exist(self):
        with SQLiteDB() as db:
            is_exist_bot = db.select_data(
                table_name="bots",
                condition=f"id={self.bot_id}"
            )

            return bool(is_exist_bot)

    async def start_animate(self):
        for chat in self.chats:
            chat.offset = ft.Offset(x=0, y=0)
            await asyncio.sleep(0.1)
            chat.update()
