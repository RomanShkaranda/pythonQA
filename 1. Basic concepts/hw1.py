#1. Задача: Створіть дві змінні first=10, second=30. Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.
#2. Задача: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1. Виведіть на екран результат кожного порівняння.
#3. Створіть репозиторій на https://gitlab.com/ або на https://github.com/ і опублікуйте файл там
#Встановіть Python, якщо в когось відсутній
#https://www.python.org/
#IDE
#https://www.jetbrains.com/pycharm/

#задача 1
first = 10
second = 30

add = first + second
sub = first - second
mul = first * second
div = first / second
exp = first ** second
floor = first // second
mod = first % second

print(add, sub, mul, div, exp, floor, mod)


#задача 2
#якщо використовувати змінні з попередньої задачі:

b1 = first > second
b2 = first < second
b3 = first == second
b4 = first != second

print(b1, b2, b3, b4)

#якщо брати порівняння чисел результатів попередньої задачі:

bool1 = mod > floor
bool2 = exp < mod
bool3 = sub == mul
bool4 = mod != exp

print(bool1, bool2, bool3, bool4)






