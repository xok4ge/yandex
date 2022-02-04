import pygame
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import requests

#---------------------------------
pygame.init()
FPS = 60
FULLSCREEN = False
WIDTH = 600
HEIGHT = 400
polz = []
start, always, Z = [30, 50], [], 2  # max y = 80, min y = -81     max x = 180, min x = -180
#----------------------------------


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(232, 134)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
            self.gridLayout.setObjectName("gridLayout")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setObjectName("label")
            self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
            self.x_cord = QtWidgets.QLineEdit(self.centralwidget)
            self.x_cord.setObjectName("x_cord")
            self.gridLayout.addWidget(self.x_cord, 0, 1, 1, 1)
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setObjectName("label_2")
            self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
            self.y_cord = QtWidgets.QLineEdit(self.centralwidget)
            self.y_cord.setObjectName("y_cord")
            self.gridLayout.addWidget(self.y_cord, 1, 1, 1, 1)
            self.end = QtWidgets.QPushButton(self.centralwidget)
            self.end.setObjectName("end")
            self.gridLayout.addWidget(self.end, 2, 1, 1, 1)
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 232, 21))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.label.setText(_translate("MainWindow", "x coord:"))
            self.label_2.setText(_translate("MainWindow", "y coord:"))
            self.end.setText(_translate("MainWindow", "Применить"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.end.clicked.connect(self.cl)

    def cl(self):
        global polz
        cor = [self.x_cord.text(), self.y_cord.text()]
        polz = [int(i) if i else '' for i in cor]
        self.close()


def render(api):
    response = requests.get(api)
    with open('l.png', 'wb') as f:
        f.write(response.content)
    img = pygame.image.load('l.png')
    return img


def get_picture(x, y, z=2):
    if -180 < x <= 180 and -81 < y <= 80:
        return f'?ll={x}%2C{y}&z={z}&l=map'


def zoom(z, *args):
    global Z
    Z += z
    if Z > 20:
        Z = 20
    elif Z < 2:
        Z = 2
    cords = f'?ll={args[0][0]}%2C{args[0][1]}&z={Z}&l=map'
    geocoder_api_serv = "https://static-maps.yandex.ru/1.x/" + cords
    img = render(geocoder_api_serv)
    return img


def main(fps, width, height, fullscreen=False):
    global always
    if not fullscreen:
        screen = pygame.display.set_mode((width, height))
    else:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((width, height))
    screen.fill((0,0,0))
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    app.exec_()

    try:
        coords = get_picture(*polz)
        if coords is None:
            raise ValueError
        always = polz
    except ValueError:
        coords = get_picture(*start)
        always = start
    geocoder_api_serve = "https://static-maps.yandex.ru/1.x/" + coords
    img = render(geocoder_api_serve)
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if keys[pygame.K_PAGEUP]:
                img = zoom(1, always)
            if keys[pygame.K_PAGEDOWN]:
                img = zoom(-1, always)
        screen.blit(img, (0, 0))
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main(FPS, WIDTH, HEIGHT, FULLSCREEN)