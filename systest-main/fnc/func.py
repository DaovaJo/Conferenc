# ФУНКЦИОНАЛ ПО
from distutils.util import execute
import math
from msilib.schema import File
import sys
import time
from tkinter import Widget
from tkinter.messagebox import IGNORE
from tokenize import Double
import os
import openpyxl 
import re
import os
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QProgressBar, QPushButton
from PySide6 import QtCore, QtWidgets, QtGui
from test import Progers
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QProgressBar, QGridLayout, QPushButton, QLineEdit, QLabel, QFileDialog
from .change import Window
from langdetect import detect

# app = QApplication([])

class Functional(QWidget):
    def __init__(self):
        super(Functional, self).__init__()
        self.key_control = False
        self.a = 1
        self.f = 1
        self.teacher = "Королькова Ирина Анатольевна"
        self.d = 11
        self.c = 0
        self.cc = list()
                   
    def open_correct_file(self):
        # self.ui2.settings.setEnabled(True)
        self.file = os.startfile("nagFile\shablon\shtat.xlsx") #офигенная вещь , запускает файл
    
    def change_teacher(self):
        self.ui = Window()

    def progressbar(self):
        self.ui = Progers()
        self.ui.run()

                        
        
    
    
        
        




# if __name__ == '__main__':
    
#     app = QApplication([])

#     mw = Functional()
#     mw.show()

#     app.exec()
    
    
   