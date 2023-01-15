from calendar import c
import sys
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QProgressBar


from choose import Ui_Form 



class Root(QWidget):
    def __init__(self):
        super(Root, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)




if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = Root()
    window.show()

    sys.exit(app.exec())