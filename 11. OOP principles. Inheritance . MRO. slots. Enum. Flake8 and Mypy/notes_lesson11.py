class Person:
    population = 0

    __slots__ = 'money'  # define with which object we can work

    def __init__(self, money):
        self.money = money

    def hello(self):
        print("Hello")

    def __eq__(self, other):
        return self.money == other.money


p = Person(500)
p2 = Person(500)



