'''
Created on Oct 23, 2020

@author: Sakshi
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_event.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_DialogAddEvent(object):
    def setupUi(self, DialogAddEvent):
        DialogAddEvent.setObjectName("DialogAddEvent")
        DialogAddEvent.resize(461, 615)
        DialogAddEvent.setStyleSheet("QDialog{background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0.895, y2:0.142045, stop:0 rgba(0, 0, 0, 255), stop:0.920398 rgba(21, 209, 255, 255));}")
        self.gridLayout = QtWidgets.QGridLayout(DialogAddEvent)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(DialogAddEvent)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pbAdd = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(14)
        self.pbAdd.setFont(font)
        self.pbAdd.setObjectName("pbAdd")
        self.gridLayout_2.addWidget(self.pbAdd, 0, 0, 1, 1)
        self.pbClear = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(14)
        self.pbClear.setFont(font)
        self.pbClear.setObjectName("pbClear")
        self.gridLayout_2.addWidget(self.pbClear, 0, 1, 1, 1)
        self.pbCancel = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(14)
        self.pbCancel.setFont(font)
        self.pbCancel.setObjectName("pbCancel")
        self.gridLayout_2.addWidget(self.pbCancel, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 11, 0, 1, 6)
        spacerItem = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 4, 2, 1, 1)
        self.lblAttachQuote = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(14)
        self.lblAttachQuote.setFont(font)
        self.lblAttachQuote.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblAttachQuote.setObjectName("lblAttachQuote")
        self.gridLayout_3.addWidget(self.lblAttachQuote, 9, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 113, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 10, 4, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 10, 2, 1, 1)
        self.listQuotes = QtWidgets.QListWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(14)
        self.listQuotes.setFont(font)
        self.listQuotes.setObjectName("listQuotes")
        item = QtWidgets.QListWidgetItem()
        self.listQuotes.addItem(item)
        self.gridLayout_3.addWidget(self.listQuotes, 9, 1, 1, 5)
        self.lblFrom = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(14)
        self.lblFrom.setFont(font)
        self.lblFrom.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblFrom.setObjectName("lblFrom")
        self.gridLayout_3.addWidget(self.lblFrom, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 4, 1, 1, 1)
        self.lblTo = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(14)
        self.lblTo.setFont(font)
        self.lblTo.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblTo.setObjectName("lblTo")
        self.gridLayout_3.addWidget(self.lblTo, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 3, 6, 1, 1)
        self.lblEventName = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(14)
        self.lblEventName.setFont(font)
        self.lblEventName.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblEventName.setObjectName("lblEventName")
        self.gridLayout_3.addWidget(self.lblEventName, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem6, 2, 1, 1, 1)
        self.lblNotes = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(14)
        self.lblNotes.setFont(font)
        self.lblNotes.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblNotes.setObjectName("lblNotes")
        self.gridLayout_3.addWidget(self.lblNotes, 7, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem7, 8, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 6, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 6, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem10, 8, 2, 1, 1)
        self.leNotes = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(14)
        self.leNotes.setFont(font)
        self.leNotes.setObjectName("leNotes")
        self.gridLayout_3.addWidget(self.leNotes, 7, 1, 1, 5)
        self.timeEditFrom = QtWidgets.QTimeEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(14)
        self.timeEditFrom.setFont(font)
        self.timeEditFrom.setObjectName("timeEditFrom")
        self.gridLayout_3.addWidget(self.timeEditFrom, 3, 1, 1, 5)
        self.timeEditTo = QtWidgets.QTimeEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(14)
        self.timeEditTo.setFont(font)
        self.timeEditTo.setObjectName("timeEditTo")
        self.gridLayout_3.addWidget(self.timeEditTo, 5, 1, 1, 5)
        self.textEditEventName = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tekton-BoldOblique")
        font.setPointSize(14)
        self.textEditEventName.setFont(font)
        self.textEditEventName.setObjectName("textEditEventName")
        self.gridLayout_3.addWidget(self.textEditEventName, 0, 1, 2, 5)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.lblAttachQuote.setBuddy(self.listQuotes)
        self.lblFrom.setBuddy(self.timeEditFrom)
        self.lblTo.setBuddy(self.timeEditTo)
        self.lblEventName.setBuddy(self.textEditEventName)
        self.lblNotes.setBuddy(self.leNotes)

        self.retranslateUi(DialogAddEvent)
        self.pbClear.clicked.connect(self.textEditEventName.clear)
        self.pbClear.clicked.connect(self.timeEditFrom.clear)
        self.pbClear.clicked.connect(self.timeEditTo.clear)
        self.pbClear.clicked.connect(self.leNotes.clear)
        self.pbClear.clicked.connect(self.listQuotes.clearSelection)
        self.pbCancel.clicked.connect(DialogAddEvent.close)
        QtCore.QMetaObject.connectSlotsByName(DialogAddEvent)
        #self.addEventClicked()

    def addEventClicked(self):
        connection = sqlite3.connect("myTable.db") 
  
# cursor  
        crsr = connection.cursor() 
          
        # SQL command to create a table in the database 
        sql_command = """CREATE TABLE emp (  
        staff_number INTEGER PRIMARY KEY,  
        fname VARCHAR(20),  
        lname VARCHAR(30),  
        gender CHAR(1),  
        joining DATE);"""
          
        # execute the statement 
        crsr.execute(sql_command) 
          
        # SQL command to insert the data in the table 
        sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
        crsr.execute(sql_command) 
        print("hi")  
        # another SQL command to insert the data in the table 
        sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
        crsr.execute(sql_command) 
        connection.commit() 
        print("bye")
# close the connection 
        connection.close() 
    def retranslateUi(self, DialogAddEvent):
        _translate = QtCore.QCoreApplication.translate
        DialogAddEvent.setWindowTitle(_translate("DialogAddEvent", "Dialog"))
        self.pbAdd.setText(_translate("DialogAddEvent", "Add"))
        self.pbClear.setText(_translate("DialogAddEvent", "Clear"))
        self.pbCancel.setText(_translate("DialogAddEvent", "Cancel"))
        self.lblAttachQuote.setText(_translate("DialogAddEvent", "Attach Quote"))
        __sortingEnabled = self.listQuotes.isSortingEnabled()
        self.listQuotes.setSortingEnabled(False)
        item = self.listQuotes.item(0)
        item.setText(_translate("DialogAddEvent", "Select quote"))
        self.listQuotes.setSortingEnabled(__sortingEnabled)
        self.lblFrom.setText(_translate("DialogAddEvent", "From"))
        self.lblTo.setText(_translate("DialogAddEvent", "To"))
        self.lblEventName.setText(_translate("DialogAddEvent", "Event Name"))
        self.lblNotes.setText(_translate("DialogAddEvent", "Notes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAddEvent = QtWidgets.QDialog()
    ui = Ui_DialogAddEvent()
    ui.setupUi(DialogAddEvent)
    DialogAddEvent.show()
    sys.exit(app.exec_())

