# 显示工作窗口和控件的提示消息
# 即鼠标悬停时显示提示信息

import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QToolTip,QPushButton,QWidget
from PyQt5.QtGui import QFont

class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置字体和大小
        QToolTip.setFont(QFont('SansSerif',12))

        # 设置内容工作窗口鼠标悬停显示文本
        # 可用html语言
        self.setToolTip('今天是<h1>星期五</h1>')

        # 设置窗口位置/大小/标题
        self.setGeometry(300,30,500,300)
        self.setWindowTitle('设置控件提示消息')

        # 设置按钮
        self.button1 = QPushButton('我的按钮')
        self.button1.setToolTip('这是一个按钮，Are you ok？')
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()

    sys.exit(app.exec_())
