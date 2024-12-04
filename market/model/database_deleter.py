import contextlib
import sqlite3


class DatabaseDeleter:
    def __init__(self):
        database_path = 'data/marketdb.db'
        self.conn = sqlite3.connect(database_path)

        with contextlib.suppress(Exception):
            self.conn.executescript(open('resources/marketdb.sql', 'r', encoding='utf-8').read())
            self.conn.commit()

    def delete(self, info):
        date = info['transaction_date'].split('/')

        year = self.get_year(date)
        if not year:
            raise ValueError('Year not found')

        month = self.get_month(date)
        if not month:
            raise ValueError('Month not found')

        month = month[0][0]
        if info['transaction_type'] == 'purchase':
            self.delete_purchase(info['transaction_name'], info['transaction_value'], date[0], month)

        elif info['transaction_type'] == 'sale':
            self.delete_sale(info['transaction_name'], info['transaction_value'], date[0], month)

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

    def delete_sale(self, name, value, day, month):
        get_id_query = f'SELECT id_sale FROM SALE WHERE product_name="{name}" AND value={value} AND day={day} AND id_month={month};'

        with self.conn as con:
            cursor = con.cursor()
            id_sale = cursor.execute(get_id_query).fetchone()[0]
            cursor.execute(f'DELETE FROM SALE WHERE id_sale={id_sale};')

    def delete_purchase(self, name, value, day, month):
        get_id_query = f'SELECT id_purchase FROM PURCHASE WHERE product_name="{name}" AND value={value} AND day={day} AND id_month={month};'

        with self.conn as con:
            cursor = con.cursor()
            id_purchase = cursor.execute(get_id_query).fetchone()[0]
            cursor.execute(f'DELETE FROM PURCHASE WHERE id_purchase={id_purchase};')
