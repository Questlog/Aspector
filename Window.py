# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window.ui'
#
# Created: Thu May 22 01:35:27 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dialogAspector(object):
    def setupUi(self, dialogAspector):
        dialogAspector.setObjectName(_fromUtf8("dialogAspector"))
        dialogAspector.setEnabled(True)
        dialogAspector.resize(310, 464)
        dialogAspector.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(dialogAspector)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(dialogAspector)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label = QtGui.QLabel(dialogAspector)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.listWidgetFrom = QtGui.QListWidget(dialogAspector)
        self.listWidgetFrom.setIconSize(QtCore.QSize(50, 50))
        self.listWidgetFrom.setObjectName(_fromUtf8("listWidgetFrom"))
        self.gridLayout.addWidget(self.listWidgetFrom, 2, 0, 1, 2)
        self.spinBox = QtGui.QSpinBox(dialogAspector)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(15)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 4, 1, 1, 1)
        self.pushButtonGo = QtGui.QPushButton(dialogAspector)
        self.pushButtonGo.setObjectName(_fromUtf8("pushButtonGo"))
        self.gridLayout.addWidget(self.pushButtonGo, 4, 2, 1, 1)
        self.label_3 = QtGui.QLabel(dialogAspector)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.listWidgetTo = QtGui.QListWidget(dialogAspector)
        self.listWidgetTo.setIconSize(QtCore.QSize(50, 50))
        self.listWidgetTo.setObjectName(_fromUtf8("listWidgetTo"))
        self.gridLayout.addWidget(self.listWidgetTo, 2, 2, 1, 1)
        self.scrollArea = QtGui.QScrollArea(dialogAspector)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 150))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 150))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 290, 148))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setMargin(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 5, 0, 1, 3)

        self.retranslateUi(dialogAspector)
        QtCore.QMetaObject.connectSlotsByName(dialogAspector)

    def retranslateUi(self, dialogAspector):
        dialogAspector.setWindowTitle(_translate("dialogAspector", "Aspector", None))
        self.label_2.setText(_translate("dialogAspector", "Nach", None))
        self.label.setText(_translate("dialogAspector", "Von", None))
        self.listWidgetFrom.setSortingEnabled(True)
        self.pushButtonGo.setText(_translate("dialogAspector", "Aspekte suchen", None))
        self.label_3.setText(_translate("dialogAspector", "Länge:", None))
        self.listWidgetTo.setSortingEnabled(True)

