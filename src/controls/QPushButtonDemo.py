# QPushButton

'''
按钮控件（QPushButton）
常见的按钮类型:
    QAbstractButton
    QPushButton
    AToolButton
    QRadioButton    单选按钮控件
    QCheckBox
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QPushButtonDemo(QDialog) :
    def __init__(self):
        super(QPushButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')

        layout = QVBoxLayout()

        self.button1 = QPushButton('第1个按钮')
        self.button1.setText('First Button 1')   # 设置按钮显示文本
        self.button1.setCheckable(True)     # 设置是否为长选中/长未选中模式, False时默认为点一下自动回弹
        self.button1.toggle()   # 转换按钮的选中状态
        # 一个信号可以绑定多个槽, 先绑定哪个槽, 哪个槽先运行
        self.button1.clicked.connect(self.buttonState)
        # lambda表达式调用, 并穿入按钮参数
        self.button1.clicked.connect(lambda :self.whichButton(self.button1))

        layout.addWidget(self.button1)

        # 在文本前面显示图像(图标)
        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('./images/python.png')))
        self.button2.clicked.connect(lambda:self.whichButton(self.button2))

        layout.addWidget(self.button2)

        # 按钮不可用
        self.button3 = QPushButton('不可用的按钮')
        self.button3.setEnabled(False)

        layout.addWidget(self.button3)

        # 设置回车键默认指向按钮
        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)   # 设置为默认按钮
        self.button4.clicked.connect(lambda:self.whichButton(self.button4))

        layout.addWidget(self.button4)

        self.setLayout(layout)
        self.resize(400,300)

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮1已经被选中')
        else:
            print('按钮1未被选中')

    # 传入btn参数
    def whichButton(self,btn):
        print('被单击的按钮是<' + btn.text() + '>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())
