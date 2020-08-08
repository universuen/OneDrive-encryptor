from Mover import *
from UI import *

if __name__ == '__main__':
    if is_admin():
        if os.path.exists("mover.pkl"):
            with open("mover.pkl", "rb") as file:
                mover = pickle.load(file)
        else:
            mover = Mover("OneDrive - whu.edu.cn", input("Set the password:"))

        app = QApplication(sys.argv)
        window = Window()
        window.pushButton.clicked.connect(lambda: mover.update_online_files())
        window.pushButton_2.clicked.connect(lambda: mover.update_local_files())
        window.pushButton_3.clicked.connect(lambda: mover.open_folder())
        window.textBrowser.setText("Ready")
        window.show()

        with open("mover.pkl", "wb") as file:
            pickle.dump(mover, file)

        sys.exit(app.exec_())
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

