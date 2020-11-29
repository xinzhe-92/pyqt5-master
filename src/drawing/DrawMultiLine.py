'''
绘制不同类型的直线
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine,self).__init__()
        self.resize(300,300)
        self.setWindowTitle('设置Pen的样式')

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        # 颜色, 粗细, 风格
        pen = QPen(Qt.red,3,Qt.SolidLine)   # 实线
        painter.setPen(pen)
        # 开始X, 开始Y, 结束X, 结束Y
        painter.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashLine)   # 宽虚线
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotDotLine)     # 点划线
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)    # 窄虚线
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)

        # 自定义点划线
        pen.setStyle(Qt.CustomDashLine)
        # 自定义长度间距
        pen.setDashPattern([1,10,5,8])
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)

        size = self.size()

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()
    sys.exit(app.exec_())