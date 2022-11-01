"""
створіть наступну структуру
- клас шкільний_персонал - абстрактний, клас ініт не має бути абстрактним, в ініті отримувати імя, прізвище,
розмір зарплати. додайте абстрактний метод __str__
- від нього наслідуються класи вчитель, технічний персонал - додайте якісь методи на свій розсуд.
метод ініт тут не перевизначайте, ви його успадкуєте
- клас школа - назва, директор, список вчителів, список технічного персоналу, проперті місячна зарплата

при створенні школи потрібно вказати, хто директор (екземпляр класу вчителів). також автоматично створити
списки вчителів, списки технічного персоналу (використайте ліст компрехеншн,
імена та прізвища можна отримувати за допомогою рамдомного вибору із зовнішніх списків, зарплата - рандомно від 10 000 до 50 000)

створити школу.
вивести список вчителів,
вивести місячну зп всього персоналу
додайте вчителя
змініть директора (школа без директора не може існувати, директор при цьому переходить в список вчителів,
 а вчитель стає директором, і відповідно, видаляється зі списку вчителів)
"""
import random
from abc import ABC
import names
"""додав до коміту файл names"""


class Stuff(ABC):
    """
    ініт клас Stuff
    """
    def __init__(self, name, last_name, salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary


class Teacher(Stuff):
    """
    наслідуєм клас Stuff
    """
    def __str__(self):
        return f'{self.name} {self.last_name}, {self.salary}, вчитель'


class Technician(Stuff):
    """
        наслідуєм клас Stuff
        """
    def __str__(self):
        return f'{self.name} {self.last_name}, {self.salary}, прибиральник'


class School:
    """
    ініт школу
    """

    def __init__(self, school_name):
        self.school_name = school_name
        self.teacher_list = [Teacher(random.choice(names.names), random.choice(names.last_names), random.randrange(10000, 50000)) for i in range(5)]
        self.technicians_list = [Technician(random.choice(names.names), random.choice(names.last_names), random.randrange(10000, 50000)) for i in range(5)]
        self.director = random.choice(self.teacher_list)
        self.teacher_list.remove(self.director)

    def add_teacher(self, other: Teacher):
        self.teacher_list.append(other)

    @property
    def teachers(self):
        total_teachers = []
        for i in self.teacher_list:
            total_teachers.append(self.teacher_list[self.teacher_list.index(i)].name + ' ' + self.teacher_list[self.teacher_list.index(i)].last_name)
        return total_teachers

    @property
    def technicians(self):
        total_technicians = []
        for i in self.technicians_list:
            total_technicians.append(self.technicians_list[self.technicians_list.index(i)].name + ' ' + self.technicians_list[self.technicians_list.index(i)].last_name)
        return total_technicians

    @property
    def total_money(self):
        teachersalary = sum(obj.salary for obj in self.teacher_list)
        techsalary = sum(obj.salary for obj in self.technicians_list)
        summa = techsalary + teachersalary
        return summa

    def change_dir(self):
        self.teacher_list.append(self.director)
        new_dir = random.choice(self.teacher_list)
        self.teacher_list.remove(new_dir)
        self.director = new_dir


school = School('Asterix and Obelix')
print(school.teachers)
print(school.total_money)
school.change_dir()