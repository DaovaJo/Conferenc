from distutils.util import execute
import math
import sys
import time
from tokenize import Double
import os
import openpyxl 
import re
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QProgressBar, QPushButton
from PySide6 import QtCore, QtWidgets, QtGui
from UIdesing_py.progress import Ui_Dialog


class Progers(QtWidgets.QMainWindow):
    def __init__(self):
        super(Progers, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

        self.key_control = False
        self.a = 1
        self.f = 1
        self.teacher = input("Введите препа: ")
        self.d = 11
        self.c = 0
        self.cc = list()
        number = None

        # self.ui.pushButton.clicked.connect(self.run)
    

        #Данная функция занимается переносом знчений в нашу форму для нагрузки
    def replacing(self, l0,  Data, Time, Class, Subjects, Sub2, Group, More, Event, Teach, Dep, Id):
        
        D = 'D' + str(self.d); P = 'P' + str(self.d); Q = 'Q' + str(self.d); R = 'R' + str(self.d); J = 'J' + str(self.d); N = 'N' + str(self.d)
        S = 'S' + str(self.d); T = 'T' + str(self.d); U = 'U' + str(self.d); AJ = 'AJ' + str(self.d); AI = 'AI' + str(self.d); E = 'E' + str(self.d); F = 'F' + str(self.d); G = 'G' + str(self.d)

# отделяем дату от основного текста
        data = Data.split(" ")
        print(data[8])

# вычисляем нагрузку
        zaman = Time.split("-")
        start_time = str(zaman[0]).replace(":", ".")
        finish_time = str(zaman[1]).replace(":", ".")
        zam = float(finish_time) - float(start_time)
        print(math.ceil(zam)) #math.ceil это округление числа в большую сторону до целого

        

# Проверка объедененных ячеек, а то сириус качает криво
        if Sub2 == None:
            subject = Subjects
        else:
            subject = Sub2

        
        book = openpyxl.open('nagFile\shablon\shtat.xlsx')
        sheet = book.active

# Данные из выписки 
   
        sheet[G] = Id
        sheet[N] = math.ceil(zam)
        sheet[E] = Time
        sheet[J] = Event
        sheet[F] = Teach
        sheet[D] = str(data[8])
        sheet[P] = subject
        sheet[Q] = Group
        sheet[R] = More   
   
# Данные для формул 
    
    

# Формулы для счета нагрузки
        # sheet[S] = '=ЕСЛИ({sheet[J]}="Лекции";{sheet[N]};"")'
        # sheet[T] = ('=ЕСЛИ(ИЛИ({J}="СПЗ";;{J}="Семинары ИПЗ";);{N};"")')
        # sheet[U] = '=ЕСЛИ({J}="Консультации";{N};"")'
        # sheet[AJ] = '=СУММ({S}:{AI})'

        # sheet['S'] = "ЕСЛИ(S='Лекции';S;'')"



        book.save(f"nagFile\shablon\shtat.xlsx")
        book.close()
        self.d = self.d + 1

    def cont(self):
        if self.cnt > 100:
            exit()

    def open_dir(self):
        self.folder = QFileDialog.getExistingDirectory(self)
        self.f = os.listdir(self.folder) #получаем нужную папку
        print(self.folder, self.f)
        self.counter = 1
        
    
    def exit_loader(self):
        self.close()
        
        

    def run(self):
            # try:
                self.open_dir()
                for i in self.f:
                    time.sleep(0.1)
                    self.ui.progressBar.setValue(round((self.f.index(i)+100/len(self.f)-self.f.index(i)) * self.counter))
                            
                    self.counter = self.counter + 1
                    self.cnt = (self.f.index(i)+100/len(self.f)-self.f.index(i)) * self.counter
                    file = self.folder + "/" + i
                    file_name = os.path.abspath(file) #поправляем путь, делаем его адеватным

                    book = openpyxl.open(file_name, read_only = True)
                    sheet = book.active
                                
                    self.cells = sheet['A11':'M500']
                    # print("عارهاثصخر")
                    for Data, n, nl, Time, Class, Subjects, n2, Group, More, Event, Teach, Dep, Id in self.cells:
                        cc = list()
                        # print("freuigiohrew")
                        # print(Teach.value)
                        # print("///", self.teacher)
                                
                        if Teach.value == self.teacher: #and Departmant.value == 'Кафедра информационных систем':
                            # print("رلائ")
                            Sub2 = n2.value
                            Data = Data.value  
                            Time = Time.value
                            Class = Class.value
                            Subjects = Subjects.value
                            Group = Group.value
                            More = More.value
                            Event = Event.value
                            Teach = Teach.value
                            Dep = Dep.value
                            Id = Id.value
                            print(Data, Time, Class, Subjects, Sub2, Group, More, Event, Teach, Dep, Id)
                            self.replacing(10, Data, Time, Class, Subjects, Sub2, Group, More, Event, Teach, Dep, Id)
                    else:
                        continue
                self.exit_loader()    
            
            # except:
                # print('упс')


# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     demo = Progers()
#     demo.show()

    


#     sys.exit(app.exec())
