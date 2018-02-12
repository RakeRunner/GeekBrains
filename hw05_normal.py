# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
import shutil
import libs.easy05 as easy

def get_user_dir():
    user_dir = ''
    while not user_dir:
        user_dir = input('Введите имя папки:')
    return user_dir

while True:
    choice = input('Выберите пункт:\n'
                   '1. Перейти в папку\n'
                   '2. Просмотреть содержимое текущей папки\n'
                   '3. Удалить папку\n'
                   '4. Создать папку\n'
                   '5. Выход\n'
                       '---------------------\n'
                   'Ваш выбор:')
    if choice == '5':
        break
    elif choice == '1':
        if easy.changedir(get_user_dir()):
            print('Каталог успешно изменен. Текущий каталог: {}'.format(os.getcwd()))
    elif choice == '2':
        print(os.listdir(os.getcwd()))
    elif choice == '3':
        easy.removedir(get_user_dir(), 1)
    elif choice == '4':
        easy.createdir(get_user_dir(), 1)
    else:
        print('Некорректный ввод.')
