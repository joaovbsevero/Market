import contextlib
import sqlite3


class DatabaseRegister:
    def __init__(self):
        database_path = 'data/marketdb.db'
        self.conn = sqlite3.connect(database_path)
        
        with contextlib.suppress(Exception):
            self.conn.executescript(open('resources/marketdb.sql', 'r', encoding='utf-8').read())
            self.conn.commit()

    def register(self, info):
        date = info['transaction_date'].split('/')

        year = self.get_year(date)
        if not year:
            self.insert_year(date)

        month = self.get_month(date)
        if not month:
            self.insert_month(date)

        month = self.get_month(date)[0][0]
        if info['transaction_type'] == 'purchase':
            self.insert_purchase(info['transaction_name'], info['transaction_value'], date[0], month)

        elif info['transaction_type'] == 'sale':
            self.insert_sale(info['transaction_name'], info['transaction_value'], date[0], month)

        else:
            raise ValueError('Wrong information sent. Check the input formatting method')

    def get_month(self, date):
        month_number = date[1]
        year_number = date[2]
        query = f'SELECT * FROM MONTH_TABLE WHERE month_number={month_number} AND year_number={year_number};'

        with self.conn as con:
            cursor = con.cursor()
            cursor.execute(query)
            return cursor.fetchall()

    def get_year(self, date):
        year_number = date[2]
        query = f'SELECT * FROM YEAR_TABLE WHERE year_number={year_number};'

        with self.conn as con:
            cursor = con.cursor()
            cursor.execute(query)
            return cursor.fetchall()

    def insert_year(self, date):
        year_number = date[2]

        query = f'INSERT INTO YEAR_TABLE (year_number) VALUES ("{year_number}");'

        with self.conn as con:
            cursor = con.cursor()
            cursor.execute(query)

    def insert_month(self, date):
        month_number = date[1]
        year_number = date[2]

        query = f'INSERT INTO MONTH_TABLE (month_number, year_number) VALUES ("{month_number}", "{year_number}");'

        with self.conn as con:
            cursor = con.cursor()
            cursor.execute(query)

    def insert_sale(self, product_name, value, day, month):
        query = f'INSERT INTO SALE (product_name, value, day, id_month) VALUES ("{product_name}", {value}, {day}, {month});'

        with self.conn as con:
            cursor = con.cursor()
            cursor.execute(query)

    def insert_purchase(self, product_name, value, day, month):
        query = f'INSERT INTO PURCHASE (product_name, value, day, id_month) VALUES ("{product_name}", {value}, {day}, {month});'

        with self.conn as con:
            cursor = con.cursor()
            cursor.execute(query)
