import sys

# QApplication  代表整个应用程序
# QWidget   代表一个窗口
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()

    # 设置窗口的尺寸
    # 参数为长,宽, 单位为px
    w.resize(1920,1080)

    # 移动窗口
    # 即窗口初始化时左上角定位
    # 参数为X轴坐标, Y轴坐标
    w.move(0,0)

    # 设置窗口的标题
    w.setWindowTitle('第一个基于PyQt5的桌面应用 helloWorld')
    # 显示窗口
    w.show()

    # 进入程序的主循环、并通过sys.exit函数确保主循环安全结束(主要是释放资源等)
    # app.exec_()函数开启程序主循环
    sys.exit(app.exec_())
