import re
import locale
locale.setlocale(locale.LC_MONETARY, '')
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

from ...controller.registration_controller import RegistrationController


class RegistrationPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(RegistrationPage, self).__init__(*args)

        self.controller = RegistrationController()
        self.base_string_value = '0,00'
        self.back_signal = back_signal
        self.dialog = QtWidgets.QMessageBox(self)
        self.dialog.setWindowTitle('Aviso')

        # Declaring main objects
        self.grid_layout = QtWidgets.QGridLayout(self)

        self.form = QtWidgets.QWidget(self, *args)
        self.form_layout = QtWidgets.QGridLayout(self.form)

        self.purchase_sale_horizontalWidget = QtWidgets.QWidget(self.form, *args)
        self.purchase_sale_layout = QtWidgets.QHBoxLayout(self.purchase_sale_horizontalWidget)

        self.coin_input_horizontalWidget = QtWidgets.QWidget(self.form, *args)
        self.coin_input_layout = QtWidgets.QHBoxLayout(self.coin_input_horizontalWidget)

        self.bottom_buttons_horizontalWidget = QtWidgets.QWidget(self, *args)
        self.bottom_buttons_layout = QtWidgets.QHBoxLayout(self.bottom_buttons_horizontalWidget)

        self.register_back_buttons_widget = QtWidgets.QWidget(self, *args)
        self.register_back_buttons = QtWidgets.QHBoxLayout(self.register_back_buttons_widget)

        # Declaring Labels
        self.page_title = QtWidgets.QLabel(self)
        self.transaction_label = QtWidgets.QLabel(self.form)
        self.date_label = QtWidgets.QLabel(self.form)
        self.value_label = QtWidgets.QLabel(self.form)
        self.product_name_label = QtWidgets.QLabel(self.form)
        self.coin_label = QtWidgets.QLabel(self.coin_input_horizontalWidget)

        # Declaring buttons
        self.register_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)
        self.back_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)
        self.undo_button = QtWidgets.QPushButton(self)

        # Declaring inputs
        self.product_name_input = QtWidgets.QTextEdit(self.form)
        self.date_input = QtWidgets.QDateEdit(self.form)
        self.value_input = QtWidgets.QTextEdit(self.coin_input_horizontalWidget)
        self.purchase_option = QtWidgets.QRadioButton(self.purchase_sale_horizontalWidget)
        self.sale_option = QtWidgets.QRadioButton(self.purchase_sale_horizontalWidget)

        # Building UI
        self.setup_ui()
        self.translate_ui()
        self.create_structure()
        self.define_actions()

    def setup_ui(self):
        # Main
        self.form.setMinimumSize(QtCore.QSize(300, 500))
        self.purchase_sale_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.coin_input_horizontalWidget.setMaximumSize(QtCore.QSize(270, 70))
        self.bottom_buttons_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 70))

        self.register_back_buttons.setContentsMargins(0, 0, 0, 0)

        # Labels
        self.page_title.setMaximumSize(QtCore.QSize(16777215, 70))
        self.transaction_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.value_label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.product_name_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.date_label.setMaximumSize(QtCore.QSize(16777215, 70))

        # Buttons
        font = QtGui.QFont()
        font.setFamily('Helvetica')
        font.setPointSize(12)
        self.register_button.setFont(font)
        self.register_button.setMinimumSize(QtCore.QSize(150, 50))
        self.register_button.setMaximumSize(QtCore.QSize(180, 70))
        self.register_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_button.setStyleSheet('''QPushButton {
                                               background-color: white;
                                               color: black;
                                               border: 2px solid #4CAF50;
                                           }
                                           
                                           QPushButton:hover:!pressed {
                                               background-color: #4CAF50;
                                               color: white;
                                               font-weight: bold;
                                           }
                                           
                                           QPushButton:pressed {
                                               background-color: #4CAF50;
                                               color: white;
                                               font-weight: bold;
                                           }''')

        self.back_button.setFont(font)
        self.back_button.setMinimumSize(QtCore.QSize(160, 50))
        self.back_button.setMaximumSize(QtCore.QSize(180, 80))
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
        self.date_input.setMinimumSize(QtCore.QSize(120, 0))
        self.date_input.setMaximumSize(QtCore.QSize(180, 50))
        self.date_input.setAlignment(QtCore.Qt.AlignCenter)
        self.date_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.date_input.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.date_input.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1990, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_input.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(3000, 12, 31), QtCore.QTime(23, 59, 59)))
        self.date_input.setDate(QtCore.QDate(datetime.now().year, datetime.now().month, datetime.now().day))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHeightForWidth(self.product_name_input.sizePolicy().hasHeightForWidth())
        self.product_name_input.setSizePolicy(size_policy)
        self.product_name_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.product_name_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))

        size_policy.setHeightForWidth(self.value_input.sizePolicy().hasHeightForWidth())
        self.value_input.setSizePolicy(size_policy)
        self.value_input.setMinimumSize(QtCore.QSize(220, 35))
        self.value_input.setMaximumSize(QtCore.QSize(260, 35))
        self.value_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.value_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.value_input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        size_policy.setHeightForWidth(self.purchase_option.sizePolicy().hasHeightForWidth())
        self.purchase_option.setSizePolicy(size_policy)
        self.purchase_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        size_policy.setHeightForWidth(self.sale_option.sizePolicy().hasHeightForWidth())
        self.sale_option.setSizePolicy(size_policy)
        self.sale_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.page_title.setText(
            _translate('MainWindow', 'Nesta área você irá cadastrar uma Compra OU Venda referente ao dia informado'))
        self.register_button.setText(_translate('MainWindow', 'Cadastrar'))
        self.back_button.setText(_translate('MainWindow', 'Voltar'))
        self.undo_button.setText(_translate('MainWindow', 'Desfazer'))
        self.product_name_input.setPlaceholderText(_translate('MainWindow', 'Nome do produto'))
        self.transaction_label.setText(_translate('MainWindow', 'Marque a opção correspondente à transação:'))
        self.date_label.setText(_translate('MainWindow', 'Informe a data da transação'))
        self.value_label.setText(_translate('MainWindow', 'Informe o valor da transação'))
        self.product_name_label.setText(_translate('MainWindow', 'Informe o nome do produto:'))
        self.coin_label.setText(_translate('MainWindow', 'R$'))
        self.value_input.setPlaceholderText(_translate('MainWindow', '0,00'))
        self.purchase_option.setText(_translate('MainWindow', 'Compra'))
        self.sale_option.setText(_translate('MainWindow', 'Venda'))

    def create_structure(self):
        self.purchase_sale_layout.addWidget(self.purchase_option)
        self.purchase_sale_layout.addWidget(self.sale_option)

        self.coin_input_layout.addWidget(self.coin_label)
        self.coin_input_layout.addWidget(self.value_input)

        self.form_layout.addWidget(self.transaction_label, 0, 0, 1, 1)
        self.form_layout.addWidget(self.purchase_sale_horizontalWidget, 1, 0, 1, 1)
        self.form_layout.addWidget(self.date_label, 2, 0, 1, 1)
        self.form_layout.addWidget(self.date_input, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.form_layout.addWidget(self.product_name_label, 7, 0, 1, 1)
        self.form_layout.addWidget(self.product_name_input, 8, 0, 1, 1)
        self.form_layout.addWidget(self.value_label, 10, 0, 1, 1)
        self.form_layout.addWidget(self.coin_input_horizontalWidget, 11, 0, 1, 1)
        self.form_layout.addItem(QtWidgets.QSpacerItem(20, 110, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum), 12, 0, 1, 1)

        self.register_back_buttons.addWidget(self.register_button)
        self.register_back_buttons.addWidget(self.back_button)
        self.bottom_buttons_layout.addItem(QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum))
        self.bottom_buttons_layout.addWidget(self.undo_button)
        self.bottom_buttons_layout.addWidget(self.register_back_buttons_widget, alignment=QtCore.Qt.AlignRight)

        self.grid_layout.addWidget(self.page_title, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.form, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.bottom_buttons_horizontalWidget, 2, 1, 1, 1)

    def define_actions(self):
        self.value_input.keyPressEvent = self.handle_key_pressed
        self.register_button.clicked.connect(self.register_transaction)
        self.back_button.clicked.connect(self.back_signal.emit)
        self.undo_button.clicked.connect(self.undo_action)

    def handle_key_pressed(self, event):
        text = self.value_input.toPlainText().replace(',', '.').replace('.', '')
        key = event.key()
        if 57 >= key >= 48:
            text = re.sub('\A0*', '', text) # type: ignore
            new_char = chr(key)
            self.format(text, new_char)

        elif key == QtCore.Qt.Key_Backspace or key == QtCore.Qt.Key_Delete:
            text = text[:-1]
            self.format(text, '')

    def format(self, text, new_char):
        text = text + new_char

        if len(text) == 0:
            text = '0.0'

        elif len(text) == 1:
            text = '0.0' + text

        elif len(text) == 2:
            text = '0.' + text

        else:
            text = text[:-2] + '.' + text[-2:]

        a = locale.currency(float(text), grouping=True).split(' ')[1]
        self.value_input.setText(a)

    def undo_action(self):
        message = self.controller.undo()
        self.clear()
        self.show_message(message)

    def register_transaction(self):
        if self.purchase_option.isChecked():
            transaction_type = 'purchase'

        elif self.sale_option.isChecked():
            transaction_type = 'sale'

        else:
            self.show_message('\nA transação não foi classificada em Compra ou Venda. Classifique e tente novamente.\t\t\n')
            return

        product_name = self.product_name_input.toPlainText()
        if not product_name.replace('\t', '').replace(' ', ''):
            self.show_message('\nNenhum nome foi dado para o produto comprado/vendido. Insira um nome e tente novamente.\t\t\n')
            self.product_name_input.setFocus(True)
            return

        value = self.value_input.toPlainText().replace('.', '').replace(',', '.')
        if not re.sub('0*', '', value.replace('.', '')):
            self.show_message('\nNenhum valor foi atribuído à transação. Insira um valor e tente novamente.\t\t\n')
            self.value_input.setFocus(True)
            return
        
        message = self.controller.register(transaction_type, product_name, value, self.date_input.text())
        self.clear()
        self.show_message(message)

    def clear(self):
        self.sale_option.setAutoExclusive(False)
        self.purchase_option.setAutoExclusive(False)

        self.sale_option.setChecked(False)
        self.purchase_option.setChecked(False)

        self.sale_option.setAutoExclusive(True)
        self.purchase_option.setAutoExclusive(True)

        self.product_name_input.clear()
        self.value_input.clear()
        self.date_input.setDate(QtCore.QDate(datetime.now().year, datetime.now().month, datetime.now().day))

    def show_message(self, text):
        self.dialog.setText('\n' + text + '\t\t\n')
        self.dialog.exec()
