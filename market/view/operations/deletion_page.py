import locale
locale.setlocale(locale.LC_MONETARY, '')
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

from ...controller.consult_controller import ConsultController
from ...controller.deletion_controller import DeletionController


class DeletionPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(DeletionPage, self).__init__(*args)

        self.back_signal = back_signal
        self.consult_controller = ConsultController()
        self.deletion_controller = DeletionController()
        self.dialog = QtWidgets.QMessageBox(self)
        self.dialog.setWindowTitle('Aviso')
        self.previous_sale_selection = None
        self.previous_purchase_selection = None

        # Main
        self.grid_layout = QtWidgets.QGridLayout(self)

        self.date_input_verticalWidget = QtWidgets.QWidget(self, *args)
        self.date_input_layout = QtWidgets.QVBoxLayout(self.date_input_verticalWidget)

        self.tables_gridWidget = QtWidgets.QWidget(self, *args)
        self.tables_layout = QtWidgets.QGridLayout(self.tables_gridWidget)

        self.purchases_table = QtWidgets.QTableWidget(self.tables_gridWidget)
        self.sales_table = QtWidgets.QTableWidget(self.tables_gridWidget)

        self.bottom_buttons_horizontalWidget = QtWidgets.QWidget(self, *args)
        self.bottom_buttons_layout = QtWidgets.QHBoxLayout(self.bottom_buttons_horizontalWidget)

        self.undo_button_horizontalWidget = QtWidgets.QWidget(self)
        self.undo_button_layout = QtWidgets.QHBoxLayout(self.undo_button_horizontalWidget)

        # Labels
        self.to_date_label = QtWidgets.QLabel(self.date_input_verticalWidget)
        self.from_date_label = QtWidgets.QLabel(self.date_input_verticalWidget)

        self.purchases_label = QtWidgets.QLabel(self.tables_gridWidget)
        self.sales_label = QtWidgets.QLabel(self.tables_gridWidget)

        # Buttons
        self.update_list_button = QtWidgets.QPushButton(self)
        self.undo_button = QtWidgets.QPushButton(self)
        self.back_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)
        self.delete_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)

        # Inputs
        self.to_date_option = QtWidgets.QDateEdit(self.date_input_verticalWidget)
        self.from_date_option = QtWidgets.QDateEdit(self.date_input_verticalWidget)

        # Building UI
        self.setup_ui()
        self.translate_ui()
        self.create_structure()
        self.define_actions()

    def setup_ui(self):
        # Main
        self.tables_gridWidget.setMinimumSize(QtCore.QSize(900, 470))

        self.purchases_table.setColumnCount(3)
        self.purchases_table.verticalHeader().setVisible(False)
        self.purchases_table.horizontalHeader().setHighlightSections(False)
        self.purchases_table.cellClicked.connect(self.update_purchase_selection)
        self.purchases_table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.purchases_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.purchases_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.purchases_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.purchases_table.setMinimumSize(QtCore.QSize(400, 400))
        self.purchases_table.setMaximumSize(QtCore.QSize(450, 1080))
        self.purchases_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.purchases_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.purchases_table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.sales_table.setColumnCount(3)
        self.sales_table.verticalHeader().setVisible(False)
        self.sales_table.horizontalHeader().setHighlightSections(False)
        self.sales_table.cellClicked.connect(self.update_sale_selection)
        self.sales_table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sales_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sales_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sales_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.sales_table.setMinimumSize(QtCore.QSize(400, 400))
        self.sales_table.setMaximumSize(QtCore.QSize(450, 1080))
        self.sales_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.sales_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.sales_table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.bottom_buttons_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 70))

        # Labels
        self.to_date_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.from_date_label.setMaximumSize(QtCore.QSize(16777215, 70))

        # Buttons
        font = QtGui.QFont()
        font.setFamily('Helvetica')
        font.setPointSize(12)
        self.back_button.setFont(font)
        self.back_button.setMinimumSize(QtCore.QSize(160, 50))
        self.back_button.setMaximumSize(QtCore.QSize(190, 80))
        self.back_button.setStyleSheet('''QPushButton {
                                           background-color: white;
                                           color: black;
                                           border: 2px solid #C1C0C0;
                                       }
                                       
                                       QPushButton:hover:!pressed {
                                           background-color: #C1C0C0;
                                           color: white;
                                           font-weight: bold;
                                       }
                                       
                                       QPushButton:pressed {
                                           background-color: #C1C0C0;
                                           color: white;
                                           font-weight: bold;
                                       }''')

        self.delete_button.setFont(font)
        self.delete_button.setMinimumSize(QtCore.QSize(160, 50))
        self.delete_button.setMaximumSize(QtCore.QSize(180, 80))
        self.delete_button.setStyleSheet('''QPushButton {
                                             background-color: white;
                                             color: black;
                                             border: 2px solid #E25235;
                                         }
                                         
                                         QPushButton:hover:!pressed {
                                             background-color: #E25235;
                                             color: white;
                                             font-weight: bold;
                                         }
                                         
                                         QPushButton:pressed {
                                             background-color: #E25235;
                                             color: white;
                                             font-weight: bold;
                                         }''')

        self.update_list_button.setFont(font)
        self.update_list_button.setMinimumSize(QtCore.QSize(170, 50))
        self.update_list_button.setMaximumSize(QtCore.QSize(190, 70))

        self.undo_button.setFont(font)
        self.undo_button.setMinimumSize(QtCore.QSize(100, 50))
        self.undo_button.setMaximumSize(QtCore.QSize(130, 80))
        self.undo_button.setStyleSheet('''QPushButton {
                                             background-color: white;
                                             color: black;
                                             border: 2px solid #c79ce6;
                                         }
                                         
                                         QPushButton:hover:!pressed {
                                             background-color: #c79ce6;
                                             color: white;
                                             font-weight: bold;
                                         }
                                         
                                         QPushButton:pressed {
                                             background-color: #c79ce6;
                                             color: white;
                                             font-weight: bold;
                                         }''')

        # Inputs
        self.to_date_option.setMinimumSize(QtCore.QSize(170, 50))
        self.to_date_option.setMaximumSize(QtCore.QSize(190, 70))
        self.to_date_option.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(3000, 12, 31), QtCore.QTime(23, 59, 59)))
        self.to_date_option.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.to_date_option.setAlignment(QtCore.Qt.AlignCenter)
        self.to_date_option.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.to_date_option.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.to_date_option.setDate(QtCore.QDate(datetime.now().year, datetime.now().month, datetime.now().day))

        self.from_date_option.setMinimumSize(QtCore.QSize(170, 50))
        self.from_date_option.setMaximumSize(QtCore.QSize(190, 70))
        self.from_date_option.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(3000, 12, 31), QtCore.QTime(23, 59, 59)))
        self.from_date_option.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.from_date_option.setAlignment(QtCore.Qt.AlignCenter)
        self.from_date_option.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.from_date_option.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

        year = datetime.now().year
        month = datetime.now().month - 1
        if month == 1:
            year -= 1
            month = 12

        self.from_date_option.setDate(QtCore.QDate(year, month, datetime.now().day))

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.to_date_label.setText(_translate('MainWindow', 'Até'))
        self.from_date_label.setText(_translate('MainWindow', 'Desde'))
        self.purchases_label.setText(_translate('MainWindow', 'Compras'))
        self.sales_label.setText(_translate('MainWindow', 'Vendas'))
        self.update_list_button.setText(_translate('MainWindow', 'Atualizar Lista'))
        self.back_button.setText(_translate('MainWindow', 'Voltar'))
        self.delete_button.setText(_translate('MainWindow', 'Excluir'))
        self.undo_button.setText(_translate('MainWindow', 'Desfazer'))

    def create_structure(self):
        self.date_input_layout.addWidget(self.to_date_label)
        self.date_input_layout.addWidget(self.to_date_option)
        self.date_input_layout.addWidget(self.from_date_label)
        self.date_input_layout.addWidget(self.from_date_option)
        self.date_input_layout.addItem(
            QtWidgets.QSpacerItem(40, 60, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))
        self.date_input_layout.addWidget(self.update_list_button)
        self.date_input_layout.addItem(
            QtWidgets.QSpacerItem(20, 460, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred))

        self.tables_layout.addWidget(self.purchases_label, 0, 0, 1, 1)
        self.tables_layout.addWidget(self.purchases_table, 1, 0, 1, 1)
        self.tables_layout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum), 1, 1, 1, 1)
        self.tables_layout.addWidget(self.sales_label, 0, 2, 1, 1)
        self.tables_layout.addWidget(self.sales_table, 1, 2, 1, 1)

        self.bottom_buttons_layout.addWidget(self.delete_button)
        self.bottom_buttons_layout.addWidget(self.back_button)

        self.grid_layout.addWidget(self.tables_gridWidget, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.date_input_verticalWidget, 0, 1, 1, 1)
        self.grid_layout.addItem(
            QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred), 1, 0, 1,
            1)

        self.tables_gridWidget.setMinimumSize(QtCore.QSize(900, 470))

        self.undo_button_layout.addWidget(self.undo_button, QtCore.Qt.AlignRight)
        self.undo_button_layout.addItem(
            QtWidgets.QSpacerItem(980, 50, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))

        self.grid_layout.addWidget(self.undo_button_horizontalWidget, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.bottom_buttons_horizontalWidget, 2, 1, 1, 1)

    def define_actions(self):
        self.back_button.clicked.connect(self.clear_and_go_back)
        self.delete_button.clicked.connect(self.delete_register)
        self.update_list_button.clicked.connect(self.clear)
        self.undo_button.clicked.connect(self.undo_action)

    def clear_and_go_back(self):
        self.purchases_table.clear()
        self.sales_table.clear()
        self.back_signal.emit()

    def format_value(self, value):
        return locale.currency(float(value), grouping=True).split(' ')[1]

    def format_date(self, date):
        date = date.split('/')

        if len(date[0]) == 1:
            date[0] = '0' + date[0]

        if len(date[1]) == 1:
            date[1] = '0' + date[1]

        return '/'.join(date)

    def update_purchase_selection(self, row, *args):
        if row == self.previous_purchase_selection:
            self.previous_purchase_selection = None
            self.purchases_table.clearSelection()
        else:
            self.previous_purchase_selection = row

    def update_sale_selection(self, row, *args):
        if row == self.previous_sale_selection:
            self.previous_sale_selection = None
            self.sales_table.clearSelection()
        else:
            self.previous_sale_selection = row

    def clear(self):
        self.previous_sale_selection = None
        self.previous_purchase_selection = None

        self.purchases_table.clear()
        self.purchases_table.setRowCount(0)
        self.purchases_table.setColumnCount(3)
        self.purchases_table.setHorizontalHeaderLabels(('Nome', 'Valor', 'Data'))

        self.sales_table.clear()
        self.sales_table.setRowCount(0)
        self.sales_table.setColumnCount(3)
        self.sales_table.setHorizontalHeaderLabels(('Nome', 'Valor', 'Data'))

        max_value = self.consult_controller.get_max_purchase_value()
        max_value = 0 if max_value is None else max_value

        min_value = self.consult_controller.get_min_purchase_value()
        min_value = 0 if min_value is None else min_value

        result, purchases, message = self.consult_controller.get_purchases_by_value_and_date(min_value, max_value,
                                                                                             self.from_date_option.text(),
                                                                                             self.to_date_option.text())
        if result and purchases:
            self.purchases_table.setRowCount(len(purchases))
            for idx, (name, value, date) in enumerate(purchases):
                name_item = QtWidgets.QTableWidgetItem(name)
                name_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.purchases_table.setItem(idx, 0, name_item)

                value_item = QtWidgets.QTableWidgetItem(self.format_value(value))
                value_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.purchases_table.setItem(idx, 1, value_item)

                date_item = QtWidgets.QTableWidgetItem(self.format_date(date))
                date_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.purchases_table.setItem(idx, 2, date_item)

        max_value = self.consult_controller.get_max_sale_value()
        max_value = 0 if max_value is None else max_value

        min_value = self.consult_controller.get_min_sale_value()
        min_value = 0 if min_value is None else min_value

        result, sales, message = self.consult_controller.get_sales_by_value_and_date(min_value, max_value,
                                                                                     self.from_date_option.text(),
                                                                                     self.to_date_option.text())
        if result and sales:
            self.sales_table.setRowCount(len(sales))
            for idx, (name, value, date) in enumerate(sales):
                name_item = QtWidgets.QTableWidgetItem(name)
                name_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.sales_table.setItem(idx, 0, name_item)

                value_item = QtWidgets.QTableWidgetItem(self.format_value(value))
                value_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.sales_table.setItem(idx, 1, value_item)

                date_item = QtWidgets.QTableWidgetItem(self.format_date(date))
                date_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.sales_table.setItem(idx, 2, date_item)

    def undo_action(self):
        message = self.deletion_controller.undo()
        self.clear()
        self.show_message(message)

    def delete_register(self):
        if self.previous_purchase_selection is not None:
            if self.previous_sale_selection is not None:
                self.show_message('É permitido apenas uma transação por vez.\nDesmarque a compra ou a venda selecionada e tente novamente.')
                return
            else:
                transaction_type = 'purchase', 'compra'
                deleted_register_name = self.purchases_table.item(self.previous_purchase_selection, 0).text()
                deleted_register_value = self.purchases_table.item(self.previous_purchase_selection, 1).text()
                deleted_register_date = self.purchases_table.item(self.previous_purchase_selection, 2).text()

        else:
            if self.previous_sale_selection is None:
                self.show_message('Nenhuma transação selecionada.\nMarque uma compra ou uma venda e tente novamente.')
                return
            else:
                transaction_type = 'sale', 'venda'
                deleted_register_name = self.sales_table.item(self.previous_sale_selection, 0).text()
                deleted_register_value = self.sales_table.item(self.previous_sale_selection, 1).text()
                deleted_register_date = self.sales_table.item(self.previous_sale_selection, 2).text()

        confirmation_box = self.get_confirmation_box(transaction_type[1], deleted_register_name,
                                                     deleted_register_value, deleted_register_date)
        result = confirmation_box.exec()

        if result == 0:
            message = self.deletion_controller.delete(transaction_type[0], deleted_register_name,
                                                      deleted_register_value, deleted_register_date)
            self.clear()
            self.show_message(message)

    def show_message(self, text):
        self.dialog.setText('\n' + text + '\t\t\n')
        self.dialog.exec()

    def get_confirmation_box(self, transaction_type, transaction_name, transaction_value, transaction_date):
        confirm_box = QtWidgets.QMessageBox()
        confirm_box.setWindowTitle('Confirmação')
        confirm_box.setText(f'Tem certeza que deseja excluir esta {transaction_type}?\n'
                            f'\nDados da {transaction_type}:'
                            f'\n\t- Nome:  {transaction_name}'
                            f'\n\t- Valor:   {transaction_value}'
                            f'\n\t- Data:    {transaction_date}\n\n')

        confirm_box.addButton('Sim', QtWidgets.QMessageBox.YesRole)
        confirm_box.addButton('Não', QtWidgets.QMessageBox.NoRole)

        confirm_box.setStyleSheet('background-color:white;')

        return confirm_box
