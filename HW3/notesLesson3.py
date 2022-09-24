# DRY
# don't repeat yourself

# KISS
#keep it simple stupid

# YAGNI
# you aren't gonna need it



# LOOPS (цикли)
# while

# counter = 0

# while counter < 10:
#     print(f"Hello world - {counter}")
#     if counter % 2 == 0:
#         print("Match odd")
#     counter += 1
#
# print("End of loop")

# counter = 0
#
# while True:
#     print(f"Hello world - {counter}")
#     if counter % 2 == 0:
#         print("Match odd")
#     counter += 1
#
#     if counter > 10:
#         break     # припиняє виконання циклу
#
# print("End of loop")

# counter = 0
#
# while True:
#     counter += 1
#     if counter % 2 == 0:  # % залишок від ділення
#         continue     # пропускаємо непарні числа
#         print("Match odd")
#     print(f"Hello world - {counter}")
#
#     if counter > 10:
#         break
#
# print("End of loop")

# while True:
#     user_input = input("enter int:")
#     if user_input.isdigit():
#         print(f"Thanks for {user_input}")
#         break
#     print(f"{user_input} - it is not int")



#str

# my_str = "asdsadsada"
#
# print(my_str.find("sd")) # повертає індекс з якого починається стрінга
#
# print(my_str.find("a", 3, 9)) # 3, 9 - діапазон пошуку
# print(my_str[0]) # шукаємо за індексом
# print((len(my_str))) # довжина стрінги
# print(my_str[-1])


#SLICES
# my_str = "123456789"
#
# print(my_str)
# print("my_str", my_str[0])
# print("my_str[2:5]", my_str[2:5])
# print("my_str[3:15]", my_str[3:15])
# print("my_str[3:15]", my_str[3:15:2]) # останнє число - крок
# print("my_str[3:15]", my_str[3:15:-1])
# print("my_str[2:5]", my_str[2:])
# print("my_str[2:5]", my_str[2::2])
# print("my_str[2:5]", my_str[:]) # дає всю стрінгу
#
#
# a = 1
# b = 2
# c = -1
# print("my_str", my_str[a:b:c])


# TRY EXCEPT # перехоплення помилок

# userinput = input("Enter int:")
#
# try:
#     userinput = int(userinput)
# except:
#     print("It is not an int")
#
# print("Done")

# userinput = input("Enter int:")

# try:
#     userinput = int(userinput)
#     userinput = 10 / userinput
# except ZeroDivisionError as e:
#     print("It is 0")
# except ValueError as e:
#     print("It is not an int")
#
#
# print("Done")


# try:
#     userinput = int(userinput)
#     userinput = 10 / userinput
# except Exception as e: # е - змінна де зберігається інформація про помилку
#     print("It is ERROR")
#     print(type(e))
# except:
#     print("Error")
#
#
# print("Done")

# try:
#     userinput = int(userinput)
#     userinput = 10 / userinput
# except (ZeroDivisionError, ValueError) as e: # е - змінна де зберігається інформація про помилку
#     print("It is ERROR")
#     print(type(e))
# except:
#     print("Error")
#
#
# print("Done")

# try:
#     userinput = int(userinput)
#     userinput = 10 / userinput
# except:
#     print("Error")
# else:
#     print("No errors")
#
#
# print("Done")

# try: # писати тільки те, що може призвести до виникнення помилки
#     userinput = int(userinput)
#     userinput = 10 / userinput
# except:
#     print("Error")
# else:
#     print("No errors")
# finally:
#     print("Final code") # це проходымо в будь якому выпадку
#
# print("Done")


# while True:
#     user_input = input("Give me float: ")
#
#     try:
#         result = float(user_input)
#     except ValueError as e:
#         print(f"It\'s not a float {user_input}")
#         print(f"VALUE ERROR {type(e), e}")
#     else:
#         print("Thanks")
#         break





