'''
滑块控件（QSlider）
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑块控件演示, 更改Label字号')
        self.resize(300,700)

        layout = QVBoxLayout()
        self.label = QLabel('你好 PyQt5')
        self.label.setAlignment(Qt.AlignCenter)     # label居中显示

        layout.addWidget(self.label)

        # 初始化水平滑块
        self.slider = QSlider(Qt.Horizontal)

        # 设置最小值
        self.slider.setMinimum(12)
        # 设置最大值
        self.slider.setMaximum(48)
        # 步长
        self.slider.setSingleStep(3)
        # 设置当前值
        self.slider.setValue(18)
        # 设置刻度的位置，刻度在下方
        self.slider.setTickPosition(QSlider.TicksBelow)
        # 设置刻度的间隔
        self.slider.setTickInterval(6)

        layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.valueChange)

        # 初始化垂直滑块
        self.slider1 = QSlider(Qt.Vertical)
        layout.addWidget(self.slider1)
        # 设置最小值
        self.slider1.setMinimum(10)
        # 设置最大值
        self.slider1.setMaximum(60)
        # 步长
        self.slider1.setSingleStep(5)
        # 设置当前值
        self.slider1.setValue(30)

        # 设置刻度的位置，刻度在下方
        # QSlider.TicksBothSides：在滑块的两侧绘制刻度线
        # QSlider.TicksAbove:在滑块的（水平）上方绘制刻度线
        # QSlider.TicksBelow:在滑块的（水平）下方绘制刻度线
        # QSlider.TicksLeft:在滑块的（垂直）左侧绘制刻度线
        # QSlider.TicksRight,在滑块的（垂直）右侧绘制刻度线
        self.slider1.setTickPosition(QSlider.TicksBothSides)
        # 设置刻度的间隔
        self.slider1.setTickInterval(2)
        self.slider1.valueChanged.connect(self.valueChange)
        self.setLayout(layout)


    def valueChange(self):
        print('当前值：%s' % self.sender().value())
        size = self.sender().value()
        self.label.setFont(QFont('Arial',size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())