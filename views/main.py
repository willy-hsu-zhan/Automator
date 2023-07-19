from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 資料庫名稱相關元件
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setObjectName("label")

        # 新增 Task 相關元件
        self.label_task = QtWidgets.QLabel(self.centralwidget)
        self.label_task.setGeometry(QtCore.QRect(10, 38, 41, 16))
        self.label_task.setObjectName("label_task")
        self.textBrowser_task = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_task.setGeometry(QtCore.QRect(80, 36, 511, 31))
        self.textBrowser_task.setObjectName("textBrowser_task")

        # ComboBox相關元件
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(103, 8, 51, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        # 連線相關元件
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 8, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(241, 8, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        # 新增數據庫相關元件
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(322, 8, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        # SQL預覽相關元件
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 82, 71, 21))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 80, 511, 301))
        self.textBrowser.setObjectName("textBrowser")

        # 提示訊息相關元件
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 400, 61, 16))
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(80, 398, 511, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        # 確認執行和跳過這筆按鈕
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(241, 438, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(322, 438, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")

        # 設定相對位置
        self.label.move(10, 10)
        self.label_task.move(10, 38)
        self.textBrowser_task.move(80, 36)
        self.comboBox.move(103, 8)
        self.pushButton.move(160, 8)
        self.pushButton_2.move(241, 8)
        self.pushButton_3.move(322, 8)
        self.label_2.move(10, 82)
        self.textBrowser.move(80, 80)
        self.label_3.move(10, 400)
        self.textBrowser_2.move(80, 398)

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
        self.label.setText(_translate("MainWindow", "資料庫名稱:"))
        self.label_task.setText(_translate("MainWindow", "Task:"))
        self.pushButton.setText(_translate("MainWindow", "連線"))
        self.pushButton_2.setText(_translate("MainWindow", "重置名稱"))
        self.comboBox.setItemText(0, _translate("MainWindow", "VAE"))
        self.comboBox.setItemText(1, _translate("MainWindow", "VAS"))
        self.pushButton_3.setText(_translate("MainWindow", "新增數據庫"))
        self.label_2.setText(_translate("MainWindow", "SQL預覽:"))
        self.label_3.setText(_translate("MainWindow", "提示訊息:"))
        self.pushButton_4.setText(_translate("MainWindow", "確認執行"))
        self.pushButton_5.setText(_translate("MainWindow", "跳過這筆"))
