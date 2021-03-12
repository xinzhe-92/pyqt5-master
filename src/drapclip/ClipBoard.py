'''
使用系统剪贴板
QCipboard类提供了对系统剪切板的访问

'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class ClipBoard(QDialog):
    def __init__(self):
        super(ClipBoard,self).__init__()

        # 初始化按钮
        textCopyButton = QPushButton('复制文本')
        textPasteButton = QPushButton('粘贴文本')
        htmlCopyButton = QPushButton('复制HTML')
        htmlPasteButton = QPushButton('粘贴HTML')
        imageCopyButton = QPushButton('复制图像')
        imagePasteButton = QPushButton('粘贴图像')

        # 初始化展示区
        self.textLabel = QLabel('默认文本')
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap('./images/book1.png'))

        # 栅格布局
        layout = QGridLayout()
        layout.addWidget(textCopyButton,0,0)
        layout.addWidget(imageCopyButton,0,1)
        layout.addWidget(htmlCopyButton,0,2)
        layout.addWidget(textPasteButton,1,0)
        layout.addWidget(imagePasteButton,1,1)
        layout.addWidget(htmlPasteButton,1,2)

        layout.addWidget(self.textLabel,2,0,1,3)
        layout.addWidget(self.imageLabel,3,0,1,3)

        self.setLayout(layout)

        # 绑定信号和槽
        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

        self.setWindowTitle('剪贴板演示')

    def copyText(self):
        clipboard = QApplication.clipboard()
        # 将文本复制到系统剪切板
        clipboard.setText('hello world')
    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('./images/表情包1518423455627.jpg'))
    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())

    # 操作html时使用mime数据封装
    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml('<b>Bold and <font color=red>Red</font></b><br/><a href = "www.baidu.com">百度</a>')
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)
    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ClipBoard()
    main.show()
    sys.exit(app.exec_())