# 代码设置QLabel与其他控件的伙伴关系
# 使用栅格布局添加控件
# 自己写了动态参数的自定义槽

'''
QLabel与伙伴控件
mainLayout.addWidget(控件对象,rowIndex,columnIndex,row,column)
'''

from PyQt5.QtWidgets import *
import sys

class QLabelBuddy(QDialog) :
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')

        nameLabel = QLabel('登录名(&N)',self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('密码(&P)',self)
        passwordLineEdit = QLineEdit(self)
        # 设置伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        btnOK.clicked.connect(self.buttonClicked)
        btnCancel.clicked.connect(self.buttonClicked)


        # 使用栅格布局
        mainLayout = QGridLayout(self)
        # 参数顺序(控件, 第几行(0起), 第几列(0起), 占用几行, 占用几列)
        mainLayout.addWidget(nameLabel,0,0)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)

        mainLayout.addWidget(passwordLabel,1,0)
        mainLayout.addWidget(passwordLineEdit,1,1,1,2)

        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)

    def buttonClicked(self):
        sender = self.sender()
        print(sender.text() + ' 按钮被按下')
        if sender.text() == '&Cancel':
            app = QApplication.instance()
            # 退出应用程序
            app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())
