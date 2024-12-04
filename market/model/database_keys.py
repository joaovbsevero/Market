import contextlib
import sqlite3


class DatabaseKeys:
    def __init__(self):
        database_path = 'data/webdb.db'
        self.conn = sqlite3.connect(database_path)
        
        with contextlib.suppress(Exception):
            self.conn.executescript(open('resources/webdb.sql', 'r', encoding='utf-8').read())
            self.conn.commit()

    def get_username_password(self, enterprise):
        query = f'SELECT username, password FROM USER_KEYS WHERE enterprise="{enterprise}";'

        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchone() or ('Desconhecido', 'Desconhecido')

    def insert_username_password(self, enterprise, username, password):
        query = f'INSERT INTO USER_KEYS VALUES ("{enterprise}", "{username}", "{password}");'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e

    def edit_username_password(self, enterprise, password, username=None):
        if username is not None:
            query = f'UPDATE USER_KEYS SET username="{username}" AND password="{password}" WHERE enterprise="{enterprise}";'
        else:
            query = f'UPDATE USER_KEYS SET password="{password}" WHERE enterprise="{enterprise}";'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e
