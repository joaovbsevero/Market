import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets

from ..controller.browser_controller import BrowserController


class InitialPage(QtWidgets.QWidget):
    def __init__(self, navigation, *args):
        super(InitialPage, self).__init__(*args)

        self.navigation = navigation
        self.browser_controller = BrowserController()

        # Declaring main objects
        self.grid_layout = QtWidgets.QGridLayout(self)

        self.operations_verticalWidget = QtWidgets.QWidget(self, *args)
        self.operations_button_layout = QtWidgets.QVBoxLayout(self.operations_verticalWidget)

        self.visualizations_verticalWidget = QtWidgets.QWidget(self, *args)
        self.visualizations_button_layout = QtWidgets.QVBoxLayout(self.visualizations_verticalWidget)

        self.others_verticalWidget = QtWidgets.QWidget(self, *args)
        self.others_button_layout = QtWidgets.QVBoxLayout(self.others_verticalWidget)

        self.bottom_buttons_horizontalWidget = QtWidgets.QWidget(self, *args)
        self.bottom_buttons_layout = QtWidgets.QHBoxLayout(self.bottom_buttons_horizontalWidget)

        # Declaring labels
        self.operations_label = QtWidgets.QLabel(self)
        self.visualizations_label = QtWidgets.QLabel(self)
        self.others_label = QtWidgets.QLabel(self)

        # Declaring buttons
        self.register_button = QtWidgets.QPushButton(self.operations_verticalWidget)
        self.edit_button = QtWidgets.QPushButton(self.operations_verticalWidget)
        self.delete_button = QtWidgets.QPushButton(self.operations_verticalWidget)

        self.list_purchases_button = QtWidgets.QPushButton(self.visualizations_verticalWidget)
        self.sales_list_button = QtWidgets.QPushButton(self.visualizations_verticalWidget)
        self.purchases_list_button = QtWidgets.QPushButton(self.visualizations_verticalWidget)

        self.enter_gmail_button = QtWidgets.QPushButton(self.others_verticalWidget)
        self.enter_facebook_button = QtWidgets.QPushButton(self.others_verticalWidget)
        self.enter_google_button = QtWidgets.QPushButton(self.others_verticalWidget)

        self.quit_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)
        self.turn_off_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)

        # Declaring spacers
        self.operations_spacer = QtWidgets.QLabel(self.operations_verticalWidget)
        self.visualizations_spacer = QtWidgets.QLabel(self.visualizations_verticalWidget)
        self.others_spacer = QtWidgets.QLabel(self.others_verticalWidget)

        # Building UI
        self.setup_ui()
        self.translate_ui()
        self.create_structure()
        self.define_actions()

    def setup_ui(self):
        self.setup_main_objects()
        self.setup_buttons()
        self.setup_labels()
        self.setup_spacers()

    def setup_main_objects(self):
        font = QtGui.QFont()
        font.setFamily('Helvetica')
        font.setPointSize(14)

        self.operations_verticalWidget.setMinimumSize(QtCore.QSize(200, 270))
        self.operations_verticalWidget.setStyleSheet('background-color: rgb(243, 243, 243);')

        self.visualizations_verticalWidget.setMinimumSize(QtCore.QSize(200, 270))
        self.visualizations_verticalWidget.setStyleSheet('background-color: rgb(243, 243, 243);')

        self.others_verticalWidget.setMinimumSize(QtCore.QSize(200, 270))
        self.others_verticalWidget.setStyleSheet('background-color: rgb(243, 243, 243);')

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.bottom_buttons_horizontalWidget.sizePolicy().hasHeightForWidth())
        self.bottom_buttons_horizontalWidget.setSizePolicy(size_policy)
        self.bottom_buttons_horizontalWidget.setMinimumSize(QtCore.QSize(210, 0))

    def setup_labels(self):
        self.operations_label.setMaximumSize(QtCore.QSize(300, 70))
        self.visualizations_label.setMaximumSize(QtCore.QSize(300, 70))
        self.others_label.setMaximumSize(QtCore.QSize(300, 70))

    def setup_buttons(self):
        font = QtGui.QFont()
        font.setFamily('Helvetica')
        font.setPointSize(12)

        self.register_button.setFont(font)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHeightForWidth(self.register_button.sizePolicy().hasHeightForWidth())
        self.register_button.setSizePolicy(size_policy)
        self.register_button.setMinimumSize(QtCore.QSize(260, 60))
        self.register_button.setMaximumSize(QtCore.QSize(260, 80))
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

        self.edit_button.setFont(font)
        size_policy.setHeightForWidth(self.edit_button.sizePolicy().hasHeightForWidth())
        self.edit_button.setSizePolicy(size_policy)
        self.edit_button.setMinimumSize(QtCore.QSize(260, 60))
        self.edit_button.setMaximumSize(QtCore.QSize(260, 80))
        self.edit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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

        self.delete_button.setFont(font)
        size_policy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(size_policy)
        self.delete_button.setMinimumSize(QtCore.QSize(260, 60))
        self.delete_button.setMaximumSize(QtCore.QSize(260, 80))
        self.delete_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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

        self.list_purchases_button.setFont(font)
        size_policy.setHeightForWidth(self.list_purchases_button.sizePolicy().hasHeightForWidth())
        self.list_purchases_button.setSizePolicy(size_policy)
        self.list_purchases_button.setMinimumSize(QtCore.QSize(260, 60))
        self.list_purchases_button.setMaximumSize(QtCore.QSize(260, 80))
        self.list_purchases_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.list_purchases_button.setStyleSheet('''QPushButton {
                                                   background-color: white;
                                                   color: black;
                                                   border: 2px solid #7932A2;
                                                 }
                                                 
                                                 QPushButton:hover:!pressed {
                                                   background-color: #7932A2;
                                                   color: white;
                                                   font-weight: bold;
                                                 }
                                                 
                                                 QPushButton:pressed {
                                                   background-color: #7932A2;
                                                   color: white;
                                                   font-weight: bold;
                                                 }''')

        self.sales_list_button.setFont(font)
        size_policy.setHeightForWidth(self.sales_list_button.sizePolicy().hasHeightForWidth())
        self.sales_list_button.setSizePolicy(size_policy)
        self.sales_list_button.setMinimumSize(QtCore.QSize(260, 60))
        self.sales_list_button.setMaximumSize(QtCore.QSize(260, 80))
        self.sales_list_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sales_list_button.setStyleSheet('''QPushButton {
                                                   background-color: white;
                                                   color: black;
                                                   border: 2px solid #54A4FF;
                                                 }
                                                 
                                                 QPushButton:hover:!pressed {
                                                   background-color: #54A4FF;
                                                   color: white;
                                                   font-weight: bold;
                                                 }
                                                 
                                                 QPushButton:pressed {
                                                   background-color: #54A4FF;
                                                   color: white;
                                                   font-weight: bold;
                                                 }''')

        self.purchases_list_button.setFont(font)
        size_policy.setHeightForWidth(self.purchases_list_button.sizePolicy().hasHeightForWidth())
        self.purchases_list_button.setSizePolicy(size_policy)
        self.purchases_list_button.setMinimumSize(QtCore.QSize(260, 60))
        self.purchases_list_button.setMaximumSize(QtCore.QSize(260, 80))
        self.purchases_list_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.purchases_list_button.setStyleSheet('''QPushButton {
                                                        background-color: white;
                                                        color: black;
                                                        border: 2px solid #3E74B2;
                                                    }
                                                    
                                                    QPushButton:hover:!pressed {
                                                        background-color: #3E74B2;
                                                        color: white;
                                                        font-weight: bold;
                                                    }
                                                    
                                                    QPushButton:pressed {
                                                        background-color: #3E74B2;
                                                        color: white;
                                                        font-weight: bold;
                                                    }''')

        self.enter_gmail_button.setFont(font)
        size_policy.setHeightForWidth(self.enter_gmail_button.sizePolicy().hasHeightForWidth())
        self.enter_gmail_button.setSizePolicy(size_policy)
        self.enter_gmail_button.setMinimumSize(QtCore.QSize(260, 60))
        self.enter_gmail_button.setMaximumSize(QtCore.QSize(260, 80))
        self.enter_gmail_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enter_gmail_button.setStyleSheet('''QPushButton {
                                                  background-color: white;
                                                  color: black;
                                                  border: 2px solid #B04949;
                                              }
                                              
                                              QPushButton:hover:!pressed {
                                                  background-color: #B04949;
                                                  color: white;
                                                  font-weight: bold;
                                              }
                                              
                                              QPushButton:pressed {
                                                  background-color: #B04949;
                                                  color: white;
                                                  font-weight: bold;
                                              }''')

        self.enter_facebook_button.setFont(font)
        size_policy.setHeightForWidth(self.enter_facebook_button.sizePolicy().hasHeightForWidth())
        self.enter_facebook_button.setSizePolicy(size_policy)
        self.enter_facebook_button.setMinimumSize(QtCore.QSize(260, 60))
        self.enter_facebook_button.setMaximumSize(QtCore.QSize(260, 80))
        self.enter_facebook_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enter_facebook_button.setStyleSheet('''QPushButton {
                                                     background-color: white;
                                                     color: black;
                                                     border: 2px solid #2C7AFF;
                                                 }
                                                 
                                                 QPushButton:hover:!pressed {
                                                     background-color: #2C7AFF;
                                                     color: white;
                                                     font-weight: bold;
                                                 }
                                                 
                                                 QPushButton:pressed {
                                                     background-color: #2C7AFF;
                                                     color: white;
                                                     font-weight: bold;
                                                 }''')

        self.enter_google_button.setFont(font)
        size_policy.setHeightForWidth(self.enter_google_button.sizePolicy().hasHeightForWidth())
        self.enter_google_button.setSizePolicy(size_policy)
        self.enter_google_button.setMinimumSize(QtCore.QSize(260, 60))
        self.enter_google_button.setMaximumSize(QtCore.QSize(260, 80))
        self.enter_google_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enter_google_button.setStyleSheet('''QPushButton {
                                                   background-color: white;
                                                   color: black;
                                                   border: 2px solid black;
                                               }
                                               
                                                QPushButton:hover:!pressed {
                                                   background-color: black;
                                                   color: white;
                                                   font-weight: bold;
                                               }
                                               
                                                QPushButton:pressed {
                                                   background-color: black;
                                                   color: white;
                                                   font-weight: bold;
                                               }''')

        self.quit_button.setFont(font)
        size_policy.setHeightForWidth(self.quit_button.sizePolicy().hasHeightForWidth())
        self.quit_button.setSizePolicy(size_policy)
        self.quit_button.setMinimumSize(QtCore.QSize(120, 60))
        self.quit_button.setMaximumSize(QtCore.QSize(190, 80))
        self.quit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quit_button.setStyleSheet('''QPushButton {
                                           background-color: white;
                                           color: black;
                                           border: 2px solid #A63030;
                                       }
                                       
                                       QPushButton:hover:!pressed {
                                           background-color: #A63030;
                                           color: white;
                                           font-weight: bold;
                                       }
                                       
                                       QPushButton:pressed {
                                           background-color: #A63030;
                                           color: white;
                                           font-weight: bold;
                                       }''')

        self.turn_off_button.setFont(font)
        size_policy.setHeightForWidth(self.turn_off_button.sizePolicy().hasHeightForWidth())
        self.turn_off_button.setSizePolicy(size_policy)
        self.turn_off_button.setMinimumSize(QtCore.QSize(100, 60))
        self.turn_off_button.setMaximumSize(QtCore.QSize(180, 70))
        self.turn_off_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.turn_off_button.setStyleSheet('''QPushButton {
                                               background-color: white;
                                               color: black;
                                               border: 2px solid black;
                                           }
                                           
                                           QPushButton:hover:!pressed {
                                               background-color: black;
                                               color: white;
                                               font-weight: bold;
                                           }
                                           
                                           QPushButton:pressed {
                                               background-color: black;
                                               color: white;
                                               font-weight: bold;
                                           }''')

    def setup_spacers(self):
        self.operations_spacer.setMinimumSize(QtCore.QSize(0, 60))
        self.operations_spacer.setMaximumSize(QtCore.QSize(0, 70))
        self.operations_spacer.setText('')

        self.visualizations_spacer.setMinimumSize(QtCore.QSize(0, 60))
        self.visualizations_spacer.setMaximumSize(QtCore.QSize(0, 70))
        self.visualizations_spacer.setText('')

        self.others_spacer.setMinimumSize(QtCore.QSize(0, 60))
        self.others_spacer.setMaximumSize(QtCore.QSize(0, 70))
        self.others_spacer.setText('')

    def create_structure(self):
        self.operations_button_layout.addWidget(self.register_button, 0, QtCore.Qt.AlignHCenter)
        self.operations_button_layout.addWidget(self.edit_button, 0, QtCore.Qt.AlignHCenter)
        self.operations_button_layout.addWidget(self.delete_button, 0, QtCore.Qt.AlignHCenter)
        self.operations_button_layout.addWidget(self.operations_spacer, 0, QtCore.Qt.AlignHCenter)

        self.grid_layout.addWidget(self.operations_label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.grid_layout.addWidget(self.operations_verticalWidget, 1, 0, 1, 1)

        self.visualizations_button_layout.addWidget(self.list_purchases_button, 0, QtCore.Qt.AlignHCenter)
        self.visualizations_button_layout.addWidget(self.sales_list_button, 0, QtCore.Qt.AlignHCenter)
        self.visualizations_button_layout.addWidget(self.purchases_list_button, 0, QtCore.Qt.AlignHCenter)
        self.visualizations_button_layout.addWidget(self.visualizations_spacer, 0, QtCore.Qt.AlignHCenter)

        self.grid_layout.addWidget(self.visualizations_label, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.grid_layout.addWidget(self.visualizations_verticalWidget, 1, 2, 1, 1)

        self.others_button_layout.addWidget(self.enter_gmail_button, 0, QtCore.Qt.AlignHCenter)
        self.others_button_layout.addWidget(self.enter_facebook_button, 0, QtCore.Qt.AlignHCenter)
        self.others_button_layout.addWidget(self.enter_google_button, 0, QtCore.Qt.AlignHCenter)
        self.others_button_layout.addWidget(self.others_spacer, 0, QtCore.Qt.AlignHCenter)

        self.grid_layout.addWidget(self.others_label, 0, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.grid_layout.addWidget(self.others_verticalWidget, 1, 4, 1, 1)

        self.bottom_buttons_layout.addWidget(self.quit_button, 0, QtCore.Qt.AlignVCenter)
        self.bottom_buttons_layout.addWidget(self.turn_off_button)

        self.grid_layout.addWidget(self.bottom_buttons_horizontalWidget, 2, 4, 1, 1)

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.operations_label.setText(_translate('MainWindow', 'Operações'))

        self.visualizations_label.setText(_translate('MainWindow', 'Visualizações'))

        self.register_button.setToolTip(_translate('MainWindow', 'Área para cadastrar vendas e compras'))
        self.register_button.setText(_translate('MainWindow', 'Cadastrar'))

        self.edit_button.setToolTip(_translate('MainWindow', 'Área para editar vendas e compras cadastradas'))
        self.edit_button.setText(_translate('MainWindow', 'Editar'))

        self.delete_button.setToolTip(_translate('MainWindow', 'Área para excluir vendas e compras cadastradas'))
        self.delete_button.setText(_translate('MainWindow', 'Excluir'))

        self.quit_button.setToolTip(_translate('MainWindow', 'Sai do programa'))
        self.quit_button.setText(_translate('MainWindow', 'Sair'))

        self.turn_off_button.setToolTip(_translate('MainWindow', 'Desliga o computador'))
        self.turn_off_button.setText(_translate('MainWindow', 'Desligar'))

        self.others_label.setText(_translate('MainWindow', 'Outros'))

        self.list_purchases_button.setToolTip(
            _translate('MainWindow', 'Exibe lista de todas vendas e compras cadastradas'))
        self.list_purchases_button.setText(_translate('MainWindow', ' Lista de Compras e Vendas '))

        self.sales_list_button.setToolTip(_translate('MainWindow', 'Exibe uma lista de todas as vendas'))
        self.sales_list_button.setText(_translate('MainWindow', 'Lista de Vendas'))

        self.purchases_list_button.setToolTip(_translate('MainWindow', 'Exibe uma lista de todas as compras'))
        self.purchases_list_button.setText(_translate('MainWindow', 'Lista de Compras'))

        self.enter_gmail_button.setToolTip(_translate('MainWindow', 'Entra no Gmail'))
        self.enter_gmail_button.setText(_translate('MainWindow', 'Acessar Gmail'))

        self.enter_facebook_button.setToolTip(_translate('MainWindow', 'Entra no Facebook'))
        self.enter_facebook_button.setText(_translate('MainWindow', 'Acessar Facebook'))

        self.enter_google_button.setToolTip(_translate('MainWindow', 'Entra no google'))
        self.enter_google_button.setText(_translate('MainWindow', 'Acessar Google'))

    def define_actions(self):
        self.register_button.clicked.connect((lambda: self.navigation.emit(1)))
        self.edit_button.clicked.connect((lambda: self.navigation.emit(2)))
        self.delete_button.clicked.connect((lambda: self.navigation.emit(3)))

        self.list_purchases_button.clicked.connect((lambda: self.navigation.emit(4)))
        self.sales_list_button.clicked.connect((lambda: self.navigation.emit(5)))
        self.purchases_list_button.clicked.connect((lambda: self.navigation.emit(6)))

        self.enter_gmail_button.clicked.connect(self.browser_controller.open_gmail)
        self.enter_facebook_button.clicked.connect(self.browser_controller.open_facebook)
        self.enter_google_button.clicked.connect(self.browser_controller.open_google)

        self.quit_button.clicked.connect((lambda: sys.exit(0)))
        self.turn_off_button.clicked.connect(self.turn_off_function)

    def turn_off_function(self):
        self.parent().close()

        if sys.platform == 'win32':
            subprocess.call(["shutdown", "/s", "/t", "0"])
        else:
            subprocess.call(["shutdown", "-h", "now"])

        sys.exit()

