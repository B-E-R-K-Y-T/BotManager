from services.api_worker.client import AsyncClient
from services.database.worker import SQLiteDB


class ApiWorker:
    def __init__(self, url: str, token: str):
        self.client = AsyncClient(url)
        self.token = token

    async def get_message(self, message_id):
        message = await self.client.get(f"/api/message/{message_id}", params={"token": self.token})

        return message

    async def get_messages(self):
        messages = await self.client.get("/api/messages", params={"token": self.token})

        return messages

    async def get_chats(self):
        chats = await self.client.get("/api/chats", params={"token": self.token})

        return chats

    async def get_chat_name(self, chat_id: int):
        chat_name = await self.client.get(f"/api/chat/get_name/{chat_id}", params={"token": self.token})

        return chat_name

    async def chat_send_message(self, chat_id: int, message: str):
        await self.client.post(
            f"/api/chat/send_message/{chat_id}/{message}",
            params={"token": self.token},
            # data={"message": message}
        )

        return True
