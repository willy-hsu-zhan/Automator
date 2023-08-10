from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QCheckBox, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout
import json
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 資料庫名稱相關元件
        self.label_database = QtWidgets.QLabel(self.centralwidget)
        self.label_database.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_database.setObjectName("label_database")

        # 新增 Task 相關元件
        self.label_task = QtWidgets.QLabel(self.centralwidget)
        self.label_task.setGeometry(QtCore.QRect(10, 38, 41, 16))
        self.label_task.setObjectName("label_task")
        self.textBrowser_task = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_task.setGeometry(QtCore.QRect(80, 36, 511, 31))
        self.textBrowser_task.setObjectName("textBrowser_task")

        # ComboBox相關元件
        self.comboBox_database = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_database.setGeometry(QtCore.QRect(103, 8, 51, 22))
        self.comboBox_database.setObjectName("comboBox_database")

        with open("config/db.json", "r") as file:
            data = json.load(file)
        # 先塞空值
        self.comboBox_database.addItem("")
        # 將 key 值填充到 ComboBox
        self.comboBox_database.addItems(data.keys())

        # 連線相關元件
        self.pushButton_connect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_connect.setGeometry(QtCore.QRect(160, 8, 75, 23))
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(241, 8, 75, 23))
        self.pushButton_reset.setObjectName("pushButton_reset")

        # 新增數據庫相關元件
        self.pushButton_add_database = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_database.setGeometry(QtCore.QRect(322, 8, 75, 23))
        self.pushButton_add_database.setObjectName("pushButton_add_database")

        # SQL預覽相關元件
        self.label_sql_preview = QtWidgets.QLabel(self.centralwidget)
        self.label_sql_preview.setGeometry(QtCore.QRect(10, 82, 71, 21))
        self.label_sql_preview.setObjectName("label_sql_preview")
        self.textBrowser_sql_preview = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_sql_preview.setGeometry(QtCore.QRect(80, 80, 511, 301))
        self.textBrowser_sql_preview.setObjectName("textBrowser_sql_preview")

        # 提示訊息相關元件
        self.label_message = QtWidgets.QLabel(self.centralwidget)
        self.label_message.setGeometry(QtCore.QRect(10, 400, 61, 16))
        self.label_message.setObjectName("label_message")
        self.textBrowser_message = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_message.setGeometry(QtCore.QRect(80, 398, 511, 31))
        self.textBrowser_message.setObjectName("textBrowser_message")

        # 確認執行和跳過這筆按鈕
        self.pushButton_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_confirm.setGeometry(QtCore.QRect(241, 438, 75, 23))
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.pushButton_skip = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_skip.setGeometry(QtCore.QRect(322, 438, 75, 23))
        self.pushButton_skip.setObjectName("pushButton_skip")

        # 設定相對位置
        self.label_database.move(10, 10)
        self.label_task.move(10, 38)
        self.textBrowser_task.move(80, 36)
        self.comboBox_database.move(103, 8)
        self.pushButton_connect.move(160, 8)
        self.pushButton_reset.move(241, 8)
        self.pushButton_add_database.move(322, 8)
        self.label_sql_preview.move(10, 82)
        self.textBrowser_sql_preview.move(80, 80)
        self.label_message.move(10, 400)
        self.textBrowser_message.move(80, 398)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_database.setText(_translate("MainWindow", "資料庫名稱:"))
        self.label_task.setText(_translate("MainWindow", "Task:"))
        self.pushButton_connect.setText(_translate("MainWindow", "連線"))
        self.pushButton_reset.setText(_translate("MainWindow", "重置名稱")) #預計改為編輯資料庫
        self.pushButton_add_database.setText(_translate("MainWindow", "新增數據庫"))
        self.label_sql_preview.setText(_translate("MainWindow", "SQL預覽:"))
        self.label_message.setText(_translate("MainWindow", "提示訊息:"))
        self.pushButton_confirm.setText(_translate("MainWindow", "確認執行"))
        self.pushButton_skip.setText(_translate("MainWindow", "跳過這筆"))

class AddDatabaseDialog(QDialog):
    def __init__(self):
        super(AddDatabaseDialog, self).__init__()
        self.setWindowTitle("新增數據庫")
        self.init_ui()

    def init_ui(self):
        # 創建所有視窗元件
        self.label_db_name = QLabel("連線名稱:")
        self.edit_db_name = QLineEdit()

        self.label_host = QLabel("主機:")
        self.edit_host = QLineEdit()

        self.label_port = QLabel("連接阜:")
        self.edit_port = QLineEdit()

        self.label_username = QLabel("用戶名稱:")
        self.edit_username = QLineEdit()

        self.label_password = QLabel("密碼:")
        self.edit_password = QLineEdit()

        self.checkbox_use_ssh = QCheckBox("使用SSH")

        self.label_ssh_host = QLabel("SSH主機:")
        self.edit_ssh_host = QLineEdit()

        self.label_ssh_port = QLabel("SSH連接阜:")
        self.edit_ssh_port = QLineEdit()

        self.label_auth_method = QLabel("驗證方法:")
        self.combo_auth_method = QComboBox()
        self.combo_auth_method.addItems(["密碼", "公鑰", "密碼和公鑰"])

        self.label_ssh_password = QLabel("SSH密碼:")
        self.edit_ssh_password = QLineEdit()

        self.label_private_key = QLabel("私鑰:")
        self.edit_private_key = QLineEdit()
        self.btn_browse_private_key = QPushButton("瀏覽")

        self.label_passphrase = QLabel("通行密碼:")
        self.edit_passphrase = QLineEdit()

        self.btn_confirm = QPushButton("確定")
        self.btn_cancel = QPushButton("取消")

        # 設定元件的佈局
        layout = QVBoxLayout()

        layout.addWidget(self.label_db_name)
        layout.addWidget(self.edit_db_name)

        layout.addWidget(self.label_host)
        layout.addWidget(self.edit_host)

        layout.addWidget(self.label_port)
        layout.addWidget(self.edit_port)

        layout.addWidget(self.label_username)
        layout.addWidget(self.edit_username)

        layout.addWidget(self.label_password)
        layout.addWidget(self.edit_password)

        layout.addWidget(self.checkbox_use_ssh)

        layout.addWidget(self.label_ssh_host)
        layout.addWidget(self.edit_ssh_host)

        layout.addWidget(self.label_ssh_port)
        layout.addWidget(self.edit_ssh_port)

        layout.addWidget(self.label_auth_method)
        layout.addWidget(self.combo_auth_method)

        layout.addWidget(self.label_ssh_password)
        layout.addWidget(self.edit_ssh_password)

        layout.addWidget(self.label_private_key)
        layout.addWidget(self.edit_private_key)
        layout.addWidget(self.btn_browse_private_key)

        layout.addWidget(self.label_passphrase)
        layout.addWidget(self.edit_passphrase)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_confirm)
        button_layout.addWidget(self.btn_cancel)

        layout.addLayout(button_layout)

        self.setLayout(layout) # init --------

        # 設定 "使用SSH" checkbox 的切換事件
        self.checkbox_use_ssh.toggled.connect(self.update_ssh_fields)
        # 設定 "確定" 按鈕的點擊事件
        self.btn_confirm.clicked.connect(self.on_confirm_clicked)
        # 設定 "取消" 按鈕的點擊事件
        self.btn_cancel.clicked.connect(self.on_cancel_clicked)

    def update_ssh_fields(self):
        checked = self.checkbox_use_ssh.isChecked()
        self.label_ssh_host.setEnabled(checked)
        self.edit_ssh_host.setEnabled(checked)
        self.label_ssh_port.setEnabled(checked)
        self.edit_ssh_port.setEnabled(checked)
        self.label_auth_method.setEnabled(checked)
        self.combo_auth_method.setEnabled(checked)
        self.label_ssh_password.setEnabled(checked)
        self.edit_ssh_password.setEnabled(checked)
        self.label_private_key.setEnabled(checked)
        self.edit_private_key.setEnabled(checked)
        self.btn_browse_private_key.setEnabled(checked)
        self.label_passphrase.setEnabled(checked)
        self.edit_passphrase.setEnabled(checked)

    def on_confirm_clicked(self):
        # 處理按下 "確定" 按鈕的邏輯
        # 在這裡取得使用者輸入的數據，並進行相應處理
        self.accept()  # 關閉對話框並回傳 QDialog.Accepted

    def on_cancel_clicked(self):
        # 處理按下 "取消" 按鈕的邏輯
        self.reject()  # 關閉對話框並回傳 QDialog.Rejected
