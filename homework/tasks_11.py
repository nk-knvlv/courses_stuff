from decimal import Decimal
from random import randint
from datetime import date


# 1
# Создать пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три приватных атрибута,
# конструктор, геттеры и сеттеры для каждого атрибута, два метода.

class Robot:
    last_model = 0


class Computer:
    __cpu = False
    __login: str
    __password: str

    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    @property
    def cpu(self):
        return self.cpu

    @property.setter
    def cpu(self, cpu):
        self.__cpu = cpu

    @property
    def login(self):
        return self.login

    @property.setter
    def login(self, login):
        self.__login = login

    @property
    def password(self):
        return self.__password

    @property.setter
    def password(self, password):
        self.__password = password

    def turn_on(self):
        self.__cpu = True

    def sing_in(self, login, password):
        if login == self.__login and password == self.__password:
            return True
        return False


class Catgirl(Robot):
    __uid: int
    __race: str
    __character: str

    name: str

    def __init__(self, race, character):
        self.__uid = super().last_model + 1
        super().last_model += 1
        self.__race = race
        self.__character = character

    @property
    def uid(self):
        return self.uid

    @uid.setter
    def uid(self, uid):
        self.__uid = uid

    @property
    def race(self):
        return self.__race

    @race.setter
    def race(self, race):
        self.__race = race

    @property
    def character(self):
        return self.character

    @character.setter
    def character(self, character):
        self.__character = character

    def love(self, target):
        while target.life > 0:
            self.love(target)

    @staticmethod
    def kill(target):
        del target


class Grave:
    __material: str
    __inside: str
    __secret: str

    def __init__(self, material, inside, secret):
        self.__material = material
        self.__inside = inside
        self.__secret = secret

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material):
        self.__material = material

    @property
    def inside(self):
        return self.__inside

    @inside.setter
    def inside(self, inside):
        self.__inside = inside

    @property
    def secret(self):
        return self.__secret

    @secret.setter
    def secret(self, secret):
        self.__secret = secret

    def fill_in(self, dead_human):
        self.__inside = dead_human

    def get_secret_from_inside(self):
        return self.secret + self.inside


class Casino:
    __bank: int
    __jackpot: int
    __owner: str

    def __init__(self, owner_name):
        self.__owner = owner_name
        self.__bank = 0
        self.__jackpot = 0

    @property
    def bank(self):
        return self.__bank

    @bank.setter
    def bank(self, value):
        self.__bank = value

    @property
    def jackpot(self):
        return self.__jackpot

    @jackpot.setter
    def jackpot(self, value):
        self.__jackpot = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner_name):
        self.__owner = owner_name

    def feed_owner(self):
        self.__bank = 0

    def enter_trouble(self):
        self.__owner = None


class Success:
    __luck: decimal
    __try_count: int
    __owner: str

    def __init__(self):
        self.__luck = Decimal(1, 100)
        self.__try = 0
        self.__owner = None

    @property
    def luck(self):
        return self.__luck

    @luck.setter
    def luck(self, luck):
        self.__luck = luck

    @property
    def try_count(self):
        return self.__try

    @try_count.setter
    def try_count(self, try_count):
        self.__try_count = try_count

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @staticmethod
    def get_draw():
        return randint(1, 100)

    def change_owner(self):
        del self.__owner


# 2

class Car:
    __make: str
    __model: str
    __speed: int
    __year_of_manufacture: int

    def __init__(self, make, model):
        self.__make = make
        self.__model = model
        self.__speed = 0
        self.__year = date.year

    def speed_up(self):
        self.__speed += 5

    def speed_down(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    @property
    def speed(self):
        return self.__speed

    def reversal(self):
        self.__speed = -self.__speed
