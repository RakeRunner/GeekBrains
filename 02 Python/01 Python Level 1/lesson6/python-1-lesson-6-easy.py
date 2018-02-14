# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
class TownCar:

    def __init__(self, name ):
        self.name = name
        self.speed = 120
        self.color = 'Silver'
        self.is_police = False
        self.direction = 'North'
    def go(self):
        print('Машина {} поехала'.format(self.name))
    def stop(self):
        print('Машина {} остановилась'.format(self.name))
    def turn(self, direction):
        print('Машина {} повернула на '.format(self.name, direction))

class SportCar:

    def __init__(self, name ):
        self.name = name
        self.speed = 350
        self.color = 'Red'
        self.is_police = False
        self.direction = 'East'
    def go(self):
        print('Машина {} поехала'.format(self.name))
    def stop(self):
        print('Машина {} остановилась'.format(self.name))
    def turn(self, direction):
        print('Машина {} повернула на '.format(self.name, direction))

class WorkCar:

    def __init__(self, name ):
        self.name = name
        self.speed = 80
        self.color = 'DarkBlue'
        self.is_police = False
        self.direction = 'South'
    def go(self):
        print('Машина {} поехала'.format(self.name))
    def stop(self):
        print('Машина {} остановилась'.format(self.name))
    def turn(self, direction):
        print('Машина {} повернула на '.format(self.name, direction))

class PoliceCar:

    def __init__(self, name ):
        self.name = name
        self.speed = 240
        self.color = 'PoliceColor'
        self.is_police = True
        self.direction = 'West'
    def go(self):
        print('Машина {} поехала'.format(self.name))
    def stop(self):
        print('Машина {} остановилась'.format(self.name))
    def turn(self, direction):
        print('Машина {} повернула на '.format(self.name, direction))


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class BaseCar:
    def __init__(self, name ):
        self.name = name
        self._speed = 80
        self._color = 'DarkBlue'
        self._is_police = False
        self.direction = 'South'
        self.current_speed = 0
    def go(self):
        print('Машина {} поехала'.format(self.name))
    def stop(self):
        print('Машина {} остановилась'.format(self.name))
    def turn(self, direction):
        print('Машина {} повернула на '.format(self.name, direction))
    def get_speed(self):
        return self._speed
    def get_color(self):
        return self._color
    def get_police(self):
        return self._is_police

class TownCar2(BaseCar):

    def __init__(self, name ):
        self.name = name
        self._speed = 120
        self._color = 'Silver'
        self._is_police = False
        self.direction = 'North'

class SportCar2(BaseCar):

    def __init__(self, name ):
        self.name = name
        self._speed = 350
        self._color = 'Red'
        self._is_police = False
        self.direction = 'East'

class WorkCar2(BaseCar):

    def __init__(self, name ):
        self.name = name
        self._speed = 80
        self._color = 'DarkBlue'
        self._is_police = False
        self.direction = 'South'

class PoliceCar2(BaseCar):

    def __init__(self, name ):
        self.name = name
        self._speed = 240
        self._color = 'PoliceColor'
        self._is_police = True
        self.direction = 'West'

my_car1 = TownCar2('Golf')
print(my_car1.get_color())
my_car2 = PoliceCar2('Crysler')
print(my_car2.get_color())
print(my_car2.get_police())