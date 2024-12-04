from ..model.database_purchase_recover import DatabasePurchaseRecover
from ..model.database_sale_recover import DatabaseSaleRecover


class ConsultController:
    def __init__(self):
        self.purchase_recover = DatabasePurchaseRecover()
        self.sale_recover = DatabaseSaleRecover()
        self.months = {1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
                       7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'}

    # =============================== Sales section ===============================

    def get_min_sale_value(self):
        return self.sale_recover.get_min_sale_value()[0]

    def get_max_sale_value(self):
        return self.sale_recover.get_max_sale_value()[0]

    def get_sales_amount_by_value_and_date(self, min_value, max_value, from_date, to_date):
        result = self.sale_recover.get_sales_amount_by_value_and_date(float(min_value), float(max_value), from_date.split(' '), to_date.split(' '))
        if result:
            return True, result, ''

        return False, [], 'Erro recuperando compras'

    def get_sales_amount_by_name_and_value_and_date(self, name, min_value, max_value, from_date, to_date):
        result = self.sale_recover.get_sales_amount_by_name_and_value_and_date(name, float(min_value), float(max_value), from_date.split(' '), to_date.split(' '))
        if result:
            return True, result, ''

        return False, [], 'Erro recuperando compras'

    def get_sales_by_value_and_date(self, min_value, max_value, from_date, to_date):
        result = self.sale_recover.get_sales_by_value_and_date(float(min_value), float(max_value), from_date.split(' '), to_date.split(' '))
        if result:
            result = [(name, value, ' '.join(map(str, [day, month, year]))) for name, value, day, month, year in result]
            return True, result, ''

        return False, [], 'Erro recuperando vendas'

    def get_sales_by_name_and_value_and_date(self, name, min_value, max_value, from_date, to_date):
        result = self.sale_recover.get_sales_by_name_and_value_and_date(name, float(min_value), float(max_value), from_date.split(' '), to_date.split(' '))
        if result:
            result = [(name, value, ' '.join(map(str, [day, month, year]))) for name, value, day, month, year in result]
            return True, result, ''

        return False, [], 'Erro recuperando vendas'

    def get_total_sales_by_value_and_date(self, min_value, max_value, from_date, to_date):
        return self.sale_recover.get_total_sales_by_value_and_date(float(min_value), float(max_value), from_date.split(' '), to_date.split(' '))

    def get_total_sales_by_name_and_value_and_date(self, name, min_value, max_value, from_date, to_date):
        return self.sale_recover.get_total_sales_by_name_and_value_and_date(name, float(min_value), float(max_value), from_date.split(' '), to_date.split(' '))

    # =============================== Purchases section ===============================

    def get_min_purchase_value(self):
        return self.purchase_recover.get_min_purchase_value()[0]

    def get_max_purchase_value(self):
        return self.purchase_recover.get_max_purchase_value()[0]

    def get_purchases_amount_by_value_and_date(self, min_value, max_value, from_date, to_date):
        result = self.purchase_recover.get_purchases_amount_by_value_and_date(float(min_value), float(max_value), from_date.split(' '), to_date.split(' '))
        if result:
            return True, result, ''

        return False, [], 'Erro recuperando compras'

    def get_purchases_amount_by_name_and_value_and_date(self, name, min_value, max_value, from_date, to_date):
        result = self.purchase_recover.get_purchases_amount_by_name_and_value_and_date(name, float(min_value), float(max_value), from_date.split(' '), to_date.split(' '))
        if result:
            return True, result, ''

        return False, [], 'Erro recuperando compras'

    def get_purchases_by_value_and_date(self, min_value, max_value, from_date, to_date):
        result = self.purchase_recover.get_purchases_by_value_and_date(float(min_value), float(max_value), from_date.split(' '), to_date.split(' '))
        if result:
            result = [(name, value, ' '.join(map(str, [day, month, year]))) for name, value, day, month, year in result]
            return True, result, ''

        return False, [], 'Erro recuperando compras'

    def get_purchases_by_name_and_value_and_date(self, name, min_value, max_value, from_date, to_date):
        result = self.purchase_recover.get_purchases_by_name_and_value_and_date(name, float(min_value), float(max_value), from_date.split(' '), to_date.split(' '))
        if result:
            result = [(name, value, ' '.join(map(str, [day, month, year]))) for name, value, day, month, year in result]
            return True, result, ''

        return False, [], 'Erro recuperando compras'

    def get_total_purchases_by_value_and_date(self, min_value, max_value, from_date, to_date):
        return self.purchase_recover.get_total_purchases_by_value_and_date(float(min_value), float(max_value), from_date.split(' '), to_date.split(' '))

    def get_total_purchases_by_name_and_value_and_date(self, name, min_value, max_value, from_date, to_date):
        return self.purchase_recover.get_total_purchases_by_name_and_value_and_date(name, float(min_value), float(max_value), from_date.split(' '), to_date.split(' '))
