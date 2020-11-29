import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
# 用于添加图标
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    # 初始化函数
    def __init__(self):
        super(FirstMainWin,self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')

        # 设置窗口的尺寸
        self.resize(400,300)

        # 获取窗口的状态栏
        self.status = self.statusBar()
        # 状态栏上显示信息
        self.status.showMessage('只存在10秒的消息',10000)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 设置图标
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())