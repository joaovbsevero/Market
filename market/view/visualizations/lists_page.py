import locale
locale.setlocale(locale.LC_MONETARY, '')
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

from ...controller.consult_controller import ConsultController


class ListsPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(ListsPage, self).__init__(*args)

        self.back_signal = back_signal
        self.controller = ConsultController()

        # Main
        self.grid_layout = QtWidgets.QGridLayout(self)

        self.date_input_verticalWidget = QtWidgets.QWidget(self, *args)
        self.date_input_layout = QtWidgets.QVBoxLayout(self.date_input_verticalWidget)

        self.tables_gridWidget = QtWidgets.QWidget(self, *args)
        self.tables_layout = QtWidgets.QGridLayout(self.tables_gridWidget)

        self.purchases_table = QtWidgets.QTableWidget(self.tables_gridWidget)
        self.sales_table = QtWidgets.QTableWidget(self.tables_gridWidget)

        self.total_purchases_horizontalWidget = QtWidgets.QWidget(self.tables_gridWidget, *args)
        self.total_purchases_layout = QtWidgets.QHBoxLayout(self.total_purchases_horizontalWidget)

        self.total_sales_horizontalWidget = QtWidgets.QWidget(self.tables_gridWidget, *args)
        self.total_sales_layout = QtWidgets.QHBoxLayout(self.total_sales_horizontalWidget)

        # Labels
        self.to_date_label = QtWidgets.QLabel(self.date_input_verticalWidget)
        self.from_date_label = QtWidgets.QLabel(self.date_input_verticalWidget)

        self.purchases_label = QtWidgets.QLabel(self.tables_gridWidget)
        self.sales_label = QtWidgets.QLabel(self.tables_gridWidget)

        self.total_purchases_label = QtWidgets.QLabel(self.total_purchases_horizontalWidget)
        self.total_purchases_value_label = QtWidgets.QLabel(self.total_purchases_horizontalWidget)

        self.total_sales_label = QtWidgets.QLabel(self.total_sales_horizontalWidget)
        self.total_sales_value_label = QtWidgets.QLabel(self.total_sales_horizontalWidget)

        # Buttons
        self.back_button = QtWidgets.QPushButton(self)
        self.update_list_button = QtWidgets.QPushButton(self)

        # Inputs
        self.to_date_input = QtWidgets.QDateEdit(self.date_input_verticalWidget)
        self.from_date_input = QtWidgets.QDateEdit(self.date_input_verticalWidget)

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
        self.purchases_table.setMinimumSize(QtCore.QSize(400, 400))
        self.purchases_table.setMaximumSize(QtCore.QSize(450, 1080))
        self.purchases_table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.purchases_table.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.purchases_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.purchases_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.purchases_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.purchases_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.purchases_table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.sales_table.setColumnCount(3)
        self.sales_table.verticalHeader().setVisible(False)
        self.sales_table.horizontalHeader().setHighlightSections(False)
        self.sales_table.setMinimumSize(QtCore.QSize(400, 400))
        self.sales_table.setMaximumSize(QtCore.QSize(450, 1080))
        self.sales_table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sales_table.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.sales_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.sales_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sales_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.sales_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.sales_table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHeightForWidth(self.total_purchases_horizontalWidget.sizePolicy().hasHeightForWidth())
        self.total_purchases_horizontalWidget.setSizePolicy(size_policy)
        self.total_purchases_horizontalWidget.setMinimumSize(QtCore.QSize(460, 0))
        self.total_purchases_horizontalWidget.setMaximumSize(QtCore.QSize(500, 70))

        size_policy.setHeightForWidth(self.total_sales_horizontalWidget.sizePolicy().hasHeightForWidth())
        self.total_sales_horizontalWidget.setSizePolicy(size_policy)
        self.total_sales_horizontalWidget.setMinimumSize(QtCore.QSize(460, 0))
        self.total_sales_horizontalWidget.setMaximumSize(QtCore.QSize(500, 70))

        # Labels
        self.to_date_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.from_date_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.total_purchases_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.total_purchases_value_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.total_sales_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.total_sales_value_label.setMaximumSize(QtCore.QSize(16777215, 70))

        # Buttons
        font = QtGui.QFont()
        font.setFamily('Helvetica')
        font.setPointSize(12)
        self.back_button.setFont(font)
        self.back_button.setMinimumSize(QtCore.QSize(160, 50))
        self.back_button.setMaximumSize(QtCore.QSize(190, 80))
        self.back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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

        self.update_list_button.setFont(font)
        self.update_list_button.setMinimumSize(QtCore.QSize(160, 50))
        self.update_list_button.setMaximumSize(QtCore.QSize(190, 70))
        self.update_list_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Inputs
        self.to_date_input.setMinimumSize(QtCore.QSize(170, 50))
        self.to_date_input.setMaximumSize(QtCore.QSize(190, 70))
        self.to_date_input.setAlignment(QtCore.Qt.AlignCenter)
        self.to_date_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.to_date_input.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.to_date_input.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.to_date_input.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(3000, 12, 31), QtCore.QTime(23, 59, 59)))
        self.to_date_input.setDate(QtCore.QDate(datetime.now().year, datetime.now().month, datetime.now().day))

        self.from_date_input.setMinimumSize(QtCore.QSize(170, 50))
        self.from_date_input.setMaximumSize(QtCore.QSize(190, 70))
        self.from_date_input.setAlignment(QtCore.Qt.AlignCenter)
        self.from_date_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.from_date_input.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.from_date_input.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.from_date_input.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(3000, 12, 31), QtCore.QTime(23, 59, 59)))

        year = datetime.now().year
        month = datetime.now().month - 1
        if month == 1:
            year -= 1
            month = 12

        self.from_date_input.setDate(QtCore.QDate(year, month, datetime.now().day))

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.to_date_label.setText(_translate('MainWindow', 'Até'))
        self.from_date_label.setText(_translate('MainWindow', 'Desde'))
        self.purchases_label.setText(_translate('MainWindow', 'Compras'))
        self.sales_label.setText(_translate('MainWindow', 'Vendas'))
        self.back_button.setText(_translate('MainWindow', 'Voltar'))
        self.update_list_button.setText(_translate('MainWindow', 'Atualizar Lista'))
        self.total_purchases_label.setText(_translate('MainWindow', 'Total de Compras:  R$'))
        self.total_purchases_value_label.setText('0,00')
        self.total_sales_label.setText(_translate('MainWindow', 'Total de Vendas:  R$'))
        self.total_sales_value_label.setText('0,00')

    def create_structure(self):
        self.date_input_layout.addWidget(self.to_date_label)
        self.date_input_layout.addWidget(self.to_date_input)
        self.date_input_layout.addWidget(self.from_date_label)
        self.date_input_layout.addWidget(self.from_date_input)
        self.date_input_layout.addWidget(self.update_list_button)
        self.date_input_layout.addItem(QtWidgets.QSpacerItem(20, 460, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred))

        self.total_purchases_layout.addWidget(self.total_purchases_label)
        self.total_purchases_layout.addWidget(self.total_purchases_value_label)
        self.total_sales_layout.addWidget(self.total_sales_label)
        self.total_sales_layout.addWidget(self.total_sales_value_label)

        self.tables_layout.addWidget(self.purchases_label, 0, 0, 1, 1)
        self.tables_layout.addWidget(self.purchases_table, 1, 0, 1, 1)
        self.tables_layout.addWidget(self.total_purchases_horizontalWidget, 2, 0, 1, 1)
        self.tables_layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum), 1, 1, 1, 1)
        self.tables_layout.addWidget(self.sales_label, 0, 2, 1, 1)
        self.tables_layout.addWidget(self.sales_table, 1, 2, 1, 1)
        self.tables_layout.addWidget(self.total_sales_horizontalWidget, 2, 2, 1, 1)

        self.grid_layout.addWidget(self.tables_gridWidget, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.date_input_verticalWidget, 0, 1, 1, 1)
        self.grid_layout.addItem(QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred), 1, 0, 1, 1)
        self.grid_layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred), 2, 0, 1, 1)
        self.grid_layout.addWidget(self.back_button, 2, 1, 1, 1)

    def define_actions(self):
        self.back_button.clicked.connect(self.clear_and_go_back)
        self.update_list_button.clicked.connect(self.clear)

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

    def clear(self):
        self.purchases_table.clear()
        self.purchases_table.setRowCount(0)
        self.purchases_table.setHorizontalHeaderLabels(('Nome', 'Valor', 'Data'))

        self.sales_table.clear()
        self.sales_table.setRowCount(0)
        self.sales_table.setHorizontalHeaderLabels(('Nome', 'Valor', 'Data'))

        max_value = self.controller.get_max_purchase_value()
        max_value = 0 if max_value is None else max_value

        min_value = self.controller.get_min_purchase_value()
        min_value = 0 if min_value is None else min_value

        result, purchases, message = self.controller.get_purchases_by_value_and_date(min_value, max_value, self.from_date_input.text(), self.to_date_input.text())
        if result and purchases:
            self.total_purchases_value_label.setText(self.format_value(sum([value for _, value, _ in purchases])))

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
        else:
            self.total_purchases_value_label.setText(self.format_value(0))

        max_value = self.controller.get_max_sale_value()
        max_value = 0 if max_value is None else max_value

        min_value = self.controller.get_min_sale_value()
        min_value = 0 if min_value is None else min_value

        result, sales, message = self.controller.get_sales_by_value_and_date(min_value, max_value, self.from_date_input.text(), self.to_date_input.text())
        if result and sales:
            self.total_sales_value_label.setText(self.format_value(sum([value for _, value, _ in sales])))

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

        else:
            self.total_sales_value_label.setText(self.format_value(0))
