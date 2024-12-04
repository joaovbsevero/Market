import logging
import sqlite3

from ..model.database_register import DatabaseRegister
from ..model.database_deleter import DatabaseDeleter


class RegistrationController:
    def __init__(self):
        self.database_register = DatabaseRegister()
        self.database_deleter = DatabaseDeleter()
        self.last_registration = None

    def register(self, transaction_type, transaction_name, transaction_value, transaction_date):
        info = {
            'transaction_type': transaction_type.lower(),
            'transaction_name': transaction_name,
            'transaction_value': float(transaction_value),
            'transaction_date': transaction_date
        }
        try:
            self.database_register.register(info)
            self.last_registration = info
            return 'Transação cadastrada com sucesso'

        except sqlite3.IntegrityError as e:
            logging.error('IntegrityError on Registration\n ---> ' + str(e) + '\nInformation sent: ' + str(info))
            return 'Houve um erro interno na aplicação.\nPor favor contate o desenvolvedor.'

        except sqlite3.OperationalError as e:
            logging.error('OperationalError on Registration\n ---> ' + str(e) + '\nInformation sent: ' + str(info))
            return 'Houve um erro interno na aplicação.\nPor favor contate o desenvolvedor.'

        except ValueError as e:
            logging.error('ValueError on Registration\n ---> ' + str(e) + '\nInformation sent: ' + str(info))
            return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'

        except Exception as e:
            logging.error('Unknown error on Registration\n ---> ' + str(e) + '\nInformation sent: ' + str(info))
            return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'

    def undo(self):
        if self.last_registration is not None:
            try:
                self.database_deleter.delete(self.last_registration)
                self.last_registration = None
                return 'Transação removida dos registros'

            except sqlite3.IntegrityError as e:
                logging.error('IntegrityError on Registration (UNDO)\n ---> ' + str(e) + '\nInformation sent: ' + str(self.last_registration))
                return 'Houve um erro interno na aplicação.\nPor favor contate o desenvolvedor.'

            except sqlite3.OperationalError as e:
                logging.error('OperationalError on Registration (UNDO)\n ---> ' + str(e) + '\nInformation sent: ' + str(self.last_registration))
                return 'Houve um erro interno na aplicação.\nPor favor contate o desenvolvedor.'

            except ValueError as e:
                logging.error('ValueError on Registration (UNDO)\n ---> ' + str(e) + '\nInformation sent: ' + str(self.last_registration))
                return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'

            except Exception as e:
                logging.error('Unknown error on Registration (UNDO)\n ---> ' + str(e) + '\nInformation sent: ' + str(self.last_registration))
                return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'

        else:
            return 'Nenhuma transação foi adicionada'

    def reset_last_info(self):
        self.last_registration = None
