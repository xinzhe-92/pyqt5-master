'''
绘图API：
    1. 文本
    2. 各种图形（直线，点，椭圆，弧，扇形，多边形等）
    3. 图像

    QPainter
    # 初始化实例
    painter = QPainter()
    # 初始化画板, 绘制开始
    painter.begin()
    # 绘制文本
    painter.drawText(...)
    # 绘制结束
    painter.end()

    注意:
        必须在paintEvent事件方法中绘制各种元素
        在创建窗口, 窗口尺寸变化后自动调用paintEvent事件
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt

class DrawText(QWidget):
    def __init__(self):
        super(DrawText,self).__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(300,200)
        self.text = "Python从菜鸟到高手"

    # 使用标准paintEvent槽
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        # 设置画笔的颜色
        painter.setPen(QColor(150,43,5))
        # 设置字体
        painter.setFont(QFont('SimSun',25))
        # 绘制文字
        painter.drawText(event.rect(),Qt.AlignCenter,self.text)

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawText()
    main.show()
    sys.exit(app.exec_())
