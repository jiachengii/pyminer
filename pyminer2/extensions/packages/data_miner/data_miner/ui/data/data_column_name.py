# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_column_name.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(824, 600)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.listWidget_var = QtWidgets.QListWidget(self.widget_2)
        self.listWidget_var.setObjectName("listWidget_var")
        self.verticalLayout_2.addWidget(self.listWidget_var)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_8.addWidget(self.widget_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_add = QtWidgets.QPushButton(self.tab)
        self.pushButton_add.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pyqt/source/images/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout_4.addWidget(self.pushButton_add)
        self.pushButton_delete = QtWidgets.QPushButton(self.tab)
        self.pushButton_delete.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pyqt/source/images/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon1)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.verticalLayout_4.addWidget(self.pushButton_delete)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.listWidget_selected = QtWidgets.QListWidget(self.tab)
        self.listWidget_selected.setObjectName("listWidget_selected")
        self.horizontalLayout_4.addWidget(self.listWidget_selected)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_selected_add = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_add.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_add.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pyqt/source/images/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_add.setIcon(icon2)
        self.pushButton_selected_add.setObjectName("pushButton_selected_add")
        self.verticalLayout_6.addWidget(self.pushButton_selected_add)
        self.pushButton_selected_up = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_up.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_up.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pyqt/source/images/up1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_up.setIcon(icon3)
        self.pushButton_selected_up.setObjectName("pushButton_selected_up")
        self.verticalLayout_6.addWidget(self.pushButton_selected_up)
        self.pushButton_selected_down = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_down.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_down.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pyqt/source/images/down1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_down.setIcon(icon4)
        self.pushButton_selected_down.setObjectName("pushButton_selected_down")
        self.verticalLayout_6.addWidget(self.pushButton_selected_down)
        self.pushButton_selected_del = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_del.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_del.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pyqt/source/images/lc_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_del.setIcon(icon5)
        self.pushButton_selected_del.setObjectName("pushButton_selected_del")
        self.verticalLayout_6.addWidget(self.pushButton_selected_del)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.comboBox_columns = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_columns.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_columns.setObjectName("comboBox_columns")
        self.comboBox_columns.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_columns)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        self.lineEdit_replace = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_replace.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_replace.setObjectName("lineEdit_replace")
        self.horizontalLayout_9.addWidget(self.lineEdit_replace)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_prefix_add = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_prefix_add.setObjectName("lineEdit_prefix_add")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_prefix_add)
        self.checkBox_prefix_del = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_prefix_del.setObjectName("checkBox_prefix_del")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox_prefix_del)
        self.lineEdit_prefix_del = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_prefix_del.setObjectName("lineEdit_prefix_del")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_prefix_del)
        self.checkBox_suffix_add = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_suffix_add.setObjectName("checkBox_suffix_add")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBox_suffix_add)
        self.lineEdit_suffix_add = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_suffix_add.setObjectName("lineEdit_suffix_add")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_suffix_add)
        self.checkBox_suffix_del = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_suffix_del.setObjectName("checkBox_suffix_del")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkBox_suffix_del)
        self.lineEdit_suffix_del = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_suffix_del.setObjectName("lineEdit_suffix_del")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_suffix_del)
        self.checkBox_prefix_add = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_prefix_add.setObjectName("checkBox_prefix_add")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox_prefix_add)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_preview = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_preview.setObjectName("pushButton_preview")
        self.horizontalLayout_2.addWidget(self.pushButton_preview)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget_dataset = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_dataset.setObjectName("tableWidget_dataset")
        self.tableWidget_dataset.setColumnCount(0)
        self.tableWidget_dataset.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_dataset)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_13.addWidget(self.tabWidget)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_code = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_code.setObjectName("pushButton_code")
        self.horizontalLayout_3.addWidget(self.pushButton_code)
        self.pushButton_help = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_help.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/pyqt/source/images/lc_helpindex.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_help.setIcon(icon6)
        self.pushButton_help.setObjectName("pushButton_help")
        self.horizontalLayout_3.addWidget(self.pushButton_help)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_ok = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_3.addWidget(self.pushButton_ok)
        self.pushButton_save = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_3.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_13.addWidget(self.widget_3)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数据-列名处理"))
        self.label_3.setText(_translate("Form", "全部变量:"))
        self.label_2.setText(_translate("Form", "已选变量:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "变量"))
        self.comboBox_columns.setItemText(0, _translate("Form", "变量列表"))
        self.label.setText(_translate("Form", "修改为"))
        self.checkBox_prefix_del.setText(_translate("Form", "删除前缀"))
        self.checkBox_suffix_add.setText(_translate("Form", "添加后缀"))
        self.checkBox_suffix_del.setText(_translate("Form", "删除后缀"))
        self.checkBox_prefix_add.setText(_translate("Form", "添加前缀"))
        self.pushButton_preview.setText(_translate("Form", "预览"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "列名处理"))
        self.pushButton_code.setText(_translate("Form", "代码"))
        self.pushButton_ok.setText(_translate("Form", "确定"))
        self.pushButton_save.setText(_translate("Form", "保存"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
import pyqtsource_rc
