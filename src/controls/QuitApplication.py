# 退出程序示例
# 涉及信号与槽

import sys
# QHBoxLayout   水平布局
# QPushButton   按钮
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,200)
        self.setWindowTitle('退出应用程序')

        # 添加打开Button
        self.openButton = QPushButton('打开文件...')
        self.openButton.clicked.connect(openFIle)

        # 添加退出Button
        self.quitButton = QPushButton('退出应用程序')
        # 将信号与槽关联
        self.quitButton.clicked.connect(self.onClick_Button)
        
        # 设置水平布局
        layout = QHBoxLayout()
        # 向水平布局中添加按钮
        layout.addWidget(self.openButton)
        layout.addWidget(self.quitButton)

        # 设置主框架
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    # 按钮单击事件的方法（自定义的槽）
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + ' 按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()

def openFIle():
    print("打开文件按钮被按下")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())