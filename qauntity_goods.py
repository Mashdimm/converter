# Form implementation generated from reading ui file 'qauntity_goods.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Qauntity_goods(object):
    def setupUi(self, Qauntity_goods):
        Qauntity_goods.setObjectName("Qauntity_goods")
        Qauntity_goods.resize(430, 140)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Qauntity_goods.sizePolicy().hasHeightForWidth())
        Qauntity_goods.setSizePolicy(sizePolicy)
        Qauntity_goods.setStyleSheet("QDialog {\n"
"    \n"
"  \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid gray;\n"
"    border-radius: 20px;\n"
"        \n"
"}\n"
"    \n"
"    \n"
"\n"
"QPushButton {\n"
"    background-color: rgb(22, 25, 31);\n"
"    color: white;\n"
"    font-size: 10pt;\n"
"    font-weight: 700;\n"
"    font-family: RussoOne-Regular;\n"
"    border: 1px ;\n"
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
        self.gridLayout = QtWidgets.QGridLayout(Qauntity_goods)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_qunt_ok = QtWidgets.QPushButton(parent=Qauntity_goods)
        self.btn_qunt_ok.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_qunt_ok.sizePolicy().hasHeightForWidth())
        self.btn_qunt_ok.setSizePolicy(sizePolicy)
        self.btn_qunt_ok.setObjectName("btn_qunt_ok")
        self.gridLayout.addWidget(self.btn_qunt_ok, 2, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.lbl_qunt_cmr = QtWidgets.QLabel(parent=Qauntity_goods)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_qunt_cmr.sizePolicy().hasHeightForWidth())
        self.lbl_qunt_cmr.setSizePolicy(sizePolicy)
        self.lbl_qunt_cmr.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.lbl_qunt_cmr.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    font-family: RussoOne-Regular;\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"    background: rgb(76, 81, 93);\n"
"    min-width: 26ex;\n"
"    min-height: 4ex;\n"
"    border: 1px;\n"
"    border-radius: 20px;\n"
"    \n"
"}")
        self.lbl_qunt_cmr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_qunt_cmr.setObjectName("lbl_qunt_cmr")
        self.gridLayout.addWidget(self.lbl_qunt_cmr, 0, 2, 1, 1)
        self.spn_qunt = QtWidgets.QSpinBox(parent=Qauntity_goods)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spn_qunt.sizePolicy().hasHeightForWidth())
        self.spn_qunt.setSizePolicy(sizePolicy)
        self.spn_qunt.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.spn_qunt.setStyleSheet("QSpinBox {\n"
"    color: white;\n"
"    font-family: RussoOne-Regular;\n"
"    font-size: 12pt;\n"
"    font-weight: 600;\n"
"    background: rgb(76, 81, 93);\n"
"    min-width: 26ex;\n"
"    min-height: 4ex;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"    border: 1px;\n"
"    border-radius: 20px;\n"
"\n"
"}\n"
"\n"
"QSpinBox:editable {\n"
"    background: rgb(76, 81, 93);\n"
"}\n"
"\n"
"QSpinBox:on { \n"
"    background: rgb(76, 81, 93);\n"
"}\n"
"\n"
"QSpinBox QAbstractItemView {\n"
"  color: white;\n"
"  background-color: rgb(76, 81, 93);\n"
"  \n"
"  selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.spn_qunt.setWrapping(True)
        self.spn_qunt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spn_qunt.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spn_qunt.setMinimum(1)
        self.spn_qunt.setMaximum(5000)
        self.spn_qunt.setProperty("value", 1)
        self.spn_qunt.setObjectName("spn_qunt")
        self.gridLayout.addWidget(self.spn_qunt, 0, 1, 1, 1)

        self.retranslateUi(Qauntity_goods)
        QtCore.QMetaObject.connectSlotsByName(Qauntity_goods)
        Qauntity_goods.setTabOrder(self.spn_qunt, self.btn_qunt_ok)

    def retranslateUi(self, Qauntity_goods):
        _translate = QtCore.QCoreApplication.translate
        Qauntity_goods.setWindowTitle(_translate("Qauntity_goods", "Количество кодов CMR № "))
        self.btn_qunt_ok.setText(_translate("Qauntity_goods", "OK"))
        self.lbl_qunt_cmr.setText(_translate("Qauntity_goods", "Количество кодов"))
