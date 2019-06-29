from test import Ui_MainWindow
from login import Ui_MainWindow1
from register import Ui_MainWindow2
from record import Ui_MainWindow3
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sys
import pymysql
class Login(QtWidgets.QMainWindow,Ui_MainWindow1):
    def __init__(self):
        super(Login,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.loginBtn)
    def loginBtn(self):
        if self.lineEdit.text() == "" and self.lineEdit_2.text() == "":
            QtWidgets.QMessageBox.warning(self, "警告！", "用户名和密码不能为空！", QtWidgets.QMessageBox.Yes)
        elif self.lineEdit.text() == "" and self.lineEdit_2.text() != "":
            QtWidgets.QMessageBox.warning(self, "警告！", "用户名不能为空！", QtWidgets.QMessageBox.Yes)
        elif self.lineEdit.text() != "" and self.lineEdit_2.text() == "":
            QtWidgets.QMessageBox.warning(self, "警告！", "密码不能为空！", QtWidgets.QMessageBox.Yes)
        else:
            db=pymysql.connect("localhost","root","emosuyan9","CARC")
            cursor = db.cursor()
            try:
                username=self.lineEdit.text()
                password=self.lineEdit_2.text()
                sql = "SELECT COUNT(*) FROM UserInfo WHERE UserName ='%s' AND UserPwd ='%s'"%(username,password)
                cursor.execute(sql)
                result = cursor.fetchone()
                if result[0] == 0:
                    QtWidgets.QMessageBox.warning(self, 'Fail', '用户名或密码错误', QtWidgets.QMessageBox.Yes)
                else:
                    self.close()
                    test.show()
            except:
                QtWidgets.QMessageBox.warning(self, 'Error', '获取数据失败', QtWidgets.QMessageBox.Yes)
            db.close()
class Test(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Test, self).__init__()
        self.setupUi(self)
        self.xianshi()
        self.slot()
    def open(self):
        self.show()
class Record(QtWidgets.QMainWindow,Ui_MainWindow3):
    def __init__(self):
        super(Record,self).__init__()
        self.setupUi(self)
    def open(self):
        self.show()
class Register(QtWidgets.QMainWindow,Ui_MainWindow2):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.recordInfo)
    def zhuce(self):
        self.show()
    def recordInfo(self):
        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "" or self.lineEdit_3.text() == "":
            QtWidgets.QMessageBox.warning(self, "警告！", "用户名/密码/电话均不能为空！", QtWidgets.QMessageBox.Yes)
        else:
            db=pymysql.connect("localhost","root","emosuyan9","CARC")
            cursor=db.cursor()
            username=self.lineEdit.text()
            userpwd=self.lineEdit_2.text()
            userphone=self.lineEdit_3.text()
            sql1 = "SELECT COUNT(*) FROM UserInfo WHERE UserName ='%s' OR UserPhone ='%s'" % (username, userphone)
            sql2="SELECT COUNT(*) FROM UserInfo"
            try:
                cursor.execute(sql1)
                result=cursor.fetchone()
                cursor.execute(sql2)
                result1=cursor.fetchone()
                if result[0]==0:
                    insertsql = "INSERT INTO UserInfo(UserID,UserName,UserPwd,UserPhone) VALUES(%d,'%s','%s','%s')" % (result1[0]+1,username,userpwd,userphone)
                    cursor.execute(insertsql)
                    db.commit()
                    QtWidgets.QMessageBox.warning(self,'Success','注册成功',QtWidgets.QMessageBox.Yes)
                    self.close()
                else:
                    QtWidgets.QMessageBox.warning(self, 'Fail', '用户名或电话重复', QtWidgets.QMessageBox.Yes)
            except:
                QtWidgets.QMessageBox.warning(self, 'Error', '获取数据失败', QtWidgets.QMessageBox.Yes)
        db.close()
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    login=Login()
    register=Register()
    record=Record()
    test=Test()
    login.show()
    login.pushButton_2.clicked.connect(register.zhuce)
    test.pushButton_6.clicked.connect(record.open)
    sys.exit(app.exec_())