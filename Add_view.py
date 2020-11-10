# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from show_Event import Ui_DialogShowEvent
from Add_event import Ui_DialogAddEvent

class Ui_DialogAddView(object):
    def setupUi(self, DialogAddView):
        DialogAddView.setObjectName("DialogAddView")
        DialogAddView.resize(423, 86)
        DialogAddView.setStyleSheet("QDialog{background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0.895, y2:0.142045, stop:0 rgba(0, 0, 0, 255), stop:0.920398 rgba(21, 209, 255, 255));}")
        self.pushButton = QtWidgets.QPushButton(DialogAddView)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(DialogAddView)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 10, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton.clicked.connect(self.addEventClicked)
        self.pushButton_2.clicked.connect(self.viewEventClicked)

        self.retranslateUi(DialogAddView)
        QtCore.QMetaObject.connectSlotsByName(DialogAddView)

    def addEventClicked(self):
        self.DialogAddEvent = QtWidgets.QDialog()
        self.uiAddEvent = Ui_DialogAddEvent()
        self.uiAddEvent.setupUi(self.DialogAddEvent)
        self.DialogAddEvent.show()
    def viewEventClicked(self):
        self.Dialog = QtWidgets.QDialog()
        self.uiView = Ui_DialogShowEvent()
        self.uiView.setupUi(self.Dialog)
        self.Dialog.show()
    def retranslateUi(self, DialogAddView):
        _translate = QtCore.QCoreApplication.translate
        DialogAddView.setWindowTitle(_translate("DialogAddView", "Dialog"))
        self.pushButton.setText(_translate("DialogAddView", "Add Event"))
        self.pushButton_2.setText(_translate("DialogAddView", "View Event"))
'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAddView = QtWidgets.QDialog()
    ui = Ui_DialogAddView()
    ui.setupUi(DialogAddView)
    DialogAddView.show()
    sys.exit(app.exec_())
'''
