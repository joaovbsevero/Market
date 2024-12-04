import sqlite3
import logging

from ..model.database_editor import DatabaseEditor


class EditionController:
    def __init__(self):
        self.database_editor = DatabaseEditor()

    def edit(self, transaction_type, transaction_old_name, transaction_old_value, transaction_old_date,
             transaction_new_name, transaction_new_value, transaction_new_date):
        old_info = {
            'transaction_type': transaction_type.lower(),
            'transaction_name': transaction_old_name,
            'transaction_value': float(transaction_old_value.replace('.', '').replace(',', '.')),
            'transaction_date': str(transaction_old_date).split('/')
        }

        new_info = {
            'transaction_name': transaction_new_name,
            'transaction_value': float(transaction_new_value.replace('.', '').replace(',', '.')),
            'transaction_date': str(transaction_new_date,).split('/')
        }

        try:
            self.database_editor.edit(old_info, new_info)
            return 'Transação alterada com sucesso'

        except sqlite3.IntegrityError as e:
            logging.error('IntegrityError on Edition\n\t---> ' + str(e) + '\nInformation sent: \n\tOld:' + str(old_info) + '\n\tNew:' + str(new_info))
            return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'

        except sqlite3.OperationalError as e:
            logging.error('OperationalError on Edition\n\t---> ' + str(e) + '\nInformation sent: \n\tOld:' + str(old_info) + '\n\tNew:' + str(new_info))
            return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'

        except ValueError as e:
            logging.error('ValueError on Edition\n\t---> ' + str(e) + '\nInformation sent: \n\tOld:' + str(old_info) + '\n\tNew:' + str(new_info))
            return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'

        except Exception as e:
            logging.error('Unknown error on Edition\n\t---> ' + str(e) + '\nInformation sent: \n\tOld:' + str(old_info) + '\n\tNew:' + str(new_info))
            return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'
