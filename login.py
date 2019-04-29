# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anmol.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_Window1(object):
    def logincheck(self):
        username=self.uname_text.text()
        password=self.password_text.text()
        connection=sqlite3.connect("login1.db")
        result = connection.execute("SELECT * FROM USERS1 WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        if (len(result.fetchall()))>0:  #Means result is found here
            print("user Found")
        else:
            print("NOT FOUND")
    def setupUi(self, Window1):
        Window1.setObjectName("Window1")
        Window1.resize(759, 544)
        self.centralwidget = QtWidgets.QWidget(Window1)
        self.centralwidget.setObjectName("centralwidget")
        
        self.uname_text = QtWidgets.QLineEdit(self.centralwidget)
        self.uname_text.setGeometry(QtCore.QRect(290, 230, 271, 31))
        self.uname_text.setObjectName("uname_text")
        
        self.password_text = QtWidgets.QLineEdit(self.centralwidget)
        self.password_text.setGeometry(QtCore.QRect(290, 280, 271, 31))
        self.password_text.setObjectName("password_text")
        
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(210, 240, 60, 16))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(210, 290, 60, 16))
        self.password.setObjectName("password")
        self.pushsignin = QtWidgets.QPushButton(self.centralwidget)
        self.pushsignin.setGeometry(QtCore.QRect(340, 330, 113, 32))
        self.pushsignin.setObjectName("pushsignin")
        
        ## THIS IS SIGNIN EVENT FOR BUTTON ##
        self.pushsignin.clicked.connect(self.logincheck)
        ## DONE##
        
        self.Header = QtWidgets.QLabel(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(310, 70, 181, 41))
        self.Header.setObjectName("Header")
        Window1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Window1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window1)
        self.statusbar.setObjectName("statusbar")
        Window1.setStatusBar(self.statusbar)
        self.actionrun = QtWidgets.QAction(Window1)
        self.actionrun.setObjectName("actionrun")
        self.actionExit = QtWidgets.QAction(Window1)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionrun)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Window1)
        QtCore.QMetaObject.connectSlotsByName(Window1)

    def retranslateUi(self, Window1):
        _translate = QtCore.QCoreApplication.translate
        Window1.setWindowTitle(_translate("Window1", "MainWindow"))
        self.username.setText(_translate("Window1", "Username"))
        self.password.setText(_translate("Window1", "Password"))
        self.pushsignin.setText(_translate("Window1", "Sign In"))
        self.Header.setText(_translate("Window1", "Welcome to LAB TEST 2019"))
        self.menuFile.setTitle(_translate("Window1", "File"))
        self.actionrun.setText(_translate("Window1", "Run"))
        self.actionExit.setText(_translate("Window1", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window1 = QtWidgets.QMainWindow()
    ui = Ui_Window1()
    ui.setupUi(Window1)
    Window1.show()
    sys.exit(app.exec_())

