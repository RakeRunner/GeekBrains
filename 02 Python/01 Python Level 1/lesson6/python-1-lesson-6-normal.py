# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random

class Person:

    def __init__(self,name):
        self.name = name
        self._armor = 1.2
        self._health = 100
        self._damage = 35
        self._attack_result = 0.0

    def armor(self):
        return  self._armor

    def health(self):
        return self._health

    def damage(self):
        return self._damage

    def mod_health(self, diff):
        self._health += diff

    def attack(self, opponent):
        print('Игрок {} атакует игрока {}!'.format(self.name, opponent.name))
        self._calc_damage(opponent)
        opponent.mod_health(-self._attack_result)
        print('Игрок {} нанес игроку {} удар с силой {}!'.format(self.name, opponent.name, round(self._attack_result, 2)))
        print('У игрока {} осталось {} единиц здоровья'.format(opponent.name, round(opponent.health(), 2)))

    def _calc_damage(self, opponent):
        self._attack_result = self._damage / opponent.armor()


class Player(Person):
    def __init__(self,name):
        self.name = name
        self._armor = 1.2
        self._health = 100
        self._damage = 50
        self._attack_result = 1.0
        self._random_success = True
        self._is_redhat = False

    def random_success(self):
        return self._random_success

    def _calc_damage(self, opponent):
        if self._random_success:
            self._attack_result = round((random.randint(50, 100) / 100) * self._damage / opponent.armor(), 2)
        else:
            self._attack_result = self._damage / opponent.armor()

    def attack_result(self, opponent):
        return self._attack_result

class Enemy(Person):
    def __init__(self,name):
        self.name = name
        self._armor = 1.2
        self._health = 100
        self._damage = 50
        self._attack_result = 1.0
        self._random_success = True
        self._is_wolf = False

    def random_success(self):
        return self._random_success

    def _calc_damage(self, opponent):
        if self._random_success:
            self._attack_result = (random.randint(50, 100) / 100) * self._damage / opponent.armor()
        else:
            self._attack_result = self._damage / opponent.armor()

    def attack_result(self, opponent):
        return self._attack_result

class Fight():
    def __init__(self):
        self._attack_result = 0.0

    def start(self, Player, Enemy):
        while Player.health() >= 0 and Enemy.health() >= 0:
            Player.attack(Enemy)

            if Player.health() > 0 and Enemy.health() > 0:
                input('\n' + 'Enter нажми, если дальше биться желаешь')
            print('-' * 80)

            if Enemy.health() > 0:
                Enemy.attack(Player)

            if Player.health() > 0 and Enemy.health() > 0:
                input('\n' + 'Enter нажми, если дальше биться желаешь')
            print('-' * 80)

        if Player.health() <= 0:
            return ('\n' + 'В этой схватке игрок {} над игроком {} победу одержал!'.format(Enemy.name, Player.name))
        elif Enemy.health() <= 0:
            return ('\n' + 'В этой схватке игрок {} над игроком {} победу одержал!'.format(Player.name, Enemy.name))
# ---- Main -----------
my_player = Player(input('Как зовут тебя, юный падаван? :'))
my_enemy = Enemy(input('Как соперника зовут твоего? :'))

game = Fight()
i = random.random()
if i > 0.5:
    print(game.start(my_player, my_enemy))
else:
    print(game.start(my_enemy, my_player))