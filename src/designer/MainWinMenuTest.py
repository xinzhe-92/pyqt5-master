# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinMenuTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menu)
        self.menu_3.setObjectName("menu_3")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionopen_zuijin = QtWidgets.QAction(MainWindow)
        self.actionopen_zuijin.setObjectName("actionopen_zuijin")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actioncut = QtWidgets.QAction(MainWindow)
        self.actioncut.setObjectName("actioncut")
        self.actioncopy = QtWidgets.QAction(MainWindow)
        self.actioncopy.setObjectName("actioncopy")
        self.actiondelete = QtWidgets.QAction(MainWindow)
        self.actiondelete.setObjectName("actiondelete")
        self.actionword = QtWidgets.QAction(MainWindow)
        self.actionword.setObjectName("actionword")
        self.menu_3.addAction(self.actionword)
        self.menu.addAction(self.menu_3.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.actionopen_zuijin)
        self.menu.addSeparator()
        self.menu.addAction(self.actionclose)
        self.menu_2.addAction(self.actioncut)
        self.menu_2.addAction(self.actioncopy)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actiondelete)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addAction(self.actioncut)
        self.toolBar.addAction(self.actioncopy)
        self.toolBar.addAction(self.actiondelete)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_3.setTitle(_translate("MainWindow", "新建"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionopen.setText(_translate("MainWindow", "打开"))
        self.actionopen_zuijin.setText(_translate("MainWindow", "打开最近"))
        self.actionclose.setText(_translate("MainWindow", "关闭"))
        self.actioncut.setText(_translate("MainWindow", "剪切"))
        self.actioncopy.setText(_translate("MainWindow", "复制"))
        self.actiondelete.setText(_translate("MainWindow", "删除"))
        self.actionword.setText(_translate("MainWindow", "新建word"))
        self.actionword.setShortcut(_translate("MainWindow", "Ctrl+A"))
