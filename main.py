import sys
from PyQt5 import QtWidgets
from views.view import Ui_MainWindow
from controllers.controller import Controller

class MainView(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = Controller(self.ui)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_view = MainView()
    main_view.show()
    sys.exit(app.exec_())
