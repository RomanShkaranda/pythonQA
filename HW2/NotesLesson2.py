# my_int = 100
#
# print(my_int)
# print(type(my_int))
#
# res = float(my_int)
# print(res)
# print(type(res))
#
# my_float = 1.9
#
# res = int(my_float)
# print(res)
# print(type(res))
#
# res = bool(0)
# print(res)
# print(type(res))
#
# res = bool(10)
# print(res)
# print(type(res))
#
#
#
# # string (str)
#
# my_str = 'Hello World'
# print(my_str)
# print(type(my_str))
#
# my_str = '''Hello
# World'''
# print(my_str)
#
# my_str = 'Hello "World"'
# print(my_str)
#
# my_str = "\"Hello\" World"
# print(my_str)

# transform to str

# my_int =10

# res = str(my_int)
# print(res)
# print(type(res))

# res = int('12321')
# print(res)
# print(type(res))

# res = float('12.321')
# print(res)
# print(type(res))
#
# # Concatenation

# my_str1 = 'Hello'
# my_str2 = 'World'

# result = my_str1 + " " + my_str2
# print(result)

# result = my_str1 * 3 # = my_str1 + my_str1 + my_str1
# print(result)
# print(type(result))
#
# my_str1 *= 3
# print(my_str1)
# print(type(my_str1))

# Formatting

# name = 'Roman'
# age = 29
#
# # Hello, my name is Roman, i\'m 39
#
# res = 'Hello, my name is' + ' ' + name + ', i\'m' + ' ' + str(age)
# print(res)
#
# res = 'Hello, my name is %s, i\'m %s' % (name, age)
# print(res)
#
# # Format method
#
# template = "Hello, my name is {}, i\'m {}"
# result = template.format(name, age)
# print(result)
#
# template = "Hello, my name is %s, i\'m %s"
# result = template % (name, age)
# print(result)
#
# template = "Hello, my name is %s, i\'m %s"
# result = template % (age, name)
# print(result)
#
# template = "Hello, my name is {name1}, i\'m {age1}"
# result = template.format(name1 = 'Adele', age1 = 56)
# print(result)
#
# # f-string
#
# name1 = "Joe"
# age1 = 23
#
# template1 = f"Hello, my name is {name1}, i\'m {age1}"
# print(template1)
#
# result = len(template1) #string length
# print(result)
#
# result = 'a' in template1 #is there "a" letter
# print(result)
#
# result = 'Joe' in template1 #is there Joe name
# print(result)




# if else

# if condition:
#     print('if condition true')
# else:
#     print('if condition false')

# condition = False #boolean
#
# if condition: #condition always = boolean
#     print(f'Inner code block IF {condition}')
# else:
#     print(f'Inner code block ELSE {condition}')

# a = 100
# b = 20
#
# res = a > b
#
# if res:
#     print('Inner code block IF a > b')
# else:
#     print('Inner code block ELSE a < b')

# my_int = 100
#
# if my_int:
#     print('Inner code block IF')
# else:
#     print('Inner code block ELSE')

# my_str = 'asf' # '' = false/ 'asd' = true
# if my_str:
#     print('Inner code block IF')
# else:
#     print('Inner code block ELSE')

# my_str = "abc"
#
# if my_str == "abcgf":
#     print('Yes, that\'s it')
# else:
#     print('No, that is not this string')

# my_condition = False
#
# if my_condition is True: # bad idea
#     print('Yes, that\'s true')
# else:
#     print('No, that is not true')

# my_condition = False
#
# if type(my_condition) == bool:
#     print('Yes, that\'s true')
# else:
#     print('No, that is not true')

# my_condition = 1

# if type(my_condition) == bool:
#     print('Yes, that\'s boolean')
# elif type(my_condition) == str:
#     print('That is string')
# else:
#     print('No, that is neither boolean nor string')

# my_condition = True
#
# if type(my_condition) == str:
#     if '1' in my_condition:
#         print('It has 1')
#     print('Yes, that\'s string')
# elif type(my_condition) == bool:
#     if my_condition:
#         print('TRUE')
#     else:
#         print('This is boolean but it is not True')
#     print('That is boolean')


# a = 100
# b = 20
# c = 30
#
# # AND
# if a > b and b < c: # first and second statements are needed to be true
#     print('a > b')
#
# # OR
# if a > b or b < c: # at least one condition must be true
#     print('a > b')
#
# if a > b or b < c and c <= 10 or b > 2: # and is executed first = (a > b or b < c) and (c <= 10 or b > 2)
#     print('a > b')
#
#     cond1 = a > b or b < c
#     cond2 = c <= 10 or b > 2
#
# if cond1 and cond2:
#     print('a > b')

# execution order:
# ()
# ** (піднесення до ступеня)
# * / // %
# + -
# == != < >
# and
# or
# =


# # string methods (advanced)
#
# my_string = '12345678923'
#
# res = my_string.replace('23', 'abc')
# print(res)
#
# res = my_string.replace('123', '')
# print(res)
#
# my_string = '----12345----'
#
# res = my_string.strip('-') #lstrip - left/ rstrip - right
# print(res)



userinput = input('Enter smth: ')

print(type(userinput))

print(f'Your entered string is: {userinput}')

