import sys
import os
import pygame
import requests
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 362)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 270, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(10, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(350, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 50, 191, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 100, 191, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
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
        self.label_2.setText(_translate("MainWindow", "Введите вид карты:"))
        self.radioButton.setText(_translate("MainWindow", "Maps"))
        self.radioButton_2.setText(_translate("MainWindow", "SATELLITE "))
        self.radioButton_3.setText(_translate("MainWindow", "HYBRID "))
        self.label_3.setText(_translate("MainWindow", "x ="))
        self.label_4.setText(_translate("MainWindow", "y = "))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.k1 = 0
        self.k2 = 0
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        hight = self.lineEdit_3.text()
        wight = self.lineEdit_4.text()
        # print(type(hight), type(wight))
        if len(hight) == 0 or len(wight) == 0:
            self.label.setText("Ведите правельные координаты")
        else:
            if hight.isdigit() == True and wight.isdigit() == True or "-" == hight[0] or "-" == wight[
                0] or "." in wight or "." in hight:
                if -180 <= float(hight) <= 180 and -85 <= float(wight) <= 85:
                    x, y = hight, wight
                    self.k1 = 1
                else:
                    self.label.setText("Ведите правельные координаты")
            else:
                self.label.setText("Ведите правельные координаты")

        if self.radioButton.isChecked() == False and self.radioButton_2.isChecked() == False and self.radioButton_3.isChecked() == False:
            self.label_2.setText("Выбирите вид карты")
        else:
            if self.radioButton_3.isChecked():
                type = "sat,skl"
            elif self.radioButton_2.isChecked():
                type = 'sat'
            else:
                type = "map"
            self.k2 = 1

        if self.k1 == 1 and self.k2 == 1:
            self.close()
            self.get_picture(x, y, 10, type)

    def get_picture(self, x, y, z=10, type="map"):
        if z > 18:
            z = 18
        if z < 1:
            z = 1
        up = z
        FPS = 60
        map_request = f'https://static-maps.yandex.ru/1.x/?ll={x}%2C{y}&size=450,450&z={z}&l={type}'
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
        pygame.display.set_caption('Задача 4')
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
                    self.get_picture(x, y, up, type)
                if keys[pygame.K_PAGEDOWN]:
                    up += 1
                    self.get_picture(x, y, up, type)
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
