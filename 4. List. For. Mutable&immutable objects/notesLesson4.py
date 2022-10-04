# TERNARY OPERATOR

# number = 123
# if number % 2 == 0:
#     is_even = True
# else:
#     is_even = False
#
# # ==
#
# is_even = True if number % 2 == 0 else False

# opt1 if condition else opt2

#LIST
#syntax

# my_list = [1, "2", True, None]
#
# print(type(my_list))
# print(my_list)
#
# my_list1 = list()
# print(my_list)
#
# my_list2 = [3, 4, 5]
# res = my_list + my_list2
# print(res)
#
# res = my_list * 2
# print(res)
#
# my_list = []
# print(my_list)
#
# my_list += [1]
# print(my_list)

# my_list = []
# print(my_list)
# my_list.append(1)
# print(my_list)
# my_list.append("afasfas")
# print(my_list)
# my_list.append(True)
# print(my_list)
#
# print(2 in my_list) # found in list
#
# print(my_list.index("afasfas"))
#
# print(my_list[1]) # as with strings
# print(my_list[1].upper()) # uppercase

# NONE TYPE

# my_none = None
# print(my_none)
#
# my_list = [1, 2, True, None, "214124124sfas", [1, 2, 3, 4]]
#
# print(my_list[4][-1]) # 4 - index 4 element/ -1 - last char in string
#
# print(my_list[5][3])
# my_list[5].append(5)
# print(my_list)
#
# my_list.pop(4) # delete element by index
# print(my_list)
#
# my_list.remove(1) # 1 = int
# print(my_list)
#
# my_list[0] = ["a", "b", "c"] # replace 0 element
# print(my_list)

# iteration (while)
# my_list = [['a', 'b', 'c'], True, None, [1, 2, 3, 4, 5]]
# idx = 0
#
# while idx < len(my_list):
#     print(" - >", my_list[idx], type(my_list[idx]))
#     idx += 1
#
# my_str = "asdasdasd"
#
# while idx < len(my_str):
#     print(" - >", my_str[idx])
#     print(type(my_str[idx]))
#     idx += 1

# LOOP FOR (якраз для таких штук, точно перебере всі елементи які хочемо еребрати)

# my_list = [['a', 'b', 'c'], 2.3, True, None, [1, 2, 3, 4, 5], None]
#
# for i in my_list: # проходить через всі елементи ліста і записує результат в і
#     if i == 2.3:
#         continue # пропустить елемент 2.3/ break припинить цикл якщо знайде 2.3
#     print("->", i, type(i))
#
#     if type(i) == list:
#         for inner_element in i:
#             print("inner element", inner_element, type(inner_element))


# НЕ ДОДАВАТИ НЕ МІНЯТИ ЕЛЕМЕНТИ В ЛІСТІ ЩОБ НЕ ДОПУСТИТИ НЕСКІНЧЕННОГО ЦИКЛУ

# user_data = []
#
# name = "Roman"
# password = "214124"
# age = 29
#
# user_data.append(name)
# user_data.append(password)
# user_data.append(age)
#
# print(user_data)
#
# user_pwd = user_data[1]
# print(user_pwd)
#
#
# print(str(user_data))
#
# print((bool(user_data)))
# print(bool([]))


# зміннні і незмінні типи даних

# immutable
# a = 10
# print(id(a))
#
# a += 1
# print(id(a))

# mutable
# lst = [1, 2, 3]
# print(id(lst))
#
# lst.append(4)
# print(id(lst))

# lst1 = [1, 2, 3]
# #
# # lst2 = lst1
# #
# # lst2.append(4)
# #
# # print(lst1)
# # print(lst2)

# lst1 = [1, 2, 3]
#
# lst2 = lst1.copy()
#
# lst2.append(4)
#
# print(lst1)
# print(lst2)
#
# lst1 = [1, 2, 3, ["a", "b"]]
#
# lst2 = lst1.copy()
#
# lst2[3].append("c")
#
# print(lst1)
# print(lst2)

# import copy
#
# lst1 = [1, 2, 3, ["a", "b"], 4]
#
# lst2 = copy.deepcopy(lst1)
#
# lst2[3].append("c")
#
# print(lst1)
# print(lst2)






