# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model_woe_result.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pyqt/source/images/logo (5).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(60, 25))
        self.label.setMaximumSize(QtCore.QSize(50, 25))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setEnabled(True)
        self.comboBox.setMinimumSize(QtCore.QSize(60, 22))
        self.comboBox.setMaximumSize(QtCore.QSize(60, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setMinimumSize(QtCore.QSize(60, 22))
        self.comboBox_2.setMaximumSize(QtCore.QSize(60, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMinimumSize(QtCore.QSize(90, 22))
        self.lineEdit.setMaximumSize(QtCore.QSize(120, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setMinimumSize(QtCore.QSize(30, 22))
        self.toolButton.setMaximumSize(QtCore.QSize(30, 22))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(30, 25))
        self.label_2.setMaximumSize(QtCore.QSize(30, 25))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(50, 22))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(50, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 22))
        self.pushButton.setMaximumSize(QtCore.QSize(60, 22))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 22))
        self.pushButton_2.setMaximumSize(QtCore.QSize(60, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_export = QtWidgets.QPushButton(Form)
        self.pushButton_export.setMinimumSize(QtCore.QSize(60, 22))
        self.pushButton_export.setMaximumSize(QtCore.QSize(60, 22))
        self.pushButton_export.setObjectName("pushButton_export")
        self.horizontalLayout.addWidget(self.pushButton_export)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tableWidget_woe_iv = QtWidgets.QTableWidget(Form)
        self.tableWidget_woe_iv.setMinimumSize(QtCore.QSize(500, 400))
        self.tableWidget_woe_iv.setObjectName("tableWidget_woe_iv")
        self.tableWidget_woe_iv.setColumnCount(0)
        self.tableWidget_woe_iv.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_woe_iv, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "WOE和IV"))
        self.label.setText(_translate("Form", "查询条件："))
        self.comboBox.setItemText(0, _translate("Form", "无"))
        self.comboBox.setItemText(1, _translate("Form", "变量名称"))
        self.comboBox.setItemText(2, _translate("Form", "WOE"))
        self.comboBox.setItemText(3, _translate("Form", "IV"))
        self.comboBox_2.setItemText(0, _translate("Form", "等于"))
        self.comboBox_2.setItemText(1, _translate("Form", "大于"))
        self.comboBox_2.setItemText(2, _translate("Form", "大于等于"))
        self.comboBox_2.setItemText(3, _translate("Form", "小于"))
        self.comboBox_2.setItemText(4, _translate("Form", "小于等于"))
        self.comboBox_2.setItemText(5, _translate("Form", "不等于"))
        self.comboBox_2.setItemText(6, _translate("Form", "包含"))
        self.toolButton.setText(_translate("Form", "..."))
        self.label_2.setText(_translate("Form", "精度："))
        self.pushButton.setText(_translate("Form", "应用"))
        self.pushButton_2.setText(_translate("Form", "重置"))
        self.pushButton_export.setText(_translate("Form", "导出"))
import pyqtsource_rc