'''
用画刷填充图形区域
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class FillRect(QWidget):
    def __init__(self):
        super(FillRect,self).__init__()
        self.resize(500,500)
        self.setWindowTitle('用画刷填充区域')
        self.show()

    def paintEvent(self,e):
        qp = QPainter()
        qp.begin(self)
        self.drawBrush(qp)
        qp.end()

    def drawBrush(self, qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10,15,90,60)

        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130,15,90,60)

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250,15,90,60)

        brush = QBrush(Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(370, 15, 90, 60)

        brush = QBrush(Qt.Dense4Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush = QBrush(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush = QBrush(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush = QBrush(Qt.Dense7Pattern)
        qp.setBrush(brush)
        qp.drawRect(370, 105, 90, 60)

        brush = QBrush(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush = QBrush(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)

        brush = QBrush(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(370, 195, 90, 60)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FillRect()
    main.show()
    sys.exit(app.exec_())