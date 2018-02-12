# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
import random

print('Курс: Python1; урок: 3; уровень: hard; задача: 1')

def attack (char1, char2):
    char2['health'] -= char1['damage']

player = {'name':'Player', 'health':100, 'damage':50}
enemy = {'name':'Enemy', 'health':100, 'damage':50}
player_name = input('Как зовут тебя, юный падаван? :')
player['name'] = player_name
enemy_name = input('Как соперника зовут твоего? :')
enemy['name'] = enemy_name

# print(player,enemy)
# attack(player, enemy)
# print(player,enemy)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

print('\n'+'Курс: Python1; урок: 3; уровень: hard; задача: 2')

player['armor'] = 1.2
enemy['armor'] = 1.2

def attack_armor (char1, char2, random_success = 'Y'): # random_success - изменять ли случайным образом успешность атаки;
                                                     # по умолчанию 'Y', то есть да
    if random_success != 'Y':
        char2['health'] -= char1['damage']/char2['armor']
    else:
        char2['health'] -= random.random() * char1['damage'] / char2['armor']

def read_player_from_file(player_name):
    keys = []
    values = []
    with open(player_name+'.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            keys.append(line.split(':')[0])
            if line.split(':')[0] == 'name':
                values.append(line.split(':')[1].strip())
            else:
                values.append(float(line.split(':')[1]))
        return dict(zip(keys, values))

def fight(player_name, enemy_name, rand_success = 'Y'):
    player = read_player_from_file(player_name)
    enemy = read_player_from_file(enemy_name)
    while player['health'] >= 0 and enemy['health'] >= 0:
        if player['health'] > 0:
            print('\n'+'{} нападает на {}!'.format(player['name'], enemy['name']))
            attack_armor(player, enemy, rand_success)
            print('После атаки {} у игрока {} осталось {} единиц здоровья'.format(player['name'], enemy['name'], round(enemy['health'],1)) )
        if enemy['health'] > 0:
            print('\n'+'{} нападает на {}!'.format(enemy['name'], player['name']))
            attack_armor(enemy, player, random_success = rand_success)
            print('После атаки {} у игрока {} осталось {} единиц здоровья'.format(enemy['name'], player['name'], round(player['health'],1)) )
        if player['health'] > 0 and enemy['health'] > 0:
            input('\n'+'Enter нажми, если дальше биться желаешь')
        print('-' * 80)
    if player['health'] <= 0:
        print('\n'+'В этой схватке игрок {} над игроком {} победу одержал!'.format(enemy['name'], player['name']))
    elif enemy['health'] <= 0:
        print('\n'+'В этой схватке игрок {} над игроком {} победу одержал!'.format(player['name'], enemy['name']))

with open(player['name']+'.txt', 'w', encoding='UTF-8') as file:
    for key in player.keys():
            file.write(key + ':' + str(player[key]) + '\n')

with open(enemy['name'] + '.txt', 'w', encoding='UTF-8') as file:
    for key in enemy.keys():
            file.write(key + ':' + str(enemy[key]) + '\n')

print('\n'+'Руки нетвердые у вас, потому ущерб от удара силе его равен не будет')
input('Enter нажми, если схватку начать хочешь')
print('\n'+'-' * 80)
fight(player['name'], enemy['name'], rand_success = 'Y')
