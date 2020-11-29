# 获取窗口大小和屏幕坐标系相对位置示例
# 未使用面向对象

import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget

# 自定义槽
def onClick_Button():
    print("输出窗口的数据(不含边框标头):")
    print("widget.x() = %d" % widget.x())    # 500 （窗口横坐标）
    print("widget.y() = %d" % widget.y())    # 400  （窗口纵坐标）
    print("widget.width() = %d" % widget.width())   # 300（工作区宽度）
    print("widget.height() = %d" % widget.height()) # 240 （工作区高度）

    print("通过坐标系获取工作区的数据(计算边框):")
    print("widget.geometry().x() = %d" % widget.geometry().x()) # 501 （工作区横坐标）
    print("widget.geometry().y() = %d" % widget.geometry().y()) # 431  （工作区纵坐标）
    print("widget.geometry().width() = %d" % widget.geometry().width() )  # 300（工作区宽度）
    print("widget.geometry().height() = %d" % widget.geometry().height()) # 240 （工作区高度）

    print("获取窗口的坐标轴和含标头的宽高:")
    print("widget.frameGeometry().x() = %d" % widget.frameGeometry().x())  # 500 （窗口横坐标）
    print("widget.frameGeometry().y() = %d" % widget.frameGeometry().y())  # 400  （窗口纵坐标）
    print("widget.frameGeometry().width() = %d" % widget.frameGeometry().width() )  # 302（窗口宽度）
    print("widget.frameGeometry().height() = %d" % widget.frameGeometry().height()) # 272（窗口高度）

app = QApplication(sys.argv)

# 初始化主框架(即工作区)
widget = QWidget()

# 初始化并设置按钮
btn = QPushButton(widget)
btn.setText("按钮")
# 关联按钮单击事件和槽
btn.clicked.connect(onClick_Button)
# 设置按钮相对于工作区的位置
btn.move(30,30)

widget.resize(300,240)   # 设置工作区的尺寸

widget.move(500,400)    # 设置工作区相对屏幕坐标系的位置

widget.setWindowTitle('屏幕坐标系')

widget.show()

sys.exit(app.exec_())

