import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def createdir(directory = '', report_error = 0):
    if directory == '':
        if report_error:
            print('Не указано имя каталога для создания')
        return False
    try:
        os.mkdir(directory)
    except FileExistsError:
        if report_error:
            print('Каталог {} уже существует'.format(directory))
        return False
    if report_error:
        print('Каталог {} успешно создан'.format(directory))
    return True

def removedir(directory, report_error = 0):
    if directory == '':
        if report_error:
            print('Не указано имя каталога для удаления')
        return False
    if os.path.exists(directory):
        try:
            os.rmdir(directory)
            if report_error:
                print('Каталог {} успешно удален'.format(directory))
            return True
        except OSError:
            if report_error:
                print('Каталог {} содержит файлы и не может быть удален'.format(directory))
            return False
    else:
        if report_error:
            print('Каталог {} отсутствует и не может быть удален'.format(directory))
        return False


for i in range(1,10):
    createdir('dir_' + str(i), 1)

for i in range(1,10):
    removedir('dir_' + str(i), 1)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def listdirs(directory = ''):
    contdir = []
    if directory == '':
        d = os.walk(os.getcwd())
    else:
        try:
            d = os.walk(directory)
        except FileExistsError:
            return []
    for i in d:
        contdir.append(i)
    return(contdir[0][1])

print(listdirs())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def selfcopy():
    if __name__ == '__main__':
        file_path = os.path.split(sys.argv[0])
        new_file_name = file_path[1]+'.copy'
        while os.path.exists(os.path.join(file_path[0],new_file_name)):
            new_file_name += '.copy'

        shutil.copy(file_path[1],new_file_name)

selfcopy()