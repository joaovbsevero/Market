import sys
from PyQt5 import QtWidgets

from .view.main_window import AppMainWindow


def main():
    APP = QtWidgets.QApplication(sys.argv)
    app = AppMainWindow()
    app.showMaximized()

    sys.exit(APP.exec())


if __name__ == '__main__':
    main()