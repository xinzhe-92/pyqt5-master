'''
颜色对话框：QColorDialog
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Dialog例子')

        layout = QVBoxLayout()

        self.colorButton = QPushButton('设置颜色')
        self.colorButton.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton)

        self.colorButton1 = QPushButton('设置背景颜色')
        self.colorButton1.clicked.connect(self.getBGColor)
        layout.addWidget(self.colorButton1)

        self.colorLabel = QLabel('Hello，测试颜色例子')
        layout.addWidget(self.colorLabel)

        self.setLayout(layout)

    def getColor(self):
        # 获取返回的颜色
        color = QColorDialog.getColor()
        # 初始化并设置调色板
        p = QPalette()
        p.setColor(QPalette.WindowText,color)
        # 应用颜色
        self.colorLabel.setPalette(p)

    def getBGColor(self):
        # 获取返回的颜色
        color = QColorDialog.getColor()
        # 初始化并设置调色板
        p = QPalette()
        p.setColor(QPalette.Window,color)
        # 设置Label控件的自动填充背景色
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())

