# 主窗口水平布局

import sys
# 导入已经ui文件转化生成好的py文件
import MainWinHorizontalLayout
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    # 创建app对象, app代表整个应用程序
    app = QApplication(sys.argv)

    # 创建主窗口对象
    mainWindow = QMainWindow()

    # ui中关联已经生成好的py文件
    ui = MainWinHorizontalLayout.Ui_MainWindow()

    # 向主窗口上添加控件
    # 关联绑定好的ui和mainWindow对象
    ui.setupUi(mainWindow)

    # 运行
    mainWindow.show()
    sys.exit(app.exec_())