'''
Created on Oct 23, 2020

@author: Sakshi
'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogAddQuote(object):
    def setupUi(self, DialogAddQuote):
        DialogAddQuote.setObjectName("DialogAddQuote")
        DialogAddQuote.resize(400, 300)
        DialogAddQuote.setStyleSheet("QDialog{background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0.895, y2:0.142045, stop:0 rgba(0, 0, 0, 255), stop:0.920398 rgba(21, 209, 255, 255));}")
        self.gridLayout = QtWidgets.QGridLayout(DialogAddQuote)
        self.gridLayout.setObjectName("gridLayout")
        self.textEditQuote = QtWidgets.QTextEdit(DialogAddQuote)
        font = QtGui.QFont()
        font.setFamily("Tekton Pro")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEditQuote.setFont(font)
        self.textEditQuote.setObjectName("textEditQuote")
        self.gridLayout.addWidget(self.textEditQuote, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(375, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(DialogAddQuote)
        self.frame.setStyleSheet("QDialog{background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0.895, y2:0.142045, stop:0 rgba(0, 0, 0, 255), stop:0.920398 rgba(21, 209, 255, 255));}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.pbCancelAddQuote = QtWidgets.QPushButton(self.frame)
        self.pbCancelAddQuote.setObjectName("pbCancelAddQuote")
        self.gridLayout_2.addWidget(self.pbCancelAddQuote, 0, 2, 1, 1)
        self.pbQuoteSave = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbQuoteSave.sizePolicy().hasHeightForWidth())
        self.pbQuoteSave.setSizePolicy(sizePolicy)
        self.pbQuoteSave.setObjectName("pbQuoteSave")
        self.gridLayout_2.addWidget(self.pbQuoteSave, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)

        self.retranslateUi(DialogAddQuote)
        self.pbCancelAddQuote.clicked.connect(DialogAddQuote.close)
        self.pbQuoteSave.clicked.connect(self.textEditQuote.selectAll)
        QtCore.QMetaObject.connectSlotsByName(DialogAddQuote)

    def retranslateUi(self, DialogAddQuote):
        _translate = QtCore.QCoreApplication.translate
        DialogAddQuote.setWindowTitle(_translate("DialogAddQuote", "Dialog"))
        self.textEditQuote.setPlaceholderText(_translate("DialogAddQuote", "Add your quote here"))
        self.pbCancelAddQuote.setText(_translate("DialogAddQuote", "Cancel"))
        self.pbQuoteSave.setText(_translate("DialogAddQuote", "Save"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAddQuote = QtWidgets.QDialog()
    ui = Ui_DialogAddQuote()
    ui.setupUi(DialogAddQuote)
    DialogAddQuote.show()
    sys.exit(app.exec_())
'''
