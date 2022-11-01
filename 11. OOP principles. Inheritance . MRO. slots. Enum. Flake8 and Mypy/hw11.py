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
import names
import random


class Stuff:
    def __init__(self, name, last_name, salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary


class School:

    def __init__(self, school_name):
        self.school_name = school_name
        self.director = ''
        self.teacher_list = [Stuff(random.choice(names.names), random.choice(names.last_names), random.randrange(10000, 50000)) for i in range(5)]
        self.technicians_list = [Stuff(random.choice(names.names), random.choice(names.last_names), random.randrange(10000, 50000)) for i in range(5)]
        self.teachers = []
        self.technicians = []
        self.summa = []

    def total_summa(self):
        return sum(self.summa)

    def add_teacher(self, other):
        self.teacher_list.append(other)

        for i in self.teacher_list:
            self.teachers.append(self.teacher_list[self.teacher_list.index(i)].name + ' ' + self.teacher_list[self.teacher_list.index(i)].last_name)

        for i in self.technicians_list:
            self.technicians.append(self.technicians_list[self.technicians_list.index(i)].name + ' ' + self.technicians_list[self.technicians_list.index(i)].last_name)

        for i in self.teacher_list:
            self.summa.append(self.teacher_list[self.teacher_list.index(i)].salary)

        for i in self.technicians_list:
            self.summa.append(self.technicians_list[self.technicians_list.index(i)].salary)

        self.director = random.choice(self.teachers)
        self.teachers.remove(self.director)

    def change_dir(self):
        self.teachers.append(self.director)
        self.director = random.choice(self.teachers)
        self.teachers.remove(self.director)


school = School('Asterix and Obelix')
school.add_teacher(Stuff('Richard', 'Hendrix', 33000))
school.change_dir()

print(school.teachers)
print(school.total_summa())
print(school.director)

print()
