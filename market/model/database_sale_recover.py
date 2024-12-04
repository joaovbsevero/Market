import contextlib
import sqlite3


class DatabaseSaleRecover:
    def __init__(self):
        database_path = 'data/marketdb.db'
        self.conn = sqlite3.connect(database_path)
        
        with contextlib.suppress(Exception):
            self.conn.executescript(open('resources/marketdb.sql', 'r', encoding='utf-8').read())
            self.conn.commit()

    def get_min_sale_value(self):
        query = """
            SELECT MIN(SALE.value) FROM SALE;
        """

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp[0]

    def get_max_sale_value(self):
        query = """
            SELECT MAX(SALE.value) FROM SALE;
        """

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp[0]

    def get_sales_amount_by_name(self, product_name):
        query = """
            SELECT COUNT(SALE.product_name), SALE.product_name, SALE.value
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE 
                    SALE.product_name = "{}"
                GROUP BY
                    SALE.product_name
                ORDER BY
                    COUNT(SALE.product_name) DESC;
        """.format(product_name)

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_sales_amount_by_value(self, min_value, max_value):
        query = """
            SELECT COUNT(SALE.product_name), SALE.product_name, SALE.value
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE
                    SALE.value >= {} AND SALE.value <= {}
                GROUP BY
                    SALE.product_name
                ORDER BY
                    COUNT(SALE.product_name) DESC;
        """.format(min_value, max_value)

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_sales_amount_by_date(self, from_date, to_date):
        query = """
            SELECT COUNT(SALE.product_name), SALE.product_name, SALE.value
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {} AND
                    MONTH_TABLE.month_number >= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    MONTH_TABLE.month_number <= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 12 END) AND
                    SALE.day >= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    SALE.day <= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 31 END)
                GROUP BY
                    SALE.product_name
                ORDER BY
                    COUNT(SALE.product_name) DESC;
        """.format(from_date[2], to_date[2], from_date[2], from_date[1], to_date[2], to_date[1], from_date[1],
                   from_date[2], from_date[0], to_date[1], to_date[2], to_date[0])

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_sales_amount_by_name_and_value(self, name, min_value, max_value):
        query = """
            SELECT COUNT(SALE.product_name), SALE.product_name, SALE.value 
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE
                    SALE.product_name = "{}" AND
                    SALE.value >= {} AND SALE.value <= {}
                GROUP BY
                    SALE.product_name
                ORDER BY
                    COUNT(SALE.product_name) DESC;
        """.format(name, min_value, max_value)

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_sales_amount_by_name_and_date(self, name, from_date, to_date):
        query = """
            SELECT COUNT(SALE.product_name), SALE.product_name, SALE.value
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE
                    SALE.product_name = "{}" AND
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {} AND
                    MONTH_TABLE.month_number >= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    MONTH_TABLE.month_number <= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 12 END) AND
                    SALE.day >= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    SALE.day <= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 31 END)
                GROUP BY
                    SALE.product_name
                ORDER BY
                    COUNT(SALE.product_name) DESC;
        """.format(name, from_date[2], to_date[2], from_date[2], from_date[1], to_date[2], to_date[1], from_date[1],
                   from_date[2], from_date[0], to_date[1], to_date[2], to_date[0])

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_sales_amount_by_value_and_date(self, min_value, max_value, from_date, to_date):
        query = """
            SELECT COUNT(SALE.product_name), SALE.product_name, SALE.value
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE
                    SALE.value >= {} AND SALE.value <= {} AND
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {} AND
                    MONTH_TABLE.month_number >= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    MONTH_TABLE.month_number <= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 12 END) AND
                    SALE.day >= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    SALE.day <= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 31 END)
                GROUP BY
                    SALE.product_name
                ORDER BY
                    COUNT(SALE.product_name) DESC;
        """.format(min_value, max_value, from_date[2], to_date[2], from_date[2], from_date[1], to_date[2], to_date[1],
                   from_date[1], from_date[2], from_date[0], to_date[1], to_date[2], to_date[0])

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_sales_amount_by_name_and_value_and_date(self, name, min_value, max_value, from_date, to_date):
        query = """
            SELECT COUNT(SALE.product_name), SALE.product_name, SALE.value
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE
                    SALE.product_name = "{}" AND
                    SALE.value >= {} AND SALE.value <= {} AND
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {} AND
                    MONTH_TABLE.month_number >= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    MONTH_TABLE.month_number <= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 12 END) AND
                    SALE.day >= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    SALE.day <= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 31 END)
                GROUP BY
                    SALE.product_name
                ORDER BY
                    COUNT(SALE.product_name) DESC;
        """.format(name, min_value, max_value, from_date[2], to_date[2], from_date[2], from_date[1], to_date[2],
                   to_date[1], from_date[1], from_date[2], from_date[0], to_date[1], to_date[2], to_date[0])

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_sales_by_name(self, name):
        query = """
            SELECT SALE.product_name, SALE.value, SALE.day, MONTH_TABLE.month_number, YEAR_TABLE.year_number 
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE
                    SALE.product_name = "{}"
                ORDER BY
                    YEAR_TABLE.year_number DESC,
                    MONTH_TABLE.month_number DESC,
                    SALE.day DESC;
        """.format(name)

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_sales_by_value(self, min_value, max_value):
        query = """
            SELECT SALE.product_name, SALE.value, SALE.day, MONTH_TABLE.month_number, YEAR_TABLE.year_number 
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE
                    SALE.value >= {} AND SALE.value <= {}
                ORDER BY
                    YEAR_TABLE.year_number DESC,
                    MONTH_TABLE.month_number DESC,
                    SALE.day DESC;
        """.format(min_value, max_value)

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_sales_by_date(self, from_date, to_date):
        query = """
            SELECT SALE.product_name, SALE.value, SALE.day, MONTH_TABLE.month_number, YEAR_TABLE.year_number 
	            FROM SALE 
		            INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
	            WHERE
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {} AND
                    MONTH_TABLE.month_number >= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    MONTH_TABLE.month_number <= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 12 END) AND
                    SALE.day >= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    SALE.day <= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 31 END)
	            ORDER BY
	                YEAR_TABLE.year_number DESC,
		            MONTH_TABLE.month_number DESC,
		            SALE.day DESC;
        """.format(from_date[2], to_date[2], from_date[2], from_date[1], to_date[2], to_date[1], from_date[1],
                   from_date[2], from_date[0], to_date[1], to_date[2], to_date[0])

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_sales_by_name_and_value(self, name, min_value, max_value):
        query = """
            SELECT SALE.product_name, SALE.value, SALE.day, MONTH_TABLE.month_number, YEAR_TABLE.year_number 
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE
                    SALE.product_name = "{}" AND
                    SALE.value >= {} AND SALE.value <= {}
                ORDER BY
                    YEAR_TABLE.year_number DESC,
                    MONTH_TABLE.month_number DESC,
                    SALE.day DESC;
        """.format(name, min_value, max_value)

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_sales_by_name_and_date(self, name, from_date, to_date):
        query = """
            SELECT SALE.product_name, SALE.value, SALE.day, MONTH_TABLE.month_number, YEAR_TABLE.year_number 
	            FROM SALE 
		            INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
	            WHERE
	                SALE.product_name = "{}" AND
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {} AND
                    MONTH_TABLE.month_number >= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    MONTH_TABLE.month_number <= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 12 END) AND
                    SALE.day >= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    SALE.day <= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 31 END)
	            ORDER BY
	                YEAR_TABLE.year_number DESC,
		            MONTH_TABLE.month_number DESC,
		            SALE.day DESC;
        """.format(name, from_date[2], to_date[2], from_date[2], from_date[1], to_date[2], to_date[1], from_date[1],
                   from_date[2], from_date[0], to_date[1], to_date[2], to_date[0])

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_sales_by_value_and_date(self, min_value, max_value, from_date, to_date):
        query = """
            SELECT SALE.product_name, SALE.value, SALE.day, MONTH_TABLE.month_number, YEAR_TABLE.year_number 
	            FROM SALE 
		            INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
	            WHERE
	                SALE.value >= {} AND SALE.value <= {} AND
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {} AND
                    MONTH_TABLE.month_number >= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    MONTH_TABLE.month_number <= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 12 END) AND
                    SALE.day >= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    SALE.day <= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 31 END)
	            ORDER BY
	                YEAR_TABLE.year_number DESC,
		            MONTH_TABLE.month_number DESC,
		            SALE.day DESC;
        """.format(min_value, max_value, from_date[2], to_date[2], from_date[2], from_date[1], to_date[2], to_date[1],
                   from_date[1], from_date[2], from_date[0], to_date[1], to_date[2], to_date[0])

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_sales_by_name_and_value_and_date(self, name, min_value, max_value, from_date, to_date):
        query = """
            SELECT SALE.product_name, SALE.value, SALE.day, MONTH_TABLE.month_number, YEAR_TABLE.year_number 
	            FROM SALE 
		            INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
	            WHERE
	                SALE.product_name = "{}" AND
	                SALE.value >= {} AND SALE.value <= {} AND
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {} AND
                    MONTH_TABLE.month_number >= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    MONTH_TABLE.month_number <= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 12 END) AND
                    SALE.day >= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    SALE.day <= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 31 END)
	            ORDER BY
	                YEAR_TABLE.year_number DESC,
		            MONTH_TABLE.month_number DESC,
		            SALE.day DESC;
        """.format(name, min_value, max_value, from_date[2], to_date[2], from_date[2], from_date[1], to_date[2],
                   to_date[1], from_date[1], from_date[2], from_date[0], to_date[1], to_date[2], to_date[0])

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_total_sales_by_name(self, name):
        query = """
            SELECT SUM(SALE.value)
                FROM 
                    SALE 
                WHERE
                    SALE.product_name = "{}";
        """.format(name)

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_total_sales_by_value(self, min_value, max_value):
        query = """
            SELECT SUM(SALE.value)
                FROM 
                    SALE 
                WHERE
                    SALE.value >= {} AND SALE.value <= {};
        """.format(min_value, max_value)

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_total_sales_by_date(self, from_date, to_date):
        query = """
            SELECT SUM(SALE.value)
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {} AND
                    MONTH_TABLE.month_number >= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    MONTH_TABLE.month_number <= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 12 END) AND
                    SALE.day >= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    SALE.day <= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 31 END);
        """.format(from_date[2], to_date[2], from_date[2], from_date[1], to_date[2], to_date[1], from_date[1],
                   from_date[2], from_date[0], to_date[1], to_date[2], to_date[0])

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_total_sales_by_name_and_date(self, name, from_date, to_date):
        query = """
            SELECT SUM(SALE.value)
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE
                    SALE.product_name = "{}" AND
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {} AND
                    MONTH_TABLE.month_number >= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    MONTH_TABLE.month_number <= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 12 END) AND
                    SALE.day >= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    SALE.day <= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 31 END);
        """.format(name, from_date[2], to_date[2], from_date[2], from_date[1], to_date[2], to_date[1], from_date[1],
                   from_date[2], from_date[0], to_date[1], to_date[2], to_date[0])

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_total_sales_by_name_and_value(self, name, min_value, max_value):
        query = """
            SELECT SUM(SALE.value)
                FROM 
                    SALE 
                WHERE
                    SALE.product_name = "{}" AND
                    SALE.value >= {} AND SALE.value <= {};
        """.format(name, min_value, max_value)

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_total_sales_by_value_and_date(self, min_value, max_value, from_date, to_date):
        query = """
            SELECT SUM(SALE.value)
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE
                    SALE.value >= {} AND SALE.value <= {} AND
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {} AND
                    MONTH_TABLE.month_number >= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    MONTH_TABLE.month_number <= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 12 END) AND
                    SALE.day >= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    SALE.day <= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 31 END);
        """.format(min_value, max_value, from_date[2], to_date[2], from_date[2], from_date[1], to_date[2], to_date[1],
                   from_date[1], from_date[2], from_date[0], to_date[1], to_date[2], to_date[0])

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp

    def get_total_sales_by_name_and_value_and_date(self, name, min_value, max_value, from_date, to_date):
        query = """
            SELECT SUM(SALE.value)
                FROM SALE 
                    INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                WHERE
                    SALE.product_name = "{}" AND
                    SALE.value >= {} AND SALE.value <= {} AND
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {} AND
                    MONTH_TABLE.month_number >= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    MONTH_TABLE.month_number <= (CASE WHEN YEAR_TABLE.year_number = {} THEN {} ELSE 12 END) AND
                    SALE.day >= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 0 END) AND
                    SALE.day <= (CASE WHEN MONTH_TABLE.month_number = {} AND YEAR_TABLE.year_number = {} THEN {} ELSE 31 END);
        """.format(name, min_value, max_value, from_date[2], to_date[2], from_date[2], from_date[1], to_date[2],
                   to_date[1], from_date[1], from_date[2], from_date[0], to_date[1], to_date[2], to_date[0])

        with self.conn as con:
            cursor = con.cursor()
            resp = cursor.execute(query).fetchall()
            return resp
