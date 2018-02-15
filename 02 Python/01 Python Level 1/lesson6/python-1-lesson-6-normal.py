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
        self._opponent_armor = 1.0
        self._opponent_health = 1.0
        self._opponent_damage = 1.0

    def armor(self):
        return  self._armor

    def health(self):
        return self._health

    def damage(self):
        return self._damage

    def mod_health(self, diff):
        self._health += diff

    def attack(self, opponent):
        print('{} атакует {}!'.format(self.name, opponent.name))
        self._opponent_ = opponent.armor()

    def _calc_damage(self, damage):
        health -= damage / armor



class Player(Person):
    def __init__(self,name):
        self.name = name
        self._armor = 1.2
        self._health = 100
        self._damage = 50
        self._opponent_armor = 1.0
        self._opponent_health = 1.0
        self._attack_result = 1.0
        self._random_success = True
        self._is_redhat = False

    def random_success(self):
        return self._random_success

    def _calc_damage(self, opponent):
        if self._random_success:
            self._attack_result = (random.randint(50, 100) / 100) * self._damage / opponent.armor()
        else:
            self._attack_result = self._damage / opponent.armor()

    def attack_result(self, opponent):
        return self._attack_result

    def attack(self, opponent):
        print('Игрок {} атакует игрока {}!'.format(self.name, opponent.name))
        self._calc_damage(opponent)
        opponent.mod_health(-self._attack_result)
        print('Игрок {} нанес игроку {} удар с силой {}!'.format(self.name, opponent.name, self._attack_result))
        print('У игрока {} осталось {} единиц здоровья'.format(opponent.name, opponent.health()))

class Enemy(Person):
    def __init__(self,name):
        self.name = name
        self._armor = 1.2
        self._health = 100
        self._damage = 50
        self._opponent_armor = 1.0
        self._opponent_health = 1.0
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

    def attack(self, opponent):
        print('Игрок {} атакует игрока {}!'.format(self.name, opponent.name))
        self._calc_damage(opponent)
        opponent.mod_health(-self._attack_result)
        print('Игрок {} нанес игроку {} удар с силой {}!'.format(self.name, opponent.name, self._attack_result))
        print('У игрока {} осталось {} единиц здоровья'.format(opponent.name, opponent.health()))

class Fight():
    def __init__(self):
        self._attack_result = 0.0
        # self._current = 0 # здесь была попытка определять первого игрока случайным образом, и далее бегать по списку персонажей
        # self._chars = [] # в цикле, но она провалилась из-за полной нечитаемости получающегося кода

    # def define_chars(self,Player, Enemy):
    #     self._chars = [Player, Enemy]

    # def define_first_player(self):
    #     i = random.random()
    #     if i > 0.5:
    #         self._current = 1
    #     else:
    #         self._current = 0

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

print(game.start(my_player, my_enemy))