from calendar import c
import sys
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QProgressBar


from Sing import Ui_Form1




class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.ui = Ui_Form1()
        self.ui.setupUi(self)




