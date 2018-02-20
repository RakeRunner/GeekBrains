#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""
import random

class LottoCard:

    def __init__(self):
        self._MAX_NUMBER = 90
        self._NUMBER_COUNT = 90
        self._LINES_NUMBER = 3
        self._DIGITS_NUMBER = 5
        self._LINE_LENGTH = 9
        self._is_player = True
        self._pouch = [_ for _ in range (1, self._MAX_NUMBER+1)]
        self._card = []

    def get_player(self):
        return self._is_player

    def set_player(self, player):
        self._is_player = player

    def generate_card(self):
        self._card = random.sample(self._pouch, self._LINES_NUMBER * self._DIGITS_NUMBER)
        self._line1 = self._card[0:self._DIGITS_NUMBER]
        self._line2 = self._card[self._DIGITS_NUMBER:self._DIGITS_NUMBER*2]
        self._line3 = self._card[self._DIGITS_NUMBER*2:self._DIGITS_NUMBER*3]
        self._line1.sort()
        self._line2.sort()
        self._line3.sort()

        for i in range(0, self._LINE_LENGTH - self._DIGITS_NUMBER):
            self._line1.insert(random.randint(1, len(self._line1)), '  ')
            self._line2.insert(random.randint(1, len(self._line2)), '  ')
            self._line3.insert(random.randint(1, len(self._line3)), '  ')

        self._card = self._line1 + self._line2 + self._line3

    def print(self):
        if self._is_player:
            print('----- Ваша карточка -------')
        else:
            print('--- Карточка компьютера----')
        for i in range (0, len(self._card)):
            print('{:>2}|'.format(self._card[i]), end = '')
            if i > 0 and (i+1) % self._LINE_LENGTH == 0:
                print()
        print('---------------------------')

    def is_in(self, value):
        if isinstance(value, int) and value in self._card:
            return self._card.index(value)
        else:
            return -1

    def cross_out(self, value):
            self._card[self._card.index(value)] = '--'

class LottoPouch():
    def __init__(self):
        self._pouch = [_ for _ in range (1,91)]

    def get_barrel(self):
        i = random.randint(0, len(self._pouch)-1)
        return self._pouch.pop(i)

    def __len__(self):
        return len(self._pouch)

    def make_full(self):
        self._pouch = [_ for _ in range(1, 91)]

class LottoGame():
    def __init__(self):
        self._player_card = LottoCard()
        self._computer_card = LottoCard()
        self._player_card.generate_card()
        self._computer_card.generate_card()
        self._computer_card.set_player(False)
        self._pouch = LottoPouch()

    def _choice(self, barrel):
        choice = ''
        while choice != 'Y' and choice != 'N':
            choice = input('Зачеркнуть цифру? (Y/N)').upper()
            if choice != 'Y' and choice != 'N':
                print('Некорректный ввод.')
        if choice == 'Y':
            if self._player_card.is_in(barrel) >= 0:
                self._player_card.cross_out(barrel)
                return True
            else:
                return False
        if choice == 'N':
            if self._player_card.is_in(barrel) < 0:
                return True
            else:
                return False

    def start(self):
        while len(self._pouch) > 1:
            self._player_card.print()
            self._computer_card.print()
            barrel = self._pouch.get_barrel()
            print('Ваш ход. Выпал бочонок с номером {}.'.format(barrel))
            if self._choice(barrel):
                print('Правильно! Продолжаем играть.')
                self._player_card.print()
                self._computer_card.print()
            else:
                print('Неправильно! Вы проиграли.')
                return 0
            barrel = self._pouch.get_barrel()
            print('Ход компьютера. Выпал бочонок с номером {}.'.format(barrel))
            if self._computer_card.is_in(barrel) > 0:
                print('Компьютер зачеркивает в карточке число {}'.format(barrel))
                self._computer_card.cross_out(barrel)
            else:
                print('Компьютер продолжает игру.')

            input('В мешочке осталось {} бочонков. Нажмите Enter для продолжения игры.'.format(len(self._pouch)))
        print('Игра окончена. В мешочке осталось {} бочонков.'.format(len(self._pouch)))

my_game = LottoGame()
my_game.start()




