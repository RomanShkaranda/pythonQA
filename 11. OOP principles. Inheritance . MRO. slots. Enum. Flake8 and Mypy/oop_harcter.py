from abc import ABC, abstractmethod
from enum import Enum


class BaseAttribute(Enum): # we can store here some data
    LIFE = 100


class Character(ABC):

    __slots__ = ('life')

    def setup(self):
        self.life = BaseAttribute.LIFE.value

    @abstractmethod
    def attack(self):
        raise NotImplemented


class Gun:

    def __init__(self, armor):
        self.armor = armor


class Tank(Character):

    def __init__(self, gun_load, gun: Gun):
        self.setup()
        self.gun = gun
        self.gun_load = gun_load

    def attack(self, other):
        if type(other) == Tank:
            self.gun_load -= 1
            other.life -= 30
        print('Attack')


class Javellin(Character):

    def __init__(self):
        self.setup()
        self.gun_load = 1

    def attack(self):
        print("Attack")

    def br(self, message: str = 'br'):
        print(message)


g = Javellin()
g.br(555)


tank = Tank(200, Gun(120))
tank2 = Tank(100, Gun(120))
print(tank.life)
print(tank2.life)
tank2.attack(tank)
print(tank.life)

tanks = [Tank(500, Gun(200)) for tank in range(100)]
print()

