import sys
import os
import pygame
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 163)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 531, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 90, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 21))
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
        self.label.setText(_translate("MainWindow", "Введите координаты:"))
        self.pushButton.setText(_translate("MainWindow", "Продолжить"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        cord = (self.lineEdit.text()).lower()
        x, y = cord.split(" ")
        print(x, y)
        self.close()
        self.get_picture(x, y)

    def get_picture(self, x, y, z=10):
        if z > 18:
            z = 18
        if z < 1:
            z = 1
        up = z
        FPS = 60
        map_request = s = f'https://static-maps.yandex.ru/1.x/?ll={x}%2C{y}&size=450,450&z={z}&l=map'
        response = requests.get(map_request)
        fullscreen = False
        width = 450
        height = 350
        pygame.init()

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.set_caption('Австралия')
        pygame.display.flip()

        running = True
        while running:
            screen.fill((255, 255, 255))
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    running = False
                if keys[pygame.K_PAGEUP]:
                    up -= 1
                    self.get_picture(x, y, up)
                if keys[pygame.K_PAGEDOWN]:
                    up += 1
                    self.get_picture(x, y, up)
            img = pygame.image.load('Map.png')
            screen.blit(img, (0, 0))
            pygame.display.flip()
        pygame.quit()
        os.remove(map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
