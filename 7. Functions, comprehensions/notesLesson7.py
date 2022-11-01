# FUNCTIONS

# syntax

# def get_int_number(message): # keyword + funcname + (arguments, outer data)
#     while True:
#         try:
#             age = int(input(message))
#         except:
#             print("Wrong")
#         else:
#             break
#     return age
#
# user_age = get_int_number("Give me your age: ")
#
# print(user_age)
#
# lenght = get_int_number("Lenght?")
#
# print(lenght)


# def my_function(arg1, arg2):
#     result = arg1 + arg2
#
#     return result
#
#
# res = my_function(1, 2) # arg1 = 1, arg2 = 2
#
# print(res)

# def my_function(arg1, arg2):
#     result = arg1 + arg2
#
#     # return result # => returns None
#
# res = my_function(1, 2)
#
# print(res)


# def my_func():
#     for i in range(10):
#         print("---->", i)
#
# my_func()


# def my_function(arg1, arg2, arg3):
#     print("arg1", arg1)
#     print("arg2", arg2)
#     result = (arg1 + arg2) * arg3
#
#     return result
#
# res = my_function(2, 3) # possitional argument adding
#
# var1 = 10
# var2 = 20
# # res = my_function(arg1=var1, arg2=var2) # naming argument adding
#
# res = my_function(arg1=1, arg2=2, arg3=3)
#
# res = my_function(1, arg2=2, arg3=3) # combine adding - first goes possitional argument
#

# def my_function(arg1, arg2, arg3):
#
#     res = arg1, arg2, arg3
#
#     return res
#
# result = my_function("124", "12312", "sadasd")

# def my_function(arg1, arg2, arg3=0): # 0 - default value
#
#     print("arg1", arg1)
#     print("arg2", arg2)
#     print("arg3", arg3)
#
#     res = arg1, arg2, arg3
#
#     return res
#
# result = my_function("124", "12312")

# def my_function(arg1, arg2, arg3):
#
#     print("arg1", arg1)
#     print("arg2", arg2)
#     print("arg3", arg3)
#
#     return
#
# res = my_function("124", [2], {"1:2"})

# def my_function1(lst1):
#
#     print("lst1", lst1)
#
#     my_list.append(1)
#     return lst1
#
#
# my_list = [1, 2, 3]
# print(my_list)
# my_list = my_function1(my_list)
#
# print(my_list)

# def my_function(lst1=[]):
#     print("lst1", lst1)
#
#     lst1.append(1)
#
#     return lst1
#
# my_list = [1, 2, 3]
#
# print("my_list", my_list)
# my_list = my_function(my_list)
# print("my_list", my_list)
#
# my_list2 = my_function()
# print("my_list2", my_list2)
#
# my_list2 = my_function()
# my_list2 = my_function()
# my_list2 = my_function()
# print("my_list2", my_list2)


# def my_function(lst1=None):
#     print("lst1", lst1)
#     if lst1 is None:
#         lst1 = []
#     lst1.append(1)
#
#     return lst1
#
# mylist2 = my_function()
# mylist2 = my_function()
# mylist2 = my_function()
# print(mylist2)

# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8. Functions, namespaces, decorator, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які
# присутні в lst1. Зауважте, що lst1 не є статичним і може формуватися динамічно.

# def my_function(lst):
#     result_list = []
#
#     if not isinstance(lst, (list, tuple)): # type(lst) == list
#         return result_list # return stops the function if cond = true
#
#     for i in lst:
#         if isinstance(i, str):
#             result_list.append(i)
#
#     return result_list
#
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8. Functions, namespaces, decorator, 'Python', 9, 0, 'Lorem Ipsum']
#
# res = my_function(lst1)
# print(res)
#
# res = my_function(["1", 2, "3"])
# print(res)



# def my_function(a, b, c, *args):
#     print("Inside function")
#     print(a, b, c)
#     print(type(args))
#     print(args)
#
# my_function(2, 5, 7)
# my_function(1, 2, 3, 4, 5, 6, 7, 8. Functions, namespaces, decorator, 9, 0)

# def my_function(a, b, c, *args):
#     print("Inside function")
#     print(a, b, c)
#     print(type(args))
#     print(args)
#
#     for i in args:
#         print(i)
#
# my_function(2, 5, 7)

# def my_function(arg1, arg2, **kwargs):
#     print("Inside function")
#     print(type(kwargs))
#     print(kwargs)
#
#     for i in kwargs:
#         print(i)
#
# my_function(2, 5, a=10, c=10)

# def my_function(arg1, arg2, *args, **kwargs):
#     print("Inside function")
#     print(args)
#     print(kwargs)
#
#     for i in kwargs:
#         print(i)
#
# my_function(2, 5, 3, 6, a=10, c=10)

# def my_function(arg1, arg2, arg3, arg4):
#     print("Inside function")
#     print(arg1, arg2, arg3, arg4)
#
# lst = [1, 2, 3, 4]
#
# my_function(*lst) # unpack = my_function(1, 2, 3, 4)

# def my_function(arg1, *args):
#     print("Inside function")
#     print(arg1, args)
#
# lst = [1, 2, 3, 4]
#
# my_function(*lst)

# def my_function(**kwargs):
#     print("Inside function")
#     print(kwargs)
#
# dict = {"a": 10, "b": 20}
#
# my_function(**dict) # unpack kwargs

# COMPREHENTION

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

for i in lst1:
    if isinstance(i, str):
        lst2.append(i)

lst2 = [i for i in lst1 if isinstance(i, str)]

lst3 = [i ** 2 for i in range(101) if i % 2 == 0]
print(lst3)

my_set = {i ** 2 for i in range(101) if i % 2 == 0}
print(my_set)











