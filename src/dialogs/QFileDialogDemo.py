'''
文件对话框：QFileDialog
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文件对话框")

        layout = QVBoxLayout()

        self.button1 = QPushButton('加载图片')
        self.button1.clicked.connect(self.loadImage)
        layout.addWidget(self.button1)

        # 图片文件使用Label控件展示
        self.imageLabel = QLabel()
        layout.addWidget(self.imageLabel)

        self.button2 = QPushButton('加载文本文件')
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)

        # 多行文本使用QTestEdit控件展示
        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)

    def loadImage(self):
        # 参数: self, 对话框标题, 默认路径, 过滤文件
        # fname 为文件绝对路径
        # _ 基本无用, 为文件筛选器内容
        fname, _ = QFileDialog.getOpenFileName(self, '打开文件' ,'.' ,'Image File(*.jpg *.png)')
        print(fname)
        print(_)
        self.imageLabel.setPixmap(QPixmap(fname))

    def loadText(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            f = open(filenames[0],encoding='utf-8',mode='r')
            with f: # 使用with语句, 对于已打开的文件进行关闭
                data = f.read()
                self.contents.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())