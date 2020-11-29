# QLineEdit综合案例

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo,self).__init__()
        self.initUI()

    def initUI(self):
        edit1 = QLineEdit()
        # 使用int校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)  # 不超过9999
        edit1.setAlignment(Qt.AlignRight)   # 设置右对齐
        edit1.setFont(QFont('Arial',20))    # 设置字体/字号

        # 使用Double校验器
        edit2 = QLineEdit()
        # 设置为0.99至99.99, 精度为2
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))

        # 使用掩码
        edit3 = QLineEdit()
        # ?表示使用?作为占位符
        edit3.setInputMask('99-9999-999999;?')

        # 文本变化时间演示
        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChanged)

        # 失去焦点, 即编辑完成
        self.edit5 = QLineEdit()
        self.edit5.setEchoMode(QLineEdit.Password)   # 回显模式使用Password
        self.edit5.editingFinished.connect(self.enterPress)

        # 使用只读属性
        edit6 = QLineEdit('Hello PyQt5')
        edit6.setReadOnly(True)


        formLayout = QFormLayout()
        formLayout.addRow('整数校验',edit1)
        formLayout.addRow('浮点数校验',edit2)
        formLayout.addRow('Input Mask',edit3)
        formLayout.addRow('文本变化', edit4)
        formLayout.addRow('密码',self.edit5)
        formLayout.addRow('只读',edit6)
        self.setLayout(formLayout)
        self.setWindowTitle('QLineEdit综合案例')


    def textChanged(self,text):
        print('输入的内容：' + text)

    def enterPress(self):
        print('已输入值'+self.edit5.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditDemo()
    main.show()
    sys.exit(app.exec_())