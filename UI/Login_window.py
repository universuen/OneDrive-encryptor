import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import *
from .login import Ui_MainWindow
from utilities import *

class Login(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_ODname)
        self.name = None

    def get_ODname(self):
        username = getpass.getuser()
        root_path = "C:\\Users\\" + username + "\\"
        directory = QFileDialog.getExistingDirectory(self,
                                                      "Select OneDrive folder",
                                                      root_path)
        self.textBrowser.setText(directory)
        self.name = directory.split("/")[-1]