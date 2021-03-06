# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

print('Курс: Python1; урок: 2; уровень: hard; задача: 1')

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

y_items = equation.split(' ')

k = float(y_items[2].replace('x',''))
b = float(4)
if y_items[3] == '-':
    b = -b
y = k*x + b

print('equation =', equation)
print ('x =', x)
print('y =', y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
#date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

print('\n'+'Курс: Python1; урок: 2; уровень: hard; задача: 2')

m_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

res = 'Y'
while res != 'N':
    correct = 1 # по умолчанию ввод корректен
    print('Введите дату в формате dd.mm.yyyy:')
    date = input()
    if len(date) != 10: # проверка длины строки; если не 10 символов, ввод некорректен
        correct = 0
    else:
        date_parts = date.split('.') # если длина 10 символов, пробуем разбить на части по разделителю
        if len(date_parts) != 3: # если разбиение не дало 3 части, то ввод некорректен
            correct = 0
        else:
            if not (1 <= int(date_parts[2]) <= 9999): # если год не в диапазоне 1 - 9999, то ввод некорректен
                correct = 0
            else:
                if not (1 <= int(date_parts[1]) <= 12): # если месяц не в диапазоне 1 - 12, то ввод некорректен
                    correct = 0
                else:
                    if not (1 <= int(date_parts[0]) <= m_days[int(date_parts[1])]): # если день не в нужном диапазоне, то ввод некорректен
                        correct = 0
    if not correct:
        print('Дата введена некорректно')
    else:
        print('Дата введена корректно')
    res = ''
    while res != 'Y' and res != 'N':
        res = input('Хотите попробовать еще раз? (Y/N)').upper()

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

# Решение:
# Башня состоит из поставленных друг на друга квадратов, стороны которых являются арифметической прогрессией с шагом 1,
# первый член также равен 1. Таким образом, нам необходимо:
# а) в цикле определить номер, и, следовательно, размер стороны квадрата, в котором расположена комната с заданным номером;
# б) вычесть из номера комнаты количество комнат, содержащихся в предыдущих квадратах;
# в) с помощью целой части от деления и остатка от деления определить номер этажа и положение комнаты на этаже
#
# Реализуем решение в коде:

print('\n'+'Курс: Python1; урок: 2; уровень: hard; задача: 3')
res = 'Y'
while res != 'N':
    room = 0
    while not 1 <= room <= 2000000000:
        room = int(input('Введите номер комнаты (от 1 до 2 000 000 000):'))

    current = 0
    prev_rooms = 0
    current_side = 0
    prev_stages = 0

    while current < room:   # ищем сторону и номер квадрата, в котором находится искомая комната
                            # условие "<" задано для корректного обсчета комнат в правых верхних углах квадратов,
                            # при "<=" произойдет "перелет" в следующий квадрат
        prev_rooms += current_side ** 2 # параллельно считаем количество комнат в пройденных квадратах
        prev_stages += current_side # и количество этажей в пройденных квадратах
        current_side += 1
        current += current_side ** 2
    if room == 1: # небольшой костыльчик, чтобы не городить переходы
        current_side = 1
    print('Потребовалось', current_side, 'циклов для поиска целевого квадрата')
    # теперь в current_side у нас содержится номер и размер стороны искомого квадрата,
    # а в prev_rooms - суммарное количество комнат в предыдущих квадартах
    position = (room - prev_rooms) % current_side # позиция комнаты на этаже
    if position == 0: #комната попадает на правый край этажа
        position = current_side
        stage = (room - prev_rooms) // current_side + prev_stages
    else:  # комната не на краю этажа
        stage = 1 + (room - prev_rooms) // current_side + prev_stages # +1, т.к. делением нацело мы получим только предыдущий этаж
    print(stage, position)

    res = ''
    while res != 'Y' and res != 'N':
        res = input('Хотите попробовать еще раз? (Y/N)').upper()