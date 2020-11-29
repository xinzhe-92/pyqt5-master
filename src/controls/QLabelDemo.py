# Label控件基本用法案例
# QLabel通常用于普通文本展示和图片展示
'''
    注意:
        label控件想绑定槽, 则必须为文本内容, 且必须为<a>标签
        图片内容无法绑定槽
        文本内容非<a>标签无法绑定槽
'''
'''
QLabel控件常用设置函数:
    setAlignment()：设置文本的对齐方式
    setIndent()：设置文本缩进
    text()：获取文本内容
    setBuddy()：设置伙伴关系
    setText()：设置文本内容
    selectedText()：返回所选择的字符
    setWordWrap()：设置是否允许换行
'''

'''
QLabel常用的信号（事件）：
1.  当鼠标滑过QLabel控件时触发(鼠标滑过悬停事件)：linkHovered
2.  当鼠标单击QLabel控件时触发()：linkActivated

'''

import sys
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QLabel,QWidget
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget) :
    def __init__(self):
        super().__init__()
        self.initUI()

    # 常在init中绘制界面
    def initUI(self):
        # 初始化控件
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        label5 = QLabel(self)

        # label1设置
        # label1设置文本
        # 此处和使用css设置文本内容
        label1.setText("<font color=yellow style='color:Red;background: black;'>这是一个文本标签.</font>")
        # 设置该控件的背景调色板
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)  # 设置Label控件的背景色
        # 对于该label设置该调色板
        label1.setPalette(palette)
        # 设置该控件label居中对齐
        label1.setAlignment(Qt.AlignCenter)

        # 设置label2文本内容
        label2.setText("<a href='#'>欢迎使用Python  GUI程序</a>")
        label2.setAlignment(Qt.AlignLeft)   # 设置label2水平左对齐

        # 设置label3居中对齐
        label3.setAlignment(Qt.AlignCenter)
        # 设置label3悬停文字
        label3.setToolTip('这是一个图片标签')
        # 设置label3图片来源
        label3.setPixmap(QPixmap("./images/python.jpg"))

        # 如果设为True，用浏览器打开网页，如果设为False，调用槽函数
        # 默认为False
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注《Python从菜鸟到高手》</a>")
        # 设置label4水平右侧对齐
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')

        label5.setText("测试被<a>文本能否被绑定槽")

        # 初始化纵向框架, 并添加label
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        # label2信号关联槽
        label2.linkHovered.connect(self.linkHovered)
        # label4信号关联槽
        label4.linkActivated.connect(self.linkClicked)

        # label3测试
        label3.linkActivated.connect(self.linkClicked)
        # label5信号绑定槽
        label4.linkHovered.connect(self.linkHovered)

        # 封装Layout
        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')

    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    def linkClicked(self):
        print('当鼠标单击label4标签时，触发事件')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())