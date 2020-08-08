import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from ODE import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    my_signal = pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.my_signal.connect(self.set_text)

    def set_text(self, text):
        self.textBrowser.setText(text)
