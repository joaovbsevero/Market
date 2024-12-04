import locale
locale.setlocale(locale.LC_MONETARY, '')
from PyQt5 import QtCore, QtGui, QtWidgets

from ...controller.edition_controller import EditionController


class EditionPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(EditionPage, self).__init__(*args)

        self.transaction_type = 'None'
        self.back_signal = back_signal
        self.edition_controller = EditionController()
        self.dialog = QtWidgets.QMessageBox(self)
        self.dialog.setWindowTitle('Aviso')

        # Main
        self.gridLayout = QtWidgets.QGridLayout(self)

        self.old_register_verticalWidget = QtWidgets.QWidget(self, *args)
        self.old_register_layout = QtWidgets.QVBoxLayout(self.old_register_verticalWidget)

        self.old_register_type_horizontalWidget = QtWidgets.QWidget(self.old_register_verticalWidget, *args)
        self.old_register_type_layout = QtWidgets.QHBoxLayout(self.old_register_type_horizontalWidget)

        self.old_register_name_horizontalWidget = QtWidgets.QWidget(self.old_register_verticalWidget, *args)
        self.old_register_name_layout = QtWidgets.QHBoxLayout(self.old_register_name_horizontalWidget)

        self.old_register_value_horizontalWidget = QtWidgets.QWidget(self.old_register_verticalWidget, *args)
        self.old_register_value_layout = QtWidgets.QHBoxLayout(self.old_register_value_horizontalWidget)

        self.old_register_date_horizontalWidget = QtWidgets.QWidget(self.old_register_verticalWidget, *args)
        self.old_register_date_layout = QtWidgets.QHBoxLayout(self.old_register_date_horizontalWidget)

        self.new_register_verticalWidget = QtWidgets.QWidget(self, *args)
        self.new_register_layout = QtWidgets.QVBoxLayout(self.new_register_verticalWidget)

        self.new_register_type_horizontalWidget = QtWidgets.QWidget(self.new_register_verticalWidget, *args)
        self.new_register_type_layout = QtWidgets.QHBoxLayout(self.new_register_type_horizontalWidget)

        self.new_register_name_horizontalWidget = QtWidgets.QWidget(self.new_register_verticalWidget, *args)
        self.new_register_name_layout = QtWidgets.QHBoxLayout(self.new_register_name_horizontalWidget)

        self.new_register_value_horizontalWidget = QtWidgets.QWidget(self.new_register_verticalWidget, *args)
        self.new_register_value_layout = QtWidgets.QHBoxLayout(self.new_register_value_horizontalWidget)

        self.new_register_date_horizontalWidget = QtWidgets.QWidget(self.new_register_verticalWidget, *args)
        self.new_register_date_layout = QtWidgets.QHBoxLayout(self.new_register_date_horizontalWidget)

        self.bottom_buttons_horizontalWidget = QtWidgets.QWidget(self, *args)
        self.bottom_buttons_layout = QtWidgets.QHBoxLayout(self.bottom_buttons_horizontalWidget)

        # Labels
        self.new_register_label = QtWidgets.QLabel(self)
        self.old_register_label = QtWidgets.QLabel(self)

        self.old_register_type_label = QtWidgets.QLabel(self.old_register_type_horizontalWidget)
        self.old_register_type_value = QtWidgets.QLabel(self.old_register_type_horizontalWidget)

        self.old_register_name_label = QtWidgets.QLabel(self.old_register_name_horizontalWidget)
        self.old_register_name_value = QtWidgets.QLabel(self.old_register_name_horizontalWidget)

        self.old_register_value_label = QtWidgets.QLabel(self.old_register_value_horizontalWidget)
        self.old_register_value_value = QtWidgets.QLabel(self.old_register_value_horizontalWidget)

        self.old_register_date_label = QtWidgets.QLabel(self.old_register_date_horizontalWidget)
        self.old_register_date_value = QtWidgets.QLabel(self.old_register_date_horizontalWidget)

        self.new_register_type_label = QtWidgets.QLabel(self.new_register_type_horizontalWidget)
        self.new_register_type_value = QtWidgets.QLineEdit(self.new_register_type_horizontalWidget)
        self.new_register_name_label = QtWidgets.QLabel(self.new_register_name_horizontalWidget)
        self.new_register_value_label = QtWidgets.QLabel(self.new_register_value_horizontalWidget)
        self.new_register_date_label = QtWidgets.QLabel(self.new_register_date_horizontalWidget)

        # Buttons
        self.edit_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)
        self.cancel_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)

        # Inputs
        self.new_register_name_input = QtWidgets.QLineEdit(self.new_register_name_horizontalWidget)
        self.new_register_value_input = QtWidgets.QLineEdit(self.new_register_value_horizontalWidget)
        self.new_register_date_input = QtWidgets.QDateEdit(self.new_register_date_horizontalWidget)

        # Building UI
        self.setup_ui()
        self.build_structure()
        self.define_actions()

    def setup_ui(self):
        font = QtGui.QFont()
        font.setFamily('Helvetica')
        font.setPointSize(12)

        # Main
        self.old_register_verticalWidget.setStyleSheet('background-color: rgb(243, 243, 243);')
        self.old_register_verticalWidget.setMinimumSize(QtCore.QSize(450, 16777215))
        self.old_register_verticalWidget.setMaximumSize(QtCore.QSize(550, 16777215))
        self.old_register_verticalWidget.setContentsMargins(80, 80, 80, 80)

        self.new_register_verticalWidget.setStyleSheet('background-color: rgb(243, 243, 243);')
        self.new_register_verticalWidget.setMinimumSize(QtCore.QSize(450, 16777215))
        self.new_register_verticalWidget.setMaximumSize(QtCore.QSize(550, 16777215))
        self.new_register_verticalWidget.setContentsMargins(80, 80, 80, 80)

        self.bottom_buttons_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 70))

        # Labels
        self.old_register_label.setMinimumSize(QtCore.QSize(100, 45))
        self.old_register_label.setMaximumSize(QtCore.QSize(16777215, 45))

        self.new_register_label.setMinimumSize(QtCore.QSize(100, 45))
        self.new_register_label.setMaximumSize(QtCore.QSize(16777215, 45))

        self.old_register_type_label.setMinimumSize(QtCore.QSize(100, 35))
        self.old_register_type_label.setMaximumSize(QtCore.QSize(200, 55))
        self.old_register_type_value.setMinimumSize(QtCore.QSize(100, 35))
        self.old_register_type_value.setMaximumSize(QtCore.QSize(200, 55))
        self.old_register_type_value.setStyleSheet('color: rgb(80, 80, 80);background-color: rgb(190, 190, 190)')

        self.old_register_name_label.setMinimumSize(QtCore.QSize(100, 35))
        self.old_register_name_label.setMaximumSize(QtCore.QSize(200, 55))
        self.old_register_name_value.setMinimumSize(QtCore.QSize(100, 35))
        self.old_register_name_value.setMaximumSize(QtCore.QSize(200, 55))
        self.old_register_name_value.setStyleSheet('color: rgb(80, 80, 80);background-color: rgb(190, 190, 190)')

        self.old_register_value_label.setMinimumSize(QtCore.QSize(100, 35))
        self.old_register_value_label.setMaximumSize(QtCore.QSize(200, 55))
        self.old_register_value_value.setMinimumSize(QtCore.QSize(100, 35))
        self.old_register_value_value.setMaximumSize(QtCore.QSize(200, 55))
        self.old_register_value_value.setStyleSheet('color: rgb(80, 80, 80);background-color: rgb(190, 190, 190)')

        self.old_register_date_label.setMinimumSize(QtCore.QSize(100, 35))
        self.old_register_date_label.setMaximumSize(QtCore.QSize(200, 55))
        self.old_register_date_value.setMinimumSize(QtCore.QSize(100, 35))
        self.old_register_date_value.setMaximumSize(QtCore.QSize(200, 55))
        self.old_register_date_value.setStyleSheet('color: rgb(80, 80, 80);background-color: rgb(190, 190, 190)')

        self.new_register_type_label.setMinimumSize(QtCore.QSize(100, 35))
        self.new_register_type_label.setMaximumSize(QtCore.QSize(200, 45))
        self.new_register_type_value.setMinimumSize(QtCore.QSize(100, 35))
        self.new_register_type_value.setMaximumSize(QtCore.QSize(200, 45))
        self.new_register_type_value.setEnabled(False)
        self.new_register_type_value.setStyleSheet('color: rgb(80, 80, 80);background-color: rgb(190, 190, 190);border: 0;')

        self.new_register_name_label.setMinimumSize(QtCore.QSize(100, 35))
        self.new_register_name_label.setMaximumSize(QtCore.QSize(200, 45))

        self.new_register_value_label.setMinimumSize(QtCore.QSize(100, 35))
        self.new_register_value_label.setMaximumSize(QtCore.QSize(200, 55))

        self.new_register_date_label.setMinimumSize(QtCore.QSize(100, 35))
        self.new_register_date_label.setMaximumSize(QtCore.QSize(200, 55))

        # Buttons
        self.edit_button.setFont(font)
        self.edit_button.setMinimumSize(QtCore.QSize(160, 50))
        self.edit_button.setMaximumSize(QtCore.QSize(190, 80))
        self.edit_button.setStyleSheet('''QPushButton {
                                             background-color: white;
                                             color: black;
                                             border: 2px solid #E5C442;
                                         }

                                         QPushButton:hover:!pressed {
                                             background-color: #E5C442;
                                             color: white;
                                             font-weight: bold;
                                         }

                                         QPushButton:pressed {
                                             background-color: #E5C442;
                                             color: white;
                                             font-weight: bold;
                                         }''')

        self.cancel_button.setFont(font)
        self.cancel_button.setMinimumSize(QtCore.QSize(160, 50))
        self.cancel_button.setMaximumSize(QtCore.QSize(190, 80))
        self.cancel_button.setStyleSheet('''QPushButton {
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

        # Inputs
        self.new_register_name_input.setStyleSheet('background-color: white;')
        self.new_register_name_input.setMinimumSize(QtCore.QSize(100, 35))
        self.new_register_name_input.setMaximumSize(QtCore.QSize(200, 40))

        self.new_register_value_input.setStyleSheet('background-color: white;')
        self.new_register_value_input.setMinimumSize(QtCore.QSize(100, 35))
        self.new_register_value_input.setMaximumSize(QtCore.QSize(200, 40))

        self.new_register_date_input.setStyleSheet('background-color: white;')
        self.new_register_date_input.setMinimumSize(QtCore.QSize(150, 35))
        self.new_register_date_input.setMaximumSize(QtCore.QSize(200, 40))
        self.new_register_date_input.setAlignment(QtCore.Qt.AlignCenter)
        self.new_register_date_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.new_register_date_input.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.new_register_date_input.setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.new_register_date_input.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(3000, 12, 31), QtCore.QTime(23, 59, 59)))

    def translate_ui(self, transaction_type, old_name, old_value, old_date):
        self.transaction_type = transaction_type[0]
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Edição"))

        self.old_register_label.setText(_translate("MainWindow", "    Valores antigos da transação"))
        self.old_register_type_label.setText(_translate("MainWindow", "Tipo:"))
        self.old_register_type_value.setText(_translate("MainWindow", '  ' + str(transaction_type[1]).capitalize()))
        self.old_register_name_label.setText(_translate("MainWindow", "Nome antigo:"))
        self.old_register_name_value.setText(_translate("MainWindow", '  ' + str(old_name)))
        self.old_register_value_label.setText(_translate("MainWindow", "Valor antigo:"))
        self.old_register_value_value.setText(_translate("MainWindow", '  ' + str(old_value)))
        self.old_register_date_label.setText(_translate("MainWindow", "Data antiga:"))
        self.old_register_date_value.setText(_translate("MainWindow", '  ' + str(old_date)))

        self.new_register_label.setText(_translate("MainWindow", '   Valores novos da transação'))
        self.new_register_type_label.setText(_translate("MainWindow", 'Tipo:'))
        self.new_register_type_value.setText(_translate("MainWindow", '  ' + str(transaction_type[1]).capitalize()))
        self.new_register_name_label.setText(_translate("MainWindow", "Nome novo:"))
        self.new_register_name_input.clear()
        self.new_register_value_label.setText(_translate("MainWindow", "Valor novo:"))
        self.new_register_value_input.clear()
        self.new_register_date_label.setText(_translate("MainWindow", "Data nova:"))
        day, month, year = str(old_date).split('/')
        self.new_register_date_input.setDate(QtCore.QDate(int(year), int(month), int(day)))

        self.edit_button.setText(_translate("MainWindow", "Editar"))
        self.cancel_button.setText(_translate("MainWindow", "Cancelar"))

    def build_structure(self):
        self.old_register_type_layout.addWidget(self.old_register_type_label)
        self.old_register_type_layout.addWidget(self.old_register_type_value)
        self.old_register_name_layout.addWidget(self.old_register_name_label)
        self.old_register_name_layout.addWidget(self.old_register_name_value)
        self.old_register_value_layout.addWidget(self.old_register_value_label)
        self.old_register_value_layout.addWidget(self.old_register_value_value)
        self.old_register_date_layout.addWidget(self.old_register_date_label)
        self.old_register_date_layout.addWidget(self.old_register_date_value)

        self.old_register_layout.addWidget(self.old_register_type_horizontalWidget)
        self.old_register_layout.addItem(QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))
        self.old_register_layout.addWidget(self.old_register_name_horizontalWidget)
        self.old_register_layout.addItem(QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))
        self.old_register_layout.addWidget(self.old_register_value_horizontalWidget)
        self.old_register_layout.addItem(QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))
        self.old_register_layout.addWidget(self.old_register_date_horizontalWidget)
        self.old_register_layout.addItem(QtWidgets.QSpacerItem(40, 150, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))

        self.new_register_type_layout.addWidget(self.new_register_type_label)
        self.new_register_type_layout.addWidget(self.new_register_type_value)
        self.new_register_name_layout.addWidget(self.new_register_name_label)
        self.new_register_name_layout.addWidget(self.new_register_name_input)
        self.new_register_value_layout.addWidget(self.new_register_value_label)
        self.new_register_value_layout.addWidget(self.new_register_value_input)
        self.new_register_date_layout.addWidget(self.new_register_date_label)
        self.new_register_date_layout.addWidget(self.new_register_date_input, alignment=QtCore.Qt.AlignLeft)

        self.new_register_layout.addWidget(self.new_register_type_horizontalWidget)
        self.new_register_layout.addItem(QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))
        self.new_register_layout.addWidget(self.new_register_name_horizontalWidget)
        self.new_register_layout.addItem(QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))
        self.new_register_layout.addWidget(self.new_register_value_horizontalWidget)
        self.new_register_layout.addItem(QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))
        self.new_register_layout.addWidget(self.new_register_date_horizontalWidget)
        self.new_register_layout.addItem(QtWidgets.QSpacerItem(40, 150, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))

        self.bottom_buttons_layout.addWidget(self.edit_button)
        self.bottom_buttons_layout.addItem(QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))
        self.bottom_buttons_layout.addWidget(self.cancel_button)

        self.gridLayout.addWidget(self.old_register_label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.old_register_verticalWidget, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.new_register_label, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.new_register_verticalWidget, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.bottom_buttons_horizontalWidget, 2, 1, 1, 1)
        self.gridLayout.addItem(QtWidgets.QSpacerItem(15, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))

    def define_actions(self):
        self.edit_button.clicked.connect(self.edit)
        self.cancel_button.clicked.connect(self.go_back)
        self.new_register_value_input.keyPressEvent = self.handle_key_pressed

    def handle_key_pressed(self, event):
        text = self.new_register_value_input.text().replace(',', '.').replace('.', '')
        key = event.key()
        if 57 >= key >= 48:
            text = re.sub('\A0*', '', text)
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
        self.new_register_value_input.setText(a)

    def go_back(self):
        self.back_signal.emit(2)

    def edit(self):
        old_name = self.old_register_name_value.text()[2:]
        old_value = self.old_register_value_value.text()[2:]
        old_date = self.old_register_date_value.text()[2:]

        new_name = self.new_register_name_input.text() or old_name
        new_value = self.new_register_value_input.text() or old_value
        new_date = self.new_register_date_input.text()

        if new_name == old_name and new_value == old_value and new_date == old_date:
            self.show_message('Nenhuma alteração no registro foi realizada. Para voltar clique em cancelar.')
            return

        message = self.edition_controller.edit(self.transaction_type, old_name, old_value, old_date, new_name, new_value, new_date)
        self.show_message(message)
        self.back_signal.emit(2)

    def show_message(self, text):
        self.dialog.setText('\n' + text + '\t\t\n')
        self.dialog.exec()
