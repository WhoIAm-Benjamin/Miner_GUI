# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_mw(object):
    def setupUi(self, mw):
        mw.setObjectName("mw")
        mw.resize(387, 111)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        mw.setFont(font)
        mw.setStyleSheet("background-color: rgb(37, 33, 39);\n"
"color: rgb(208, 208, 208);")
        self.centralwidget = QtWidgets.QWidget(mw)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(15, 15, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.defmain = QtWidgets.QSlider(self.centralwidget)
        self.defmain.setGeometry(QtCore.QRect(125, 67, 160, 19))
        self.defmain.setStyleSheet("")
        self.defmain.setMaximum(1)
        self.defmain.setPageStep(1)
        self.defmain.setOrientation(QtCore.Qt.Horizontal)
        self.defmain.setObjectName("defmain")
        self.label_miner = QtWidgets.QLabel(self.centralwidget)
        self.label_miner.setGeometry(QtCore.QRect(19, 60, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_miner.setFont(font)
        self.label_miner.setObjectName("label_miner")
        self.miner_st = QtWidgets.QLabel(self.centralwidget)
        self.miner_st.setGeometry(QtCore.QRect(319, 60, 47, 30))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(18)
        self.miner_st.setFont(font)
        self.miner_st.setStyleSheet("color: rgb(186, 2, 2);")
        self.miner_st.setObjectName("miner_st")
        mw.setCentralWidget(self.centralwidget)

        self.retranslateUi(mw)
        QtCore.QMetaObject.connectSlotsByName(mw)

    def retranslateUi(self, mw):
        _translate = QtCore.QCoreApplication.translate
        mw.setWindowTitle(_translate("mw", "CryptoTab Miner Lite"))
        self.label_name.setText(_translate("mw", "CryptoTab Miner"))
        self.label_miner.setText(_translate("mw", "Miner"))
        self.miner_st.setText(_translate("mw", "OFF"))
