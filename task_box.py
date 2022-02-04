import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from tasks import messbox, get_picture, cheak

class MyWidget(QMainWindow, messbox.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        hight = self.lineEdit_3.text()
        wight = self.lineEdit_4.text()
        k1= cheak.cheak_num(hight, wight)
        k2, type= cheak.cheak_map(self.radioButton.isChecked(), self.radioButton_2.isChecked(), self.radioButton_3.isChecked())
        # print(k1, k2)

        if k1 == 1 and k2 == 1:
            self.close()
            get_picture.get_picture(float(hight), float(wight), 10, type)

        elif k1 == 0 and k2 == 1:
            self.label.setText("Ведите правельные координаты")

        elif k1 == 1 and k2 == 0:
            self.label_2.setText("Выбирите вид карты")

        else:
            self.label.setText("Ведите правельные координаты")
            self.label_2.setText("Выбирите вид карты")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
