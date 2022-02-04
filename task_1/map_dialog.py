from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QApplication, QMainWindow
import main
import sys


class MapMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task_1/map_data.ui', self)
        self.setWindowTitle('Map data')
        self.pushButton.clicked.connect(self.esc)
        self.setWindowFlags(
            self.windowFlags() and QtCore.Qt.CustomizeWindowHint)
        

    def esc(self):
        cor = [self.x_cord.text(), self.y_cord.text()]
        main.scale = self.spn.text()
        main.polz = [int(i) if i else '' for i in cor]
        self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def open_dialog():
    # Fix HiDPI
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    ex = MapMenu()
    ex.show()
    sys.excepthook = except_hook
    app.exec_()
    del app
    del ex


# if __name__ == '__main__':
#     open_dialog()
