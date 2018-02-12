# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

print('Курс: Python1; урок: 3; уровень: easy; задача: 1')

def my_print (name, age, city):
    print('%s, %s года(а), проживает в городе %s'% (name, age,  city))

res = 'Y'
while res != 'N':
    name = input('Введите имя: ')
    age  = input('Введите возраст: ')
    city = input('Введите город: ')
    my_print(name, age, city)
    res = ''
    while res != 'Y' and res != 'N':
        res = input('Хотите попробовать еще раз? (Y/N)').upper()


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
print('Курс: Python1; урок: 3; уровень: easy; задача: 2')

def my_max3(a, b, c):
    max = -float('inf')
    if a > max:
        max = a
    if b > max:
        max = b
    if c > max:
        return c
    return max

res = 'Y'
while res != 'N':
    var_a = float(input('Введите число 1:'))
    var_b = float(input('Введите число 2:'))
    var_c = float(input('Введите число 3:'))

    print ('Максимальное из введенных чисел равно: ', my_max3(var_a, var_b, var_c))

    res = ''
    while res != 'Y' and res != 'N':
        res = input('Хотите попробовать еще раз? (Y/N)').upper()

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

# Тестовый входной набор:
# Арбуз
# Манго
# Абракадабра
# Квазимодо12
# Абвгдейка
# Сейшельский
# Океанариум
# *END*
print('Курс: Python1; урок: 3; уровень: easy; задача: 3')
# ***
def my_max_string(*args):
    max_len = 0
    ret_list = []
    for i in args:
        if len(i) > max_len:
            max_len = len(i)
    for i in args:
        if len(i) == max_len:
            ret_list.append(i)
    return ret_list
# ***
res = 'Y'
while res != 'N':
    print('Вводите строки по одной. Конец ввода - строка *END*:')
    in_str = ''
    input_strings = []
    while in_str != '*END*':
        in_str = input()
        input_strings.append(in_str)
    print('Строка(и) с максимальной длиной во входной последовательности:', my_max_string(*input_strings))

    res = ''
    while res != 'Y' and res != 'N':
        res = input('Хотите попробовать еще раз? (Y/N)').upper()
