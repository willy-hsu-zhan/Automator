from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QComboBox, QFileDialog
from PyQt5 import QtCore
from views.view import AddDatabaseDialog
import json
import mysql.connector

class Controller:
    hostname = ""
    port = ""
    database = ""
    user = ""
    password = ""

    errormsg = ""

    def __init__(self, main_window):
        self.main_window = main_window
        self.setup_ui_connections()

    def setup_ui_connections(self):
        self.main_window.pushButton_connect.clicked.connect(self.on_button_connect_clicked)
        self.main_window.pushButton_reset.clicked.connect(self.on_button_reset_clicked)
        self.main_window.pushButton_add_database.clicked.connect(self.on_button_add_database_clicked)
        self.main_window.pushButton_confirm.clicked.connect(self.on_button_confirm_clicked)
        self.main_window.pushButton_skip.clicked.connect(self.on_button_skip_clicked)
        self.main_window.comboBox_database.currentIndexChanged.connect(self.on_combobox_database_changed)

        self.main_window.pushButton_add_database.clicked.connect(self.on_button_add_database_clicked)
        # self.main_window.checkbox_use_ssh.stateChanged.connect(self.on_use_ssh_checkbox_changed) #點擊按鈕後再顯示出來

    def on_button_connect_clicked(self):
        # 處理連線按鈕被點擊時的邏輯
        print("連線按鈕被點擊了！")
        print(self.create_connection())
        if self.hostname is not None and self.create_connection():
            self.main_window.textBrowser_message.setText("連線成功！")
        else:
            print("ERROR" + "你未選擇資料庫或連線失敗")
            self.main_window.textBrowser_message.setText("連線失敗！")

    def on_button_reset_clicked(self):
        # 處理重置名稱按鈕被點擊時的邏輯
        print("重置名稱按鈕被點擊了！")

    def on_button_add_database_clicked(self):
        # 處理新增數據庫按鈕被點擊時的邏輯
        print("新增數據庫按鈕被點擊了！")
        dialog = AddDatabaseDialog()
        dialog.update_ssh_fields() # 預設設為未啟用
        dialog.exec_()

    def on_button_confirm_clicked(self):
        # 處理確認執行按鈕被點擊時的邏輯
        print("確認執行按鈕被點擊了！")

    def on_button_skip_clicked(self):
        # 處理跳過這筆按鈕被點擊時的邏輯
        print("跳過這筆按鈕被點擊了！")

    def on_combobox_database_changed(self, index):
        # 處理 ComboBox 資料庫選擇改變時的邏輯
        selected_db_text = self.main_window.comboBox_database.currentText()
        print(f"Selected item: {selected_db_text}")

        with open("config/db.json", "r") as file:
            data = json.load(file)
        if data[selected_db_text] is not None:
            self.hostname = data[selected_db_text]["hostname"]
            self.port = data[selected_db_text]["port"]
            self.user = data[selected_db_text]["user"]
            self.password = data[selected_db_text]["password"]
            self.database = data[selected_db_text]["database"]
        # else:
        #     print('selected DATABASE ERROR')  連線action再來檔空值

    def set_ssh_widgets_enabled(self, enabled):
        self.label_ssh_host.setEnabled(enabled)
        self.edit_ssh_host.setEnabled(enabled)
        self.label_ssh_port.setEnabled(enabled)
        self.edit_ssh_port.setEnabled(enabled)
        self.label_auth_method.setEnabled(enabled)
        self.combo_auth_method.setEnabled(enabled)
        self.label_ssh_password.setEnabled(enabled)
        self.edit_ssh_password.setEnabled(enabled)
        self.label_private_key.setEnabled(enabled)
        self.edit_private_key.setEnabled(enabled)
        self.btn_browse_private_key.setEnabled(enabled)
        self.label_passphrase.setEnabled(enabled)
        self.edit_passphrase.setEnabled(enabled)

    def on_use_ssh_checkbox_changed(self, state):
        enabled = state == QtCore.Qt.Checked
        self.set_ssh_widgets_enabled(enabled)


    ## database 待優化

    # 建立数据库连接
    def create_connection(self):
        hostname = ""
        port = ""
        database = ""
        username = ""
        password = ""
        print(self.hostname)
        print(self.port)
        print(self.database)
        print(self.user)
        print(self.password)
        # try:
        #     print(11112323132)
        #     connection = mysql.connector.connect(
        #         host='localhost',      # 数据库主机地址
        #         user='root',  # 数据库用户名
        #         password='root',  # 数据库密码
        #         database='versiontool'  # 要连接的数据库名
        #     )
        #     print(1132)
        #     if connection.is_connected():
        #         print("成功连接到MySQL数据库")
        #         return connection
        # except mysql.connector.Error as e:
        #     print(f"连接失败：{e}")
        #     return None
        try:
            connection = mysql.connector.connect(
                host=self.hostname,      # 数据库主机地址
                port=self.port,
                user=self.user,  # 数据库用户名
                password=self.password,  # 数据库密码
                database=self.database  # 要连接的数据库名
            )
            if connection.is_connected():
                print("成功连接到MySQL数据库")
                return connection
        except mysql.connector.Error as e:
            print(f"连接失败：{e}")
            return None

    # 执行查询操作
    def execute_query(self, connection, query):
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            print(f"执行查询操作失败：{e}")
            return None

    # 关闭数据库连接
    def close_connection(self, connection):
        if connection:
            connection.close()
            print("数据库连接已关闭")

    def closeEvent(self, event): # 關閉資料庫事件
        # 在窗口关闭时调用
        self.close_connection()  # 在窗口关闭时执行 close_connection
        event.accept()

