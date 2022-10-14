# FUNCTIONS
# namespace (scope)

# def my_function(b):
#     a = 10
#
#     print(a)
#     return a
#
#
# a = 100
# print(a)
# my_function(1)


# def my_function():
#    print("inside", a)
#
#
# a = 100
# print("outside", a)
# my_function()


# def my_function(var):
#    print("inside", var)
#
#
# a = 100
# print("outside", a)
# my_function(1)

# def my_function():
#     print("inside", global_var)
#     global_var += 1
#
#
# global_var = 100
# print("outside", global_var)
# my_function()

# def my_function(global_var):
#
#     global_var.append(1)
#     print("inside", global_var)
#
#
# global_var = []
# global_var = my_function(global_var)
# print("outside", global_var)
# my_function()

# def foo():
#     pass


# def my_function(global_var):
#
#     global_var.append(1)
#     print("inside", global_var)
#
#     foo()
#
#     return global_var
#
#
# global_var = []
# global_var = my_function(global_var)
# print("outside", global_var)
# my_function()

# var_1 = 100
#
# def my_function():
#     global var_1
#     var_1 += 1
#     print("inside", var_1)
#
# print("outside before", var_1)
#
# my_function()
#
# print("outside after", var_1)


# DECORATORS

# a, b = 10, 20
#
# def foo(arg1, arg2):
#     print("inside function")
#
#
# if isinstance(a, int) and isinstance(b, int):
#     foo(a, b)

# def my_decorator(func):
#
#     def wrapper(*args, **kwargs):
#         print("some code before")
#         res = func(*args, **kwargs)
#         print("Some code after")
#
#         return res
#
#     return wrapper
#
# decorated = my_decorator(foo)
#
# decorated(1, 2)
#
# foo = my_decorator(foo)
#
# foo()
#
# @my_decorator # foo = my_decorator(foo)

#
# def only_ints(func):
#
#     def wrapper(*args, **kwargs):
#         print("decorator only ints")
#         for arg in args:
#             if not isinstance(arg, int):
#                 raise TypeError(f"Wrong!!!! {type(arg)}")
#         for k, v in kwargs:
#             if not isinstance(v, int):
#                 raise TypeError(f"Wrong!!!! {k} {type(v)}")
#
#         res = func(*args, **kwargs)
#
#         return  res
#
#     return wrapper()
#
# @only_ints
# def foo(arg1, arg2):
#     print("smth")
#
# res = foo(1, 2)


# ANNOTATION

# def foo(arg1, arg2):
#     """
#     Function for bla - bla #docstring
#     Function for bla - bla
#     Function for bla - bla
#     Function for bla - bla
#     """
#
#     print(arg1, arg2)
#
# foo(1, 2)

# TYPING

# def foo(arg1 : int, arg2 : float) -> str:
#     """
#
#     """
#
#     print(arg1, arg2)
#     return str(arg1)
#
# foo(1, "2")


# LAMBDA

# lst = [1, 2, 3, 4, 5, 28, 6, 51, 24, 22, 0, 213]
#
# res = sorted(lst, reverse=True)
# print(res)
#
# def foo(arg):
#     return arg % 3
#
# res = sorted(lst, key=foo)
#
# print(res)


# lst = [1, 2, 3, 4, 5, 28, 6, 51, 24, 22, 0, 213]
#
# def foo(arg):
#     return arg % 3
#
# res = sorted(lst, key=lambda val: val % 3) # res = sorted(lst, key=foo)
#
# print(res)
#
# # lambda *args, **kwargs: return smth


# TYPE TRANSFORM

# int
# float
# bool
# str
# list
# tuple
# set
# frozenset

# math

# min / max
#
# lst = [1, 2, 3, 4, 5, 28, 6, 51, 24, 22, 0, 213]
#
# print(min(lst, key=lambda x: x % 3))
# print(max(lst))
#
# print(sum(lst))
#
# res = range(1, 10, 2)
#
# for i in res:
#     print(i)

#
# enum = enumerate("Lorem ipsum")
#
# for i in enum:
#     print(i)

# def foo(val):
#     return val % 3


# lst = [1, 2, 3, 4, 5, 28, 6, 51]
# for i in lst:
#     i = foo(i)
#     print(i)
#
# # mapping
#
# mapped = map(foo, lst)
#
# for i in mapped:
#     print(i)

# for i in map(foo, lst):
#     print(i)

# for i in map(lambda x: x % 3, lst):
#     print(i)

# ZIP

# lst = [21, 2, 3, 4, 5, 28, 6, 51]
# str = "asdr"
#
# # 21 a
# # 2 s
#
# zipped = zip(lst, str)
#
# for i in zipped:
#     print(i)
#
# print(type(zipped))

# lst = [21, 2, 3, 4, 5, 28, 6, 51]
#
# filtered = list(filter(lambda x: x % 2 == 0, lst))
# print(filtered)



# ANY ALL

a, b = 10, 20

if a > b or b > 0 or b - a > 10:
    print("match")

conditions = (
    a > b,
    b > 0,
    b - a > 10,
)

if any(conditions):
    print("match")




