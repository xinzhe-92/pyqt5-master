'''
日历控件
QCalendarWidget
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUI()
    def initUI(self):
        # 初始化日历控件
        self.cal = QCalendarWidget(self)
        # 设置可显示日期最大/最小
        self.cal.setMinimumDate(QDate(1988,1,1))
        self.cal.setMaximumDate(QDate(2088,1,1))

        self.cal.setGridVisible(True)   # 设置日历内的网格效果
        self.cal.move(20,20)    # 移动日历位置

        # 绑定信号和槽
        self.cal.clicked.connect(self.showDate)

        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString("yyyy-MM-dd dddd"))
        self.label.move(20,300) # label绝对布局

        self.resize(400,350)
        self.setWindowTitle("日历演示")

    # 获取日历文本
    def showDate(self,date):
        #self.label.setText((date.toString("yyyy-MM-dd dddd")))
        self.label.setText((self.cal.selectedDate().toString("yyyy-MM-dd dddd")))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyCalendar()
    main.show()
    sys.exit(app.exec_())
