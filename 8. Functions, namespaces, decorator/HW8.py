# 1. Напишіть декоратор, який перетворює результат роботи функції на стрінг
# 2. Напишіть докстрінг для цього декоратора


user_input1 = int(input("First int: "))
user_input2 = int(input("Second int: "))


def to_string(func):
    """
    decorator that converts user inputs into string
    """
    def wrapped_func(*args, **kwargs):
        result = str(func(*args, **kwargs))
        print(type(result))
        print(result)
        return result
    return wrapped_func

@to_string
def my_function(arg1, arg2):
    res = arg1 + arg2

    return res


my_function(user_input1, user_input2)

