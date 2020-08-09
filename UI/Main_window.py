import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from .ODE import Ui_MainWindow
from utilities import *



class Thread(QThread):
    sig = pyqtSignal(str)

    def __init__(self, func = None, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        if self.func:
            self.func(*self.args, **self.kwargs)
        else:
            message = Message()
            while True:
                self.sig.emit(message.get())
                time.sleep(0.5)



class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.message = Thread()
        self.message.sig.connect(self.set_text)
        self.message.start()
    def set_text(self, text):
        self.textBrowser.setText(text)
