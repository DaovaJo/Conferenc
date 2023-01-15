
from abc import abstractproperty
from openpyxl import Workbook
import openpyxl
import re

import xlwings as xw
import re


from openpyxl.worksheet import worksheet # для регулярных выражений

a = 1

f = 1
teacher = "Беляев Павел Вячеславович"
d = 11 + 3

forEvent = ['\Основная выписка на ', '\Изменения в выписке на ']
# forMounth = input('Месяц: ')

# Данная функция занимается переносом знчений в нашу форму для нагрузки


def replacing(l0, Data, Time, Class, Subjects, Group, Event, Teach, Com, Coment, Output, Departmant, num):
    global d
    cl_A = 'A' + str(d)
    cl_B = 'B' + str(d)
    cl_C = 'C' + str(d)
    cl_D = 'D' + str(d)
    cl_P = 'P' + str(d)
    cl_Q = 'Q' + str(d)
    cl_R = 'R' + str(d)
    cl_J = 'J' + str(d)
    cl_N = 'N' + str(d)

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
    d = d + 1
c = 0
cc = list()
number = None



def search_group(Group, cc, c):
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
                number = count.value
                cc.append(str(number))       
                for __ in cc:                 
                    c =int(__) + c
    num = c



def search(f):
    global c
    global lst
    for i in forEvent:   
            file = r'C:\Users\ddaova\Desktop\работа\апрель нагрузка' + i + str(f) + r' апреля 2022 г.XLSX'
            print(file)
            # print(x)


            book = openpyxl.open(file, read_only = True)
            sheet = book.active
            cells = sheet['D7':'O500']
            # f = 7
            
            for Data, Time, Class, Subjects, none, Group, Event, Teach, Com, Coment, Output, Departmant in cells:
                cc = list()       
                if Teach.value == teacher: #and Departmant.value == 'Кафедра информационных систем':
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
                    search_group(Group, cc, c)
                    # print(num)
                    print(Data, Time, Class, Subjects, Group, Event, Teach, Com, Coment, Output, Departmant)
                    replacing(10, Data, Time, Class, Subjects, Group, Event, Teach, Com, Coment, Output, Departmant, num)
                        
                    
                    
                    # continue
                else:
                    continue

def cicl(f, search):
    global c
    for _ in range(30):
        try:
            # c = 0
            search(f)
            f=f+1
        except FileNotFoundError:
            print("FileNotFoundError")
            f = f+1
            

    

cicl(f, search)
input()