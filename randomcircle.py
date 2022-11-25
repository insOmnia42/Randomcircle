import random
import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen
from PyQt5.QtCore import Qt
from random import randint
from math import factorial, sqrt


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(1000, 1000, 1000, 1000))
        self.btn.setMinimumSize(QtCore.QSize(1000, 1000))
        self.btn.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 591, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Окружность"))
        self.btn.setText(_translate("MainWindow", "Создать окружность"))
        self.pushButton.setText(_translate("MainWindow", "Нарисовать окружность"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.circle)
        canvas = QPixmap(589, 520)
        self.label.setPixmap(canvas)

    def circle(self):
        x = random.randint(10, 480)
        y = random.randint(10, 420)
        d = random.randint(10, 80)
        # создаем экземпляр QPainter, передавая холст (self.label.pixmap())
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pen.setColor(QColor(r, g, b))
        painter.setPen(pen)
        painter.drawEllipse(x, y, d, d)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())