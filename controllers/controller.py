class Controller:
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

    def on_button_connect_clicked(self):
        # 處理連線按鈕被點擊時的邏輯
        print("連線按鈕被點擊了！")

    def on_button_reset_clicked(self):
        # 處理重置名稱按鈕被點擊時的邏輯
        print("重置名稱按鈕被點擊了！")

    def on_button_add_database_clicked(self):
        # 處理新增數據庫按鈕被點擊時的邏輯
        print("新增數據庫按鈕被點擊了！")

    def on_button_confirm_clicked(self):
        # 處理確認執行按鈕被點擊時的邏輯
        print("確認執行按鈕被點擊了！")

    def on_button_skip_clicked(self):
        # 處理跳過這筆按鈕被點擊時的邏輯
        print("跳過這筆按鈕被點擊了！")

    def on_combobox_database_changed(self, index):
        # 處理 ComboBox 資料庫選擇改變時的邏輯
        selected_database = self.main_window.comboBox_database.itemText(index)
        print("選擇的資料庫是:", selected_database)
