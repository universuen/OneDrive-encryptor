from Mover import *
from UI.Main_window import *
from UI.Login_window import Login



if __name__ == '__main__':

    if is_admin():
        app = QApplication(sys.argv)

        if os.path.exists("config.pkl"):
            with open("config.pkl", "rb") as file:
                mover = pickle.load(file)
            window = Window()
            t1 = Thread(mover.update_online_files)
            t1.sig.connect(window.set_text)
            t2 = Thread(mover.update_local_files)
            t2.sig.connect(window.set_text)
            window.pushButton.clicked.connect(t1.start)
            window.pushButton_2.clicked.connect(t2.start)
            window.pushButton_3.clicked.connect(mover.open_folder)
            window.show()
        else:
            login = Login()
            mover = Mover()
            login.pushButton_2.clicked.connect(lambda: get_mover(login, mover))
            login.show()
        sys.exit(app.exec_())

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

