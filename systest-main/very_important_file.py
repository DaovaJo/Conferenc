import sys
import time
from tokenize import Double
import os
import openpyxl 
import re
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QProgressBar


class CreatNag:
    def __init__(self):
        # self.key_control = False
        self.a = 1
        self.f = 1
        self.teacher = "Гамидов Лазер Шафтаридинович"
        self.d = 11
        self.forEvent = ['\Основная выписка на ', '\Изменения в выписке на ']
        self.c = 0
        self.cc = list()
        number = None
        

    def getter(self):
        return self.key_control

    
    def close(self):
        quit()
        
    #Данная функция занимается переносом знчений в нашу форму для нагрузки
    def replacing(self, l0, Data, Time, Class, Subjects, Group, Event, Teach, Com, Coment, Output, Departmant, num):
        cl_A = 'A' + str(self.d)
        cl_B = 'B' + str(self.d)
        cl_C = 'C' + str(self.d)
        cl_D = 'D' + str(self.d)
        cl_P = 'P' + str(self.d)
        cl_Q = 'Q' + str(self.d)
        cl_R = 'R' + str(self.d)
        cl_J = 'J' + str(self.d)
        cl_N = 'N' + str(self.d)

        book = openpyxl.open('try.xlsx')
        sheet = book.active

        sheet[cl_D] = Data
        sheet[cl_P] = Subjects
        sheet[cl_Q] = Group
        sheet[cl_R] = num
        sheet[cl_J] = Event
        sheet[cl_N] = Output


        book.save('try.xlsx')
        book.close()
        self.d = self.d + 1
   

    def search_group(self, Group):
        global num
        global dep
        global training
        global number
        bk = openpyxl.open('+Учебные группы_кол-во студентов.xlsx', read_only = True)
        sheet = bk.active
        cells = sheet['A15':'F904']
        Groups =  str(Group)
        Groups = re.split(";", Group)
        Groups = [x.strip(" ") for x in Groups]
        for _ in Groups:
            
            for group, department, speciality, form_of_training, tecnologi_of_training, count in cells:
                if group.value == _:
                    """Я стащила значение и запихала его в список, после чего сконвертировала с одним разделителем а потом в дикте убрала пробелы перед элементами"""
                    self.number = count.value
                    self.cc.append(str(self.number))       
                    for __ in self.cc:                 
                        self.c =int(__) + self.c
        num = self.c


    def run(self):
        try:
            folder = QFileDialog.getExistingDirectory(self)
            f = os.listdir(folder) #получаем нужную папку
            print(folder, f)
            counter = 1

            for i in f:
                global c
                global lst
                
                

                time.sleep(0.1)
                self.ui.progressBar.setValue(round((f.index(i)+100/len(f)-f.index(i)) * counter))
                print(len(f))
                print(round((f.index(i)+100/len(f)-f.index(i)) * counter))
                
                counter = counter + 1
                file = folder + "/" + i
                file_name = os.path.abspath(file) #поправляем путь, делаем его адеватным
                print(file_name)

                book = openpyxl.open(file_name, read_only = True)
                sheet = book.active
                    
                cells = sheet['D7':'O500']
                for Data, Time, Class, Subjects, none, Group, Event, Teach, Com, Coment, Output, Departmant in cells:
                    cc = list()
                    print(Data)
                        
                    if Teach.value == self.teacher and Departmant.value == "Кафедра информационных систем": #and Departmant.value == 'Кафедра информационных систем':
                        Data = Data.value
                                
                        Time = Time.value
                        Class = Class.value
                        Subjects = Subjects.value
                        Group = Group.value
                        Event = Event.value
                        Teach = Teach.value
                        Com = Com.value
                        Coment = Coment.value
                        Output = Output.value
                        Departmant = Departmant.value
                                # print(Group)
                        self.search_group(Group)
                                # print(num)
                        print(Data, Time, Class, Subjects, Group, Event, Teach, Com, Coment, Output, Departmant)
                        self.replacing(10, Data, Time, Class, Subjects, Group, Event, Teach, Com, Coment, Output, Departmant, num)
                    else:
                        continue
                    
            self.key_control = True
            book.close()
            

            # if self.key_control == True:
                # app.exec()
                # self.close()

        except FileNotFoundError:
            self.key_control = False
        except openpyxl.utils.exceptions.InvalidFileException:
            msg_Error = QMessageBox()
            msg_Error.setText("""ВНИМАНИЕ!!!
Убедитесь в том что в папке только файлы формата: .xlsx,.xlsm,.xltx,.xltm
            """
            ) 
            msg_Error.exec()
        except PermissionError:
            msg_Premm = QMessageBox()
            msg_Premm.setText("Данный файл уже используется дргуим приложением")
            msg_Premm.exec()
        
        # Progers.close(self)
    
    
