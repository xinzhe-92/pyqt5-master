# QLineEdit控件介绍1
# QLineEdit控件与回显模式

'''

QLineEdit控件与回显模式

QLine基本功能：输入单行的文本

EchoMode（回显模式）
    即输入文本后, QLine内显示的模式
    4种回显模式
        1. Normal   正常模式, 输入即显示;
        2. NoEcho   不回显模式, 实际存在输入, 但不显示;
        3. Password 密码模式, 输入, 但显示为*号;
        4. PasswordEchoOnEdit   密码模式2, 输入则正常显示, LineEdit控件失去焦点之后使用*代替;

'''
from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget) :
    def __init__(self):
        super(QLineEditEchoMode,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        # 使用表单布局
        formLayout = QFormLayout()
        # 此处同样可以使用热键
        formLayout.addRow("&Normal",normalLineEdit)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("Password",passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit",passwordEchoOnEditLineEdit)

        # placeholdertext即LineEdit中的默认显示消息, 常用于内容提示
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        # 设置回显模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())
