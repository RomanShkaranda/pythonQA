# OOP

import datetime

dotation = 50_000

class Human:
    population: int = 0 # class atribute
    money_in_country = 20_000

    def __init__(self, name, surname, sex, bday):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.__bday = bday
        self.money = dotation
        Human.total_cash(self.money)
        Human.increase_population()
        # self.__class__.increase_population() # same as above
        # print(self)





    @property # for property inside class
    def b_day(self):
        return self.__bday

    @b_day.setter # to set when property date of birth can be accessed (cause "__")
    def b_day(self, date: list[int]):
        """Expected date format [2000, 6, 28]"""
        if len(date) == 3 and type(date[0]) == int and type(date[1]) == int and type(date[2]) == int and date[0] >= 2000:
            self.__bday = datetime.datetime(*date)

    @property
    def age(self):
        return (datetime.datetime.today() - self.b_day).days // 365

    def __str__(self):
        return f'{self.name} {self.surname} {self.__bday}'

    @classmethod # general method for the whole class
    def increase_population(cls):
        Human.population += 1

    @classmethod
    def decrease_population(cls):
        Human.population -= 1

    def __del__(self):
        Human.decrease_population()
        # print(self, 'I died')

    @staticmethod
    def who_we_are(self):
        print('We are from Earth')

    def eat(self):
        print(self, 'eat')

    def money_landing(self, other, summa):
        """I borrow money"""
        if other.money >= summa:
            self.money += summa
            other.money -= summa
        else:
            self.money += other.money
            other.money = 0

    def __add__(self, other):
        return self.money + other.money

    @classmethod
    def total_cash(cls, summa):
        Human.money_in_country += summa


class Bank:
    def __init__(self):
        self.money = 1_000_000

    def money_landing(self, other, summa):
        """I borrow money"""
        if other.money >= summa:
            self.money += summa
            other.money -= summa
        else:
            self.money += other.money
            other.money = 0


mono = Bank()

alex = Human('Alex', 'Bush', 'male', datetime.datetime(2000, 5, 10))

# alex.b_day = [1955, 5, 10]
# print(alex.age)

tom = Human('Tom', 'Bush', 'male', datetime.datetime(2000, 5, 10))

alex.money_landing(tom, 5000)

m = alex + tom

tom.money_landing(mono, 50000)

print(tom.money)




