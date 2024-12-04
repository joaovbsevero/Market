from PyQt5 import QtCore, QtGui, QtWidgets


class QRangeSlider(QtWidgets.QWidget):

    def __init__(self, min, max, parent, *args):
        super(QRangeSlider, self).__init__(parent=parent, *args)

        self.sliders_box_layout = QtWidgets.QHBoxLayout(self)

        self.start_slider = QtWidgets.QSlider(self)
        self.end_slider = QtWidgets.QSlider(self)

        self.create_structure(max)

    def create_structure(self, max_value):
        self.setMinimumSize(QtCore.QSize(0, 45))
        self.setMaximumSize(QtCore.QSize(16777215, 55))

        self.start_slider.setOrientation(QtCore.Qt.Horizontal)
        self.end_slider.setOrientation(QtCore.Qt.Horizontal)

        self.start_slider.setMaximum(0)
        self.start_slider.setMinimum(-5)
        self.start_slider.setInvertedAppearance(True)
        self.start_slider.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
        self.start_slider.setStyleSheet('border: 0px')
        self.old_start_event = self.start_slider.mouseMoveEvent
        self.start_slider.mouseMoveEvent = self.show_start_current_value

        self.end_slider.setMaximum(10)
        self.end_slider.setMinimum(5)
        self.end_slider.setValue(max_value)
        self.end_slider.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
        self.end_slider.setStyleSheet('border: 0px;')
        self.old_end_event = self.end_slider.mouseMoveEvent
        self.end_slider.mouseMoveEvent = self.show_end_current_value

        self.sliders_box_layout.addWidget(self.start_slider, alignment=QtCore.Qt.AlignRight)
        self.sliders_box_layout.addWidget(self.end_slider, alignment=QtCore.Qt.AlignLeft)
        self.sliders_box_layout.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
        self.sliders_box_layout.setSpacing(0)
        self.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))

    def show_start_current_value(self, event):
        self.old_start_event(event)
        QtWidgets.QToolTip.showText(QtGui.QCursor.pos(), str(abs(self.start_slider.value())))

    def show_end_current_value(self, event):
        self.old_end_event(event)
        QtWidgets.QToolTip.showText(QtGui.QCursor.pos(), str(abs(self.end_slider.value())))

    def min(self):
        return self.start_slider.value()

    def max(self):
        return self.end_slider.value()

    def setMinMax(self, min_value, max_value):
        max_value += 1
        if min_value == max_value:
            min_value = max_value - 10
            while min_value < 0:
                min_value += 1

        self.end_slider.setMaximum(max_value)
        self.end_slider.setMinimum((max_value + min_value) // 2)
        self.end_slider.setValue(max_value)

        self.start_slider.setMinimum(-(max_value + min_value) // 2)
        self.start_slider.setMaximum(-min_value)
        self.start_slider.setValue(-min_value)
