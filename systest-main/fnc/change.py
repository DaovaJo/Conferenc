import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QProgressBar, QInputDialog, QPushButton, QLineEdit, QGridLayout, QLabel
from langdetect import detect

from UIdesing_py.editTeach import EditTeacher

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = EditTeacher()
        self.ui.setupUi(self)
        self.teacher = list()

        self.ui.pushButton.clicked.connect(self.edit_teach) 
        self.show() 
    
    def edit_teach(self):
        value = self.ui.lineEdit.text()
        val2 = self.ui.lineEdit_2.text()
        # print(value)
        # создаю список из введенных слов для проверки на наличии болие 2 слов а именно Имени и Фамилии
        chek_value = value.split(" ")
        # print(chek_value)
        # Проверка на количество слов ввода (P.S. Обязательно больше 1 слова, так как либо будет ФИО либо ФИ но никак не И, О, Ф и наоборот)
        if len(chek_value) < 2:
            # Выводим окно сообщения
            msg1 = QMessageBox()
            msg1.setText("""Введите полностью ФИО""")
            msg1.exec()
        # Проверка на язык ввода
        else:
            self.teacher.append(value)
            self.teacher.append(val2)
            print(self.teacher) 
        
   
            
        


# if __name__ == '__main__':
#     app = QApplication([])

#     mw = Window()
#     mw.show()

#     app.exec()

