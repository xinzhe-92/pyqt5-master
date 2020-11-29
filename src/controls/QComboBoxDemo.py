'''
下拉列表控件（QComboBox）
    1. 如何将列表项添加到QComboBox控件中
    2. 如何获取选中的列表项
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表控件演示')
        self.resize(300,100)

        layout = QVBoxLayout()

        self.label = QLabel('请选择编程语言')

        self.cb = QComboBox()
        # 两种添加列表项的方式
        self.cb.addItem('Python')
        self.cb.addItems(['Java','C#','Ruby','C++', 'aaaaaaaaaaaaaaaa'])

        # 当更改下拉框值时触发事件currentIndexChanged
        # Activated	当用户选中一个下拉选项时发射该信号
        # currentIndexChanged	当下拉选项的索引发生改变时发射该信号
        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)

    def selectionChange(self,i):
        # cb.currentText()用于获取当前选择的文本
        self.label.setText(self.cb.currentText())
        # label重新调整尺寸, 动态调整
        self.label.adjustSize()

        # 遍历下标, 获取下拉列表项
        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))

        # i为当前获取列表项的下标
        print('current index',i,'selection changed', self.cb.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())