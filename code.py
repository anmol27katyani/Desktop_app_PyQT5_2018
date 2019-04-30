# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'code.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window2(object):
    def logincheck(self):
        user="sd"
        user = self.code.toPlainText()
        print(user)
    def setupUi(self, Window2):
        Window2.setObjectName("Window2")
        Window2.resize(1003, 740)
        self.centralwidget = QtWidgets.QWidget(Window2)
        self.centralwidget.setObjectName("centralwidget")
        self.Question = QtWidgets.QLabel(self.centralwidget)
        self.Question.setGeometry(QtCore.QRect(10, 30, 841, 41))
        self.Question.setObjectName("Question")
        self.scroller = QtWidgets.QScrollArea(self.centralwidget)
        self.scroller.setGeometry(QtCore.QRect(20, 70, 841, 441))
        self.scroller.setWidgetResizable(True)
        self.scroller.setObjectName("scroller")
        self.scrollContents = QtWidgets.QWidget()
        self.scrollContents.setGeometry(QtCore.QRect(0, 0, 839, 439))
        self.scrollContents.setObjectName("scrollContents")
        self.code = QtWidgets.QPlainTextEdit(self.scrollContents)
        self.code.setGeometry(QtCore.QRect(0, 0, 841, 441))
        self.code.setObjectName("code")
        self.scroller.setWidget(self.scrollContents)
        self.submitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.submitbutton.setGeometry(QtCore.QRect(770, 520, 113, 32))
        self.submitbutton.setObjectName("submitbutton")
        ##
        self.submitbutton.clicked.connect(self.logincheck)
        ##
        Window2.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Window2)
        self.statusBar.setObjectName("statusBar")
        Window2.setStatusBar(self.statusBar)
        self.actionRun = QtWidgets.QAction(Window2)
        self.actionRun.setObjectName("actionRun")
        self.actionExit = QtWidgets.QAction(Window2)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(Window2)
        QtCore.QMetaObject.connectSlotsByName(Window2)

    def retranslateUi(self, Window2):
        _translate = QtCore.QCoreApplication.translate
        Window2.setWindowTitle(_translate("Window2", "MainWindow"))
        self.Question.setText(_translate("Window2", "Question: Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’?"))
        self.submitbutton.setText(_translate("Window2", "Submit"))
        self.actionRun.setText(_translate("Window2", "Run"))
        self.actionExit.setText(_translate("Window2", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window2 = QtWidgets.QMainWindow()
    ui = Ui_Window2()
    ui.setupUi(Window2)
    Window2.show()
    sys.exit(app.exec_())

