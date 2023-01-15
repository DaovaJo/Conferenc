from calendar import c
import sys
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QProgressBar


from account import Ui_Form
from SignForm import Form


class Account(QWidget):
    def __init__(self, parent = None):
        super(Account, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.form)

    def form(self):
        self.close()
        self.form = Form()
        self.form.show()



def main():
    app = QApplication(sys.argv)
    window = Account()
    window.show()

    sys.exit(app.exec())








if __name__ == "__main__":
    main()





 