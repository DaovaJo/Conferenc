import os
import re
import sys
import time
from calendar import c
from tkinter import image_types

import openpyxl
from openpyxl import workbook
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox, QProgressBar, QVBoxLayout, QWidget)

from fnc.func import Functional
from fnc.change import Window
from UIdesing_py.finaly import Ui_Form


# from UIdesing_py.finaly import Ui_Form
# from UIdesing_py.progress import Progers

# app = QApplication(sys.argv)

class Root(QWidget):
    def __init__(self):
        super(Root, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.funcsh = Functional()
        
        self.ui.check_nag.clicked.connect(self.funcsh.open_correct_file)
        self.ui.change_teach.clicked.connect(self.funcsh.change_teacher)
        self.ui.creat_nag.clicked.connect(self.funcsh.progressbar)
        

        self.show()
    
    def change_teacher(self):
        pass
        

        
        




if __name__ == "__main__":

    app = QApplication(sys.argv)
    root = Root()

    sys.exit(app.exec())