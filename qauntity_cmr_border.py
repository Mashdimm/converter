# Form implementation generated from reading ui file 'qauntity_cmr_border.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Qauntity_Border_CMR(object):
    def setupUi(self, Qauntity_Border_CMR):
        Qauntity_Border_CMR.setObjectName("Qauntity_Border_CMR")
        Qauntity_Border_CMR.resize(566, 242)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Qauntity_Border_CMR.sizePolicy().hasHeightForWidth())
        Qauntity_Border_CMR.setSizePolicy(sizePolicy)
        Qauntity_Border_CMR.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        Qauntity_Border_CMR.setStyleSheet("QDialog {\n"
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
"}\n"
"\n"
"QLabel {\n"
"    background-color: rgb(22, 25, 31);\n"
"    color: white;\n"
"    font-size: 12pt;\n"
"    font-weight: 700;\n"
"    font-family: RussoOne-Regular;\n"
"    border: 1px ;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    spacing: 10 px;\n"
"    color: white;\n"
"    font-family: RussoOne-Regular;\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"    background-color: rgb(22, 25, 31);\n"
"    border: 2px solid grey;\n"
"    border-radius: 10px;\n"
"   \n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Qauntity_Border_CMR)
        self.gridLayout.setObjectName("gridLayout")
        self.country_lbl = QtWidgets.QLabel(parent=Qauntity_Border_CMR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.country_lbl.sizePolicy().hasHeightForWidth())
        self.country_lbl.setSizePolicy(sizePolicy)
        self.country_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.country_lbl.setObjectName("country_lbl")
        self.gridLayout.addWidget(self.country_lbl, 0, 1, 1, 2)
        self.btn_brd_qunt_ok = QtWidgets.QPushButton(parent=Qauntity_Border_CMR)
        self.btn_brd_qunt_ok.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_brd_qunt_ok.sizePolicy().hasHeightForWidth())
        self.btn_brd_qunt_ok.setSizePolicy(sizePolicy)
        self.btn_brd_qunt_ok.setObjectName("btn_brd_qunt_ok")
        self.gridLayout.addWidget(self.btn_brd_qunt_ok, 6, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.lbl_brd_cmr = QtWidgets.QLabel(parent=Qauntity_Border_CMR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_brd_cmr.sizePolicy().hasHeightForWidth())
        self.lbl_brd_cmr.setSizePolicy(sizePolicy)
        self.lbl_brd_cmr.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.lbl_brd_cmr.setStyleSheet("QLabel {\n"
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
        self.lbl_brd_cmr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_brd_cmr.setObjectName("lbl_brd_cmr")
        self.gridLayout.addWidget(self.lbl_brd_cmr, 4, 2, 1, 1)
        self.spn_qunt = QtWidgets.QSpinBox(parent=Qauntity_Border_CMR)
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
        self.spn_qunt.setMinimum(1)
        self.spn_qunt.setMaximum(20)
        self.spn_qunt.setObjectName("spn_qunt")
        self.gridLayout.addWidget(self.spn_qunt, 4, 1, 1, 1)
        self.rdb_lt = QtWidgets.QRadioButton(parent=Qauntity_Border_CMR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdb_lt.sizePolicy().hasHeightForWidth())
        self.rdb_lt.setSizePolicy(sizePolicy)
        self.rdb_lt.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.rdb_lt.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.rdb_lt.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.rdb_lt.setObjectName("rdb_lt")
        self.gridLayout.addWidget(self.rdb_lt, 1, 1, 1, 1)
        self.rdb_ee = QtWidgets.QRadioButton(parent=Qauntity_Border_CMR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdb_ee.sizePolicy().hasHeightForWidth())
        self.rdb_ee.setSizePolicy(sizePolicy)
        self.rdb_ee.setObjectName("rdb_ee")
        self.gridLayout.addWidget(self.rdb_ee, 1, 2, 1, 1)

        self.retranslateUi(Qauntity_Border_CMR)
        QtCore.QMetaObject.connectSlotsByName(Qauntity_Border_CMR)
        Qauntity_Border_CMR.setTabOrder(self.spn_qunt, self.btn_brd_qunt_ok)

    def retranslateUi(self, Qauntity_Border_CMR):
        _translate = QtCore.QCoreApplication.translate
        Qauntity_Border_CMR.setWindowTitle(_translate("Qauntity_Border_CMR", "Количество CMR"))
        self.country_lbl.setText(_translate("Qauntity_Border_CMR", "Страна пересечения"))
        self.btn_brd_qunt_ok.setText(_translate("Qauntity_Border_CMR", "OK"))
        self.lbl_brd_cmr.setText(_translate("Qauntity_Border_CMR", "Количество CMR"))
        self.rdb_lt.setText(_translate("Qauntity_Border_CMR", "LT, PL"))
        self.rdb_ee.setText(_translate("Qauntity_Border_CMR", "FI, EE, LV, RO"))
