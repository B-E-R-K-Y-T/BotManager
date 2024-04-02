from services.database.worker import SQLiteDB


def init_database():
    with SQLiteDB() as db:
        db.create_table(
            table_name="bots",
            columns=["id INTEGER PRIMARY KEY AUTOINCREMENT ", "token TEXT UNIQUE", "name TEXT UNIQUE"]
        )

        db.create_table(
            table_name="chats",
            columns=["id INTEGER PRIMARY KEY AUTOINCREMENT ", "name TEXT"]
        )

        db.create_table(
            table_name="message",
            columns=[
                "id INTEGER PRIMARY KEY AUTOINCREMENT ",
                "text TEXT",
                "timestamp INTEGER",
                "chat_id INTEGER",
                "user_id INTEGER",
            ],
        )


if __name__ == "__main__":
    init_database()
