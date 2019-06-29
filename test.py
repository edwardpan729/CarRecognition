# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from aip import AipImageClassify
import os
from aip import AipOcr
APP_ID='16630610'
API_KEY='cvLklIe7UhuQU7Uzl2eXKosx'
SECRET_KEY='Ix53uAnzQ2HAUbLKevMc689QedVG7gMl'

class Ui_MainWindow(object):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__()
        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 561)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 30, 741, 479))
        self.widget.setObjectName("widget")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(380, 30, 101, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(380, 60, 311, 361))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 50, 72, 15))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 290, 72, 15))
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(110, 30, 191, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 70, 191, 81))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_3.setGeometry(QtCore.QRect(110, 160, 191, 91))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_4.setGeometry(QtCore.QRect(110, 260, 191, 91))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 440, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(602, 440, 101, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 351, 361))
        self.label_6.setObjectName("label_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(110, 430, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox.raise_()
        self.label_5.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.label_6.raise_()
        self.pushButton_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "检测界面"))
        self.label_5.setText(_translate("MainWindow", "车辆检测结果"))
        self.label.setText(_translate("MainWindow", "车牌号"))
        self.label_2.setText(_translate("MainWindow", "车型"))
        self.label_3.setText(_translate("MainWindow", "车辆分类统计"))
        self.label_4.setText(_translate("MainWindow", "车辆属性"))
        self.pushButton_5.setText(_translate("MainWindow", "保存记录"))
        self.pushButton_6.setText(_translate("MainWindow", "查看识别记录"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_7.setText(_translate("MainWindow", "拍照检测"))

    def xianshi(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == True:
                self.timer_camera.start(10)
        else:
            self.timer_camera.stop()
            self.cap.release()

    def paizhao(self):
        imgpath = os.path.join("1.png")
        cv2.imwrite(imgpath, self.image)
        self.indentityxing()
        self.indentitypai()

    def indentityxing(self):
        imageClassify = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
        filepath = "1.png"

        def get_file_content(filepath):
            with open(filepath, 'rb')as fp:
                return fp.read()

        options = {
            'baike_num': '0',
        }
        result = imageClassify.carDetect(get_file_content(filepath), options)
        self.textBrowser_2.setText(
            result['result'][0]['name'] + "    " + '%.2f' % (result['result'][0]['score'] * 100) + "%\n"
            + result['result'][1]['name'] + "    " + '%.2f' % (result['result'][1]['score'] * 100) + "%\n"
            + result['result'][2]['name'] + "    " + '%.2f' % (result['result'][2]['score'] * 100) + "%\n")

    def indentitypai(self):
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        filepath = "1.png"

        def get_file_content(filepath):
            with open(filepath, 'rb')as fp:
                return fp.read()

        result1 = client.licensePlate(get_file_content(filepath))
        self.textBrowser.setText(result1['words_result']['number'])

    def show_camera(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_6.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def slot(self):
        self.timer_camera.timeout.connect(self.show_camera)
        self.pushButton_7.clicked.connect(self.paizhao)