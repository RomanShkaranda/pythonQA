'''
напишіть функцію, яка перевірить, чи передане їй число є парним чи непарним (повертає True False)
напишіть функцію. яка приймає стрічку, і визначає, чи дана стрічка відповідає результатам роботи методу capitalize()
(перший символ є верхнім регістром, а решта – нижнім.) (повертає True False)
написати до кожної функції мінімум 5 assert
написати декоратор, який добавляє принт з результатом роботи отриманої функції + текстовий параметр, отриманий ним
(декоратор з параметром - це там, де три функції)
при цьому очікувані результати роботи функції не змінюються (декоратор просто добавляє принт)
'''


def param_func(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return_value = func(*args, **kwargs)
            print(f"{text} {return_value}")
            return return_value

        return wrapper
    return decorator


@param_func("The is_even function returns ")
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


@param_func("The is_capital function returns ")
def is_capital(string):
    if string == string.capitalize():
        return True
    else:
        return False


def main():
    is_even(2)
    is_capital("asfasf")


main()



