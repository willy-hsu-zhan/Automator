from PyQt5 import QtCore, QtWidgets

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
        self.comboBox_database.addItem("")
        self.comboBox_database.addItem("")

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
        self.pushButton_reset.setText(_translate("MainWindow", "重置名稱"))
        self.comboBox_database.setItemText(0, _translate("MainWindow", "VAE"))
        self.comboBox_database.setItemText(1, _translate("MainWindow", "VAS"))
        self.pushButton_add_database.setText(_translate("MainWindow", "新增數據庫"))
        self.label_sql_preview.setText(_translate("MainWindow", "SQL預覽:"))
        self.label_message.setText(_translate("MainWindow", "提示訊息:"))
        self.pushButton_confirm.setText(_translate("MainWindow", "確認執行"))
        self.pushButton_skip.setText(_translate("MainWindow", "跳過這筆"))

