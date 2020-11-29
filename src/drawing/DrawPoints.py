'''
用像素点绘制正弦曲线
    -2PI  2PI

    # 绘制一个像素点, X, Y为坐标参数
    drawPoint(x,y)
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class DrawPoints(QWidget):
    def __init__(self):
        super(DrawPoints,self).__init__()
        self.resize(300,300)
        self.setWindowTitle('在窗口上用像素点绘制2个周期的正弦曲线')

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        size = self.size()

        for i in range(1000):
            # size.width()/height() / 2.0 的意义在于将坐标轴原点从左上角移动至中心
            x = 100 * (-1 + 2.0 * i/1000) + size.width()/2.0
            y = -50 * math.sin((x - size.width()/2.0) * math.pi/50) + size.height()/2.0
            painter.drawPoint(x,y)

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawPoints()
    main.show()
    sys.exit(app.exec_())