'''
计数器控件（QSpinBox）
    计数器控件用于显示数字, 数字可以手工输入, 也可以通过小按钮调节;
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSpinBox演示')
        self.resize(300,100)

        layout = QVBoxLayout()
        self.label = QLabel('当前值')
        # 只用居中对齐
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.sb = QSpinBox()
        self.sb.setValue(18)    # 设置计数器控件默认值
        self.sb.setRange(1,150)     # 设置计数器控件数字范围
        self.sb.setSingleStep(2)    # 设置按钮更改步长
        layout.addWidget(self.sb)
        # 当计数器控件值改变时触发valueChanged事件
        self.sb.valueChanged.connect(self.valueChange)
        self.setLayout(layout)

    def valueChange(self):
        self.label.setText('当前值：' + str(self.sb.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec_())