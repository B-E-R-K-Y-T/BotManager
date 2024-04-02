import sqlite3

from config import app_settings


class SQLiteDB:
    def __init__(self, db_name: str = app_settings.DATABASE_NAME):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name: str, columns: list):
        columns_str = ", ".join(columns)
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str});")
        self.conn.commit()

    def insert_data(self, table_name: str, data: dict):
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        self.cursor.execute(f"INSERT INTO {table_name}({columns}) VALUES ({placeholders})", list(data.values()))
        self.conn.commit()

    def select_data(self, table_name: str, condition: str = ""):
        if condition:
            self.cursor.execute(f"SELECT * FROM {table_name} WHERE {condition};")
        else:
            self.cursor.execute(f"SELECT * FROM {table_name};")

        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self

    def __del__(self):
        self.cursor.close()
        self.close_connection()


if __name__ == "__main__":
    # Пример использования
    # Создание объекта и подключение к базе данных
    with SQLiteDB("example.db") as db:
        # Создание таблицы
        db.create_table("users", ["id INTEGER PRIMARY KEY", "name TEXT", "age INTEGER"])

        # Вставка данных
        db.insert_data("users", {"id": 1, "name": "Alice", "age": 30})
        db.insert_data("users", {"id": 2, "name": "Bob", "age": 25})

        # Получение данных
        all_users = db.select_data("users")
        print("All users:", all_users)

        # Получение данных с условием
        alice = db.select_data("users", 'name="Alice"')
        print("User Alice:", alice)

    # Соединение с базой данных автоматически закроется после выхода из блока with
