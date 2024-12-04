import locale

locale.setlocale(locale.LC_MONETARY, '')
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from resources.qtslider import QRangeSlider

from ...controller.consult_controller import ConsultController


class PurchaseListPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(PurchaseListPage, self).__init__(*args)

        self.back_signal = back_signal
        self.controller = ConsultController()

        # Main
        self.gridLayout = QtWidgets.QGridLayout(self)

        self.filters_verticalWidget = QtWidgets.QWidget(self, *args)
        self.filters_layout = QtWidgets.QVBoxLayout(self.filters_verticalWidget)

        self.from_date_horizontalWidget = QtWidgets.QWidget(self.filters_verticalWidget, *args)
        self.from_date_layout = QtWidgets.QHBoxLayout(self.from_date_horizontalWidget)

        self.to_date_horizontalWidget = QtWidgets.QWidget(self.filters_verticalWidget, *args)
        self.to_date_layout = QtWidgets.QHBoxLayout(self.to_date_horizontalWidget)

        self.products_table = QtWidgets.QTableWidget(self)
        self.filter_buttons_layout = QtWidgets.QHBoxLayout()

        # Labels
        self.table_label = QtWidgets.QLabel(self)
        self.from_date_label = QtWidgets.QLabel(self.from_date_horizontalWidget)
        self.to_date_label = QtWidgets.QLabel(self.to_date_horizontalWidget)
        self.value_interval_label = QtWidgets.QLabel(self.filters_verticalWidget)
        self.comboBox_label = QtWidgets.QLabel(self.filters_verticalWidget)
        self.total_purchases_label = QtWidgets.QLabel(self)

        # Inputs
        self.product_name_input = QtWidgets.QLineEdit(self.filters_verticalWidget)
        self.from_date_input = QtWidgets.QDateEdit(self.from_date_horizontalWidget)
        self.to_date_input = QtWidgets.QDateEdit(self.to_date_horizontalWidget)
        self.value_slider = QRangeSlider(10, 100, self.filters_verticalWidget)
        self.order_by_comboBox = QtWidgets.QComboBox(self.filters_verticalWidget)

        # Buttons
        self.back_button = QtWidgets.QPushButton(self)
        self.apply_filters_button = QtWidgets.QPushButton(self.filters_verticalWidget)
        self.clear_filters_button = QtWidgets.QPushButton(self.filters_verticalWidget)

        self.setup_ui()
        self.translate_ui()
        self.create_structure()
        self.define_actions()

    def setup_ui(self):
        # Main
        self.products_table.verticalHeader().setVisible(False)
        self.products_table.horizontalHeader().setHighlightSections(False)
        self.products_table.setMinimumSize(QtCore.QSize(400, 400))
        self.products_table.setMaximumSize(QtCore.QSize(1080, 1080))
        self.products_table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.products_table.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.products_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.products_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.filters_verticalWidget.setMinimumSize(QtCore.QSize(290, 0))
        self.filters_verticalWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.filters_layout.setContentsMargins(QtCore.QMargins(5, 0, 5, 0))

        self.from_date_horizontalWidget.setMinimumSize(QtCore.QSize(0, 45))
        self.from_date_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 45))

        self.to_date_horizontalWidget.setMinimumSize(QtCore.QSize(0, 45))
        self.to_date_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 45))

        # Labels
        self.table_label.setMinimumSize(QtCore.QSize(0, 40))
        self.table_label.setMaximumSize(QtCore.QSize(16777215, 45))

        self.from_date_label.setMinimumSize(QtCore.QSize(0, 35))
        self.from_date_label.setMaximumSize(QtCore.QSize(16777215, 45))

        self.to_date_label.setMinimumSize(QtCore.QSize(0, 35))
        self.to_date_label.setMaximumSize(QtCore.QSize(16777215, 45))

        self.comboBox_label.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_label.setMaximumSize(QtCore.QSize(16777215, 45))

        self.total_purchases_label.setMinimumSize(QtCore.QSize(0, 35))
        self.total_purchases_label.setMaximumSize(QtCore.QSize(16777215, 45))

        # Inputs
        self.product_name_input.setMinimumSize(QtCore.QSize(0, 45))
        self.product_name_input.setMaximumSize(QtCore.QSize(16777215, 45))
        self.product_name_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))

        self.to_date_input.setMinimumSize(QtCore.QSize(100, 35))
        self.to_date_input.setAlignment(QtCore.Qt.AlignCenter)
        self.to_date_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.to_date_input.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.to_date_input.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.to_date_input.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(3000, 12, 31), QtCore.QTime(23, 59, 59)))
        self.to_date_input.setDate(QtCore.QDate(datetime.now().year, datetime.now().month, datetime.now().day))

        self.from_date_input.setMinimumSize(QtCore.QSize(100, 35))
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

        self.order_by_comboBox.setMinimumSize(QtCore.QSize(0, 35))
        self.order_by_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.order_by_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.order_by_comboBox.setStyleSheet('''QComboBox:item {
                                                    background-color: white;
                                                    selection-background-color: transparent;
                                                    color: black;
                                                }''')

        # Buttons
        self.apply_filters_button.setMinimumSize(QtCore.QSize(130, 40))
        self.apply_filters_button.setMaximumSize(QtCore.QSize(130, 50))
        self.apply_filters_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.apply_filters_button.setStyleSheet('''QPushButton {
                                                    background-color: white;
                                                    color: black;
                                                    border: 2px solid #cffaff;
                                                }
                                            
                                                QPushButton:hover:!pressed {
                                                    background-color: #cffaff;
                                                    font-weight: bold;
                                                }
                                                
                                                QPushButton:pressed {
                                                    background-color: #cffaff;
                                                    font-weight: bold;
                                                }''')

        self.clear_filters_button.setMinimumSize(QtCore.QSize(130, 40))
        self.clear_filters_button.setMaximumSize(QtCore.QSize(130, 50))
        self.clear_filters_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_filters_button.setStyleSheet('''QPushButton {
                                                    background-color: white;
                                                    color: black;
                                                    border: 2px solid #f2bfbf;
                                                }
                                                
                                                QPushButton:hover:!pressed {
                                                    background-color: #f2bfbf;
                                                    font-weight: bold;
                                                }
                                                
                                                QPushButton:pressed {
                                                    background-color: #f2bfbf;
                                                    font-weight: bold;
                                                }''')

        self.back_button.setMinimumSize(QtCore.QSize(180, 70))
        self.back_button.setMaximumSize(QtCore.QSize(180, 70))
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

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.table_label.setText(_translate('MainWindow', 'Lista de Compras'))
        self.total_purchases_label.setText(_translate('MainWindow', 'Total de compras: R$ 0,00'))
        self.back_button.setText(_translate('MainWindow', 'Voltar'))
        self.product_name_input.setPlaceholderText(_translate('Form', 'Nome do produto'))
        self.from_date_label.setText(_translate('MainWindow', 'Desde'))
        self.to_date_label.setText(_translate('MainWindow', 'Até'))
        self.value_interval_label.setText(_translate('MainWindow', 'Intervalo de valor desejado'))
        self.comboBox_label.setText(_translate('MainWindow', 'Ordenar por'))
        self.order_by_comboBox.addItem(_translate('MainWindow', 'Data'))
        self.order_by_comboBox.addItem(_translate('MainWindow', 'Valor'))
        self.order_by_comboBox.addItem(_translate('MainWindow', 'Mais vendido'))
        self.order_by_comboBox.addItem(_translate('MainWindow', 'Menos vendido'))
        # self.order_by_comboBox.addItem(_translate('MainWindow', 'Maior lucro'))
        # self.order_by_comboBox.addItem(_translate('MainWindow', 'Menor lucro'))
        self.apply_filters_button.setText(_translate('MainWindow', 'Aplicar Filtros'))
        self.clear_filters_button.setText(_translate('MainWindow', 'Limpar Filtros'))

    def create_structure(self):
        self.filters_layout.addWidget(self.product_name_input, alignment=QtCore.Qt.AlignVCenter)

        self.filters_layout.addItem(
            QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))

        self.from_date_layout.addWidget(self.from_date_label, alignment=QtCore.Qt.AlignVCenter)
        self.from_date_layout.addWidget(self.from_date_input, alignment=QtCore.Qt.AlignVCenter)
        self.to_date_layout.addWidget(self.to_date_label, alignment=QtCore.Qt.AlignVCenter)
        self.to_date_layout.addWidget(self.to_date_input, alignment=QtCore.Qt.AlignVCenter)
        self.filters_layout.addWidget(self.from_date_horizontalWidget, alignment=QtCore.Qt.AlignVCenter)
        self.filters_layout.addWidget(self.to_date_horizontalWidget, alignment=QtCore.Qt.AlignVCenter)

        self.filters_layout.addItem(
            QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))

        self.filters_layout.addWidget(self.value_interval_label, alignment=QtCore.Qt.AlignVCenter)
        self.filters_layout.addWidget(self.value_slider, alignment=QtCore.Qt.AlignVCenter)

        self.filters_layout.addItem(
            QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))

        self.filters_layout.addWidget(self.comboBox_label, alignment=QtCore.Qt.AlignVCenter)
        self.filters_layout.addWidget(self.order_by_comboBox, alignment=QtCore.Qt.AlignVCenter)

        self.filters_layout.addItem(
            QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))

        self.filter_buttons_layout.addWidget(self.apply_filters_button, alignment=QtCore.Qt.AlignVCenter)
        self.filter_buttons_layout.addWidget(self.clear_filters_button, alignment=QtCore.Qt.AlignVCenter)
        self.filters_layout.addLayout(self.filter_buttons_layout)

        self.filters_layout.addItem(
            QtWidgets.QSpacerItem(20, 220, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))

        self.gridLayout.addWidget(self.table_label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.products_table, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.total_purchases_label, 2, 0, alignment=QtCore.Qt.AlignHCenter)

        self.gridLayout.addWidget(self.filters_verticalWidget, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.back_button, 3, 1, alignment=QtCore.Qt.AlignHCenter)

    def define_actions(self):
        self.back_button.clicked.connect(self.clear_and_go_back)
        self.apply_filters_button.clicked.connect(self.apply_filters)
        self.clear_filters_button.clicked.connect(self.clear)

    def clear_and_go_back(self):
        self.products_table.clear()
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
        year = datetime.now().year
        month = datetime.now().month - 1
        if month == 1:
            year -= 1
            month = 12

        self.from_date_input.setDate(QtCore.QDate(year, month, datetime.now().day))
        self.to_date_input.setDate(QtCore.QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        self.order_by_comboBox.setCurrentIndex(0)
        self.product_name_input.clear()

        min_purchase = self.controller.get_min_purchase_value()
        min_purchase = 0 if min_purchase is None else min_purchase

        max_purchase = self.controller.get_max_purchase_value()
        max_purchase = 0 if max_purchase is None else max_purchase

        self.value_slider.setMinMax(min_purchase, max_purchase)

        self.products_table.setColumnCount(3)
        self.products_table.setHorizontalHeaderLabels(('Nome', 'Preco', 'Data'))
        for i in range(self.products_table.columnCount()):
            self.products_table.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        result, purchases, message = self.controller.get_purchases_by_value_and_date(min_purchase, max_purchase,
                                                                                     self.from_date_input.text(),
                                                                                     self.to_date_input.text())
        if result and purchases:
            self.populate_table(purchases)

    def apply_filters(self):
        min_value = self.value_slider.min()
        max_value = self.value_slider.max()

        name = self.product_name_input.text()

        if self.order_by_comboBox.currentText().lower() == 'mais vendido':
            if name:
                result, purchases, message = self.controller.get_purchases_amount_by_name_and_value_and_date(name, min_value, max_value, self.from_date_input.text(), self.to_date_input.text())
            else:
                result, purchases, message = self.controller.get_purchases_amount_by_value_and_date(min_value, max_value, self.from_date_input.text(), self.to_date_input.text())

        elif self.order_by_comboBox.currentText().lower() == 'menos vendido':
            if name:
                result, purchases, message = self.controller.get_purchases_amount_by_name_and_value_and_date(name, min_value, max_value, self.from_date_input.text(), self.to_date_input.text())
            else:
                result, purchases, message = self.controller.get_purchases_amount_by_value_and_date(min_value, max_value, self.from_date_input.text(), self.to_date_input.text())
            purchases.reverse()

        elif self.order_by_comboBox.currentText().lower() == 'valor':
            if name:
                result, purchases, message = self.controller.get_purchases_by_name_and_value_and_date(name, min_value, max_value, self.from_date_input.text(), self.to_date_input.text())
            else:
                result, purchases, message = self.controller.get_purchases_by_value_and_date(min_value, max_value, self.from_date_input.text(), self.to_date_input.text())

            purchases = sorted(purchases, key=lambda pur: pur[1])

        else:
            if name:
                result, purchases, message = self.controller.get_purchases_by_name_and_value_and_date(name, min_value, max_value, self.from_date_input.text(), self.to_date_input.text())
            else:
                result, purchases, message = self.controller.get_purchases_by_value_and_date(min_value, max_value, self.from_date_input.text(), self.to_date_input.text())

        self.populate_table(purchases)

    def populate_table(self, purchases):
        if self.order_by_comboBox.currentText().lower() not in ['data', 'valor']:
            new_value_text = self.total_purchases_label.text().split(':')[0] + ': R$ ' + self.format_value(0)
            self.products_table.setColumnCount(2)
            self.products_table.setHorizontalHeaderLabels(('Nome', 'Quantidade'))
            for i in range(self.products_table.columnCount()):
                self.products_table.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        else:
            new_value_text = self.total_purchases_label.text().split(':')[0] + ': R$ ' + self.format_value(sum([value for _, value, _ in purchases]))
            self.products_table.setColumnCount(3)
            self.products_table.setHorizontalHeaderLabels(('Nome', 'Preco', 'Data'))
            for i in range(self.products_table.columnCount()):
                self.products_table.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        self.total_purchases_label.setText(new_value_text)
        self.products_table.setRowCount(len(purchases))

        for idx, (one, two, three) in enumerate(purchases):
            if self.order_by_comboBox.currentText().lower() not in ['data', 'valor']:
                name_item = QtWidgets.QTableWidgetItem(two)
                name_item.setTextAlignment(QtCore.Qt.AlignCenter)

                quantity_item = QtWidgets.QTableWidgetItem(str(one))
                quantity_item.setTextAlignment(QtCore.Qt.AlignCenter)

                self.products_table.setItem(idx, 0, name_item)
                self.products_table.setItem(idx, 1, quantity_item)
            else:
                name_item = QtWidgets.QTableWidgetItem(one)
                name_item.setTextAlignment(QtCore.Qt.AlignCenter)

                value_item = QtWidgets.QTableWidgetItem(self.format_value(two))
                value_item.setTextAlignment(QtCore.Qt.AlignCenter)

                date_item = QtWidgets.QTableWidgetItem(self.format_date(three))
                date_item.setTextAlignment(QtCore.Qt.AlignCenter)

                self.products_table.setItem(idx, 0, name_item)
                self.products_table.setItem(idx, 1, value_item)
                self.products_table.setItem(idx, 2, date_item)

