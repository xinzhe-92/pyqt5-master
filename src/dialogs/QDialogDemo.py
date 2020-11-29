'''
    QDialog
'''
'''
对话框：QDialog(基类)
    在QDialog的基础上扩展了5中对话框:
        QMessageBox     消息对话框
        QColorDialog    颜色对话框
        QFileDialog     文件对话框
        QFontDialog     字体对话框
        QInputDialog    输入对话框

QMainWindow
QWidget
QDialog
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        # 主窗口设置
        self.setWindowTitle('QDialog案例')
        self.resize(300,200)

        # 按钮设置
        self.button = QPushButton(self)
        self.button.setText('弹出对话框')    # 设置按钮文字
        self.button.move(50,50)     # 设置按钮位置
        # 绑定事件与槽
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        vbox = QVBoxLayout()  # 纵向布局
        hbox = QHBoxLayout()  # 横向布局

        panel = QLabel()
        panel.setText("确定保存信息？")

        # 设置Dialog
        self.dialog = QDialog()
        self.dialog.resize(100, 100)

        # 设置两个按钮
        self.okBtn = QPushButton("确定")
        self.cancelBtn = QPushButton("取消")

        # 绑定事件
        self.okBtn.clicked.connect(self.ok)
        self.cancelBtn.clicked.connect(self.cancel)

        # 设置dialog标题
        self.dialog.setWindowTitle("提示信息！")

        #使用layout布局设置，因此move效果失效
        # okBtn.move(50,50)

        # 确定与取消按钮横向布局
        hbox.addWidget(self.okBtn)
        hbox.addWidget(self.cancelBtn)

        # 消息label与按钮组合纵向布局
        vbox.addWidget(panel)
        vbox.addLayout(hbox)

        self.dialog.setLayout(vbox)
        self.dialog.setWindowModality(Qt.ApplicationModal)  # 该模式下，只有该dialog关闭，才可以关闭父界面

        self.dialog.exec_()

    # 槽函数如下：
    def ok(self):
        print("确定保存！")
        self.dialog.close()

    def cancel(self):
        print("取消保存！")
        self.dialog.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())

