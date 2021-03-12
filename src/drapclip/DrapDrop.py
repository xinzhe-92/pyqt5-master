'''
让控件支持拖拽动作
A为被拖拽的
B为接收拖拽的
A.setDragEnabled(True)
B.setAcceptDrops(True)

B需要两个事件
1. dragEnterEvent   将A拖到B时触发
2. dropEvent        在B的区域放下A时触发

'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyComboBox(QComboBox) :
    def __init__(self):
        super(MyComboBox,self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self,e):
        print(e)    # e为dragEnterEvent事件对象
        print(e.mimeData()) # e.mimeData()为获取进入数据的mime对象, 可由此获取
        if e.mimeData().hasText():
            if e.mimeData().text() == "abc":
                e.mimeData().setText("空白")
                e.accept()
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e):
        print(e)
        # checkbox放置文本
        self.addItem(e.mimeData().text())

class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo,self).__init__()

        # 设置表格布局
        formLayout = QFormLayout()
        # 添加说明文本
        formLayout.addRow(QLabel("请将左边的文本拖拽到右边的下拉列表中"))

        # 初始化文本输入标签
        lineEdit = QLineEdit()
        # 让QLineEdit控件可拖动
        lineEdit.setDragEnabled(True)

        # 设置下拉框
        combo = MyComboBox()
        formLayout.addRow(lineEdit,combo)

        self.setLayout(formLayout)
        self.setWindowTitle('拖拽案例')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrapDropDemo()
    main.show()
    sys.exit(app.exec_())