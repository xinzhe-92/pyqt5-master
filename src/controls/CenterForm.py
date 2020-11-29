# 窗口居中示例, 需获取参数后进行计算

# QDesktopWidget
import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm,self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle('让窗口居中')

        # 设置窗口的尺寸
        self.resize(400,300)

        self.center()

    # 计算并移动窗口, 使之居中
    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft,newTop)
        print("test")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CenterForm()
    main.show()

    sys.exit(app.exec_())
