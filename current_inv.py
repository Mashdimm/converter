# Form implementation generated from reading ui file 'current_inv.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Current_inv(object):
    def setupUi(self, Current_inv):
        Current_inv.setObjectName("Current_inv")
        Current_inv.resize(490, 231)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Current_inv.sizePolicy().hasHeightForWidth())
        Current_inv.setSizePolicy(sizePolicy)
        Current_inv.setStyleSheet("QDialog {\n"
"    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    \n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(22, 25, 31);\n"
"    color: white;\n"
"    font-size: 10pt;\n"
"    font-weight: 700;\n"
"    font-family: RussoOne-Regular;\n"
"    border:1px;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #888;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Current_inv)
        self.gridLayout.setObjectName("gridLayout")
        self.country_lbl = QtWidgets.QLabel(parent=Current_inv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.country_lbl.sizePolicy().hasHeightForWidth())
        self.country_lbl.setSizePolicy(sizePolicy)
        self.country_lbl.setMaximumSize(QtCore.QSize(250, 40))
        self.country_lbl.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    font-family: RussoOne-Regular;\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"    background: rgb(76, 81, 93);\n"
"    min-width: 26ex;\n"
"    min-height: 4ex;\n"
"    border:1px;\n"
"    border-radius: 20px;\n"
"    \n"
"}")
        self.country_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.country_lbl.setObjectName("country_lbl")
        self.gridLayout.addWidget(self.country_lbl, 1, 2, 1, 1)
        self.country_cmb = QtWidgets.QComboBox(parent=Current_inv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.country_cmb.sizePolicy().hasHeightForWidth())
        self.country_cmb.setSizePolicy(sizePolicy)
        self.country_cmb.setMinimumSize(QtCore.QSize(104, 16))
        self.country_cmb.setMaximumSize(QtCore.QSize(250, 40))
        self.country_cmb.setStyleSheet("QComboBox {\n"
"    color: white;\n"
"    font-family: RussoOne-Regular;\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"    background: rgb(76, 81, 93);\n"
"    min-width: 26ex;\n"
"    min-height: 4ex;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"    border:1px;\n"
"    border-radius: 20px;\n"
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: rgb(76, 81, 93);\n"
"}\n"
"\n"
"QComboBox:on { \n"
"    background: rgb(76, 81, 93);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  color: white;\n"
"  background-color: rgb(76, 81, 93);\n"
"  \n"
"  selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.country_cmb.setObjectName("country_cmb")
        self.gridLayout.addWidget(self.country_cmb, 1, 1, 1, 1)
        self.current_cmb = QtWidgets.QComboBox(parent=Current_inv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_cmb.sizePolicy().hasHeightForWidth())
        self.current_cmb.setSizePolicy(sizePolicy)
        self.current_cmb.setMinimumSize(QtCore.QSize(104, 16))
        self.current_cmb.setMaximumSize(QtCore.QSize(250, 40))
        self.current_cmb.setStyleSheet("QComboBox {\n"
"    color: white;\n"
"    font-family: RussoOne-Regular;\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"    background: rgb(76, 81, 93);\n"
"    min-width: 26ex;\n"
"    min-height: 4ex;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"    border:1px;\n"
"    border-radius: 20px;\n"
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: rgb(76, 81, 93);\n"
"}\n"
"\n"
"QComboBox:on { \n"
"    background: rgb(76, 81, 93);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  color: white;\n"
"  background-color: rgb(76, 81, 93);\n"
"  \n"
"  selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.current_cmb.setObjectName("current_cmb")
        self.gridLayout.addWidget(self.current_cmb, 0, 1, 1, 1)
        self.lbl_current = QtWidgets.QLabel(parent=Current_inv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_current.sizePolicy().hasHeightForWidth())
        self.lbl_current.setSizePolicy(sizePolicy)
        self.lbl_current.setMinimumSize(QtCore.QSize(104, 16))
        self.lbl_current.setMaximumSize(QtCore.QSize(250, 40))
        self.lbl_current.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.lbl_current.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    font-family: RussoOne-Regular;\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"    background: rgb(76, 81, 93);\n"
"    min-width: 26ex;\n"
"    min-height: 4ex;\n"
"    border:1px;\n"
"    border-radius: 20px;\n"
"    \n"
"}")
        self.lbl_current.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_current.setObjectName("lbl_current")
        self.gridLayout.addWidget(self.lbl_current, 0, 2, 1, 1)
        self.btn_ok = QtWidgets.QPushButton(parent=Current_inv)
        self.btn_ok.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ok.sizePolicy().hasHeightForWidth())
        self.btn_ok.setSizePolicy(sizePolicy)
        self.btn_ok.setMaximumSize(QtCore.QSize(480, 60))
        self.btn_ok.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.btn_ok, 2, 0, 1, 3)

        self.retranslateUi(Current_inv)
        QtCore.QMetaObject.connectSlotsByName(Current_inv)

    def retranslateUi(self, Current_inv):
        _translate = QtCore.QCoreApplication.translate
        Current_inv.setWindowTitle(_translate("Current_inv", "Валюта инвойса"))
        self.country_lbl.setText(_translate("Current_inv", "Страна происхождения"))
        self.lbl_current.setText(_translate("Current_inv", "Валюта инвойса"))
        self.btn_ok.setText(_translate("Current_inv", "OK"))
