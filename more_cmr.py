# Form implementation generated from reading ui file 'more_cmr.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_one_cmr(object):
    def setupUi(self, one_cmr):
        one_cmr.setObjectName("one_cmr")
        one_cmr.resize(597, 461)
        one_cmr.setStyleSheet("QDialog {\n"
"    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid gray;\n"
"    border-radius: 20px;\n"
"    \n"
"    \n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(22, 25, 31);\n"
"    color: white;\n"
"    font-size: 10pt;\n"
"    font-weight: 700;\n"
"    font-family: RussoOne-Regular;\n"
"    \n"
"    border: 1px;\n"
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
"    color: white;\n"
"    font-family: RussoOne-Regular;\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"    background: rgb(76, 81, 93);\n"
"    min-width: 26ex;\n"
"    min-height: 4ex;\n"
"    \n"
"    border: 1px;\n"
"    border-radius: 20px;\n"
"    \n"
"}\n"
"\n"
"QComboBox {\n"
"    color: white;\n"
"    font-family: RussoOne-Regular;\n"
"    font-size: 10pt;\n"
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
"}\n"
"\n"
"QLineEdit {\n"
"    color: white;\n"
"    font-family: RussoOne-Regular;\n"
"    font-size: 12pt;\n"
"    font-weight: 600;\n"
"    background: rgb(76, 81, 93);\n"
"    border:1px;\n"
"\n"
"    border-radius: 20px;\n"
"   \n"
"    \n"
"\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(one_cmr)
        self.gridLayout.setObjectName("gridLayout")
        self.cmb_contr_dest = QtWidgets.QComboBox(parent=one_cmr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_contr_dest.sizePolicy().hasHeightForWidth())
        self.cmb_contr_dest.setSizePolicy(sizePolicy)
        self.cmb_contr_dest.setObjectName("cmb_contr_dest")
        self.gridLayout.addWidget(self.cmb_contr_dest, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.lbl_nbr_cmr = QtWidgets.QLabel(parent=one_cmr)
        font = QtGui.QFont()
        font.setFamily("RussoOne-Regular")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nbr_cmr.setFont(font)
        self.lbl_nbr_cmr.setObjectName("lbl_nbr_cmr")
        self.gridLayout.addWidget(self.lbl_nbr_cmr, 1, 0, 1, 1)
        self.lbl_qunt_cll = QtWidgets.QLabel(parent=one_cmr)
        font = QtGui.QFont()
        font.setFamily("RussoOne-Regular")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_qunt_cll.setFont(font)
        self.lbl_qunt_cll.setObjectName("lbl_qunt_cll")
        self.gridLayout.addWidget(self.lbl_qunt_cll, 5, 0, 1, 1)
        self.lne_numb_inv = QtWidgets.QLineEdit(parent=one_cmr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lne_numb_inv.sizePolicy().hasHeightForWidth())
        self.lne_numb_inv.setSizePolicy(sizePolicy)
        self.lne_numb_inv.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.lne_numb_inv.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lne_numb_inv.setObjectName("lne_numb_inv")
        self.gridLayout.addWidget(self.lne_numb_inv, 2, 1, 1, 1)
        self.lne_numb_cmr = QtWidgets.QLineEdit(parent=one_cmr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lne_numb_cmr.sizePolicy().hasHeightForWidth())
        self.lne_numb_cmr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("RussoOne-Regular")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
        self.lne_numb_cmr.setFont(font)
        self.lne_numb_cmr.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.lne_numb_cmr.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lne_numb_cmr.setObjectName("lne_numb_cmr")
        self.gridLayout.addWidget(self.lne_numb_cmr, 1, 1, 1, 1)
        self.lbl_nbr_inv = QtWidgets.QLabel(parent=one_cmr)
        font = QtGui.QFont()
        font.setFamily("RussoOne-Regular")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nbr_inv.setFont(font)
        self.lbl_nbr_inv.setObjectName("lbl_nbr_inv")
        self.gridLayout.addWidget(self.lbl_nbr_inv, 2, 0, 1, 1)
        self.lbl_countr_dest = QtWidgets.QLabel(parent=one_cmr)
        font = QtGui.QFont()
        font.setFamily("RussoOne-Regular")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_countr_dest.setFont(font)
        self.lbl_countr_dest.setObjectName("lbl_countr_dest")
        self.gridLayout.addWidget(self.lbl_countr_dest, 4, 0, 1, 1)
        self.lbl_count_disp = QtWidgets.QLabel(parent=one_cmr)
        font = QtGui.QFont()
        font.setFamily("RussoOne-Regular")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_count_disp.setFont(font)
        self.lbl_count_disp.setObjectName("lbl_count_disp")
        self.gridLayout.addWidget(self.lbl_count_disp, 3, 0, 1, 1)
        self.btn_ok = QtWidgets.QPushButton(parent=one_cmr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ok.sizePolicy().hasHeightForWidth())
        self.btn_ok.setSizePolicy(sizePolicy)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.btn_ok, 7, 0, 1, 2)
        self.qaunt_cll = QtWidgets.QLineEdit(parent=one_cmr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qaunt_cll.sizePolicy().hasHeightForWidth())
        self.qaunt_cll.setSizePolicy(sizePolicy)
        self.qaunt_cll.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.qaunt_cll.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.qaunt_cll.setObjectName("qaunt_cll")
        self.gridLayout.addWidget(self.qaunt_cll, 5, 1, 1, 1)
        self.cmb_count_disp = QtWidgets.QComboBox(parent=one_cmr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_count_disp.sizePolicy().hasHeightForWidth())
        self.cmb_count_disp.setSizePolicy(sizePolicy)
        self.cmb_count_disp.setEditable(False)
        self.cmb_count_disp.setObjectName("cmb_count_disp")
        self.gridLayout.addWidget(self.cmb_count_disp, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 1)

        self.retranslateUi(one_cmr)
        QtCore.QMetaObject.connectSlotsByName(one_cmr)
        one_cmr.setTabOrder(self.lne_numb_cmr, self.lne_numb_inv)
        one_cmr.setTabOrder(self.lne_numb_inv, self.cmb_count_disp)
        one_cmr.setTabOrder(self.cmb_count_disp, self.cmb_contr_dest)
        one_cmr.setTabOrder(self.cmb_contr_dest, self.qaunt_cll)
        one_cmr.setTabOrder(self.qaunt_cll, self.btn_ok)

    def retranslateUi(self, one_cmr):
        _translate = QtCore.QCoreApplication.translate
        one_cmr.setWindowTitle(_translate("one_cmr", "Dialog"))
        self.lbl_nbr_cmr.setText(_translate("one_cmr", "    Номер CMR"))
        self.lbl_qunt_cll.setText(_translate("one_cmr", "    Количество мест"))
        self.lbl_nbr_inv.setText(_translate("one_cmr", "    Номер инвойса"))
        self.lbl_countr_dest.setText(_translate("one_cmr", "    Страна назначения"))
        self.lbl_count_disp.setText(_translate("one_cmr", "    Страна отправления  "))
        self.btn_ok.setText(_translate("one_cmr", "OK"))
