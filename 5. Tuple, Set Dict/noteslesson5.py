# TUPLE
# cannot change data inside tuple
# idx and slices as in list
# operator "in" like in list

# my_tuple = (1, 2.0, True, "Four", [1, 2, 3], None, 1)

# print(my_tuple)
# print(type(my_tuple))
#
# print(my_tuple[0])
# print(my_tuple[3:5])
#
# my_tuple = (1,)
# print(type(my_tuple))
#
# my_tuple = 1, 2, 3, 4
# print(type(my_tuple))
#
# print("abcd" in my_tuple)

# for elem in my_tuple:
#     print(elem, type(elem))
#
# print((1, 2, 3) == (1, 2, 3))

# for i in range(5): # 5 цифр від 0 до 4
#     print(i)

# my_list = list("asfjnaskfjna")
# print(my_list)
# my_tuple = tuple("asfjnaskfjna")
# print(my_tuple)
#
# my_list = list(my_tuple)
# print(my_list)
#
# my_list = list(range(5, 15, 2))
# print(my_list)


# SET не зберігає порядок даних
# унікальні дані всередині
# тільки незмінні типи даних

# my_set = {1, 2.0, True, "10", "qwert", None, (1, 2, 3), 1, 2, 3}
#
# print(my_set)
#
# # my_set.add("1")
# # print(my_set)
#
# my_set.remove("10")
# print(my_set)
#
# print("10" in my_set)
#
# my_set.pop() # видаляє рандомний елемент
# print(my_set)
# print(my_set.pop())
#
# for elem in my_set:
#     print(type(elem), elem)
#
# my_set = set("wqrqwrqwrqwrqw")
# print(my_set)
#
# my_set = set([1, 2, 3, 4, 5])
# print(my_set)
#
# # FROZENSET
#
# my_frset = frozenset([1, 2, 3, 4, 5])
# print(my_frset)

# DICT dictionary (most popular)
# key and value
# keys only immutable data type, only unique, value can be everything
# getting data by keys
# dict has specified order

# my_dict = {
#     "key_1": 1,
#     "key_2": 2,
#     "key_3": 3,
#     1: 2,
#     2.2: 2,
#     False: "asfasf",
#     (1, 2, 3): [1, 2, 3]
#     }
#
# print(my_dict)
# print(my_dict["key_1"])
#
# my_dict["key_1"] = 1000
# print(my_dict)
# my_dict[(1, 2, 3)][0] = "asdas"
# print(my_dict)
#
# my_dict["asffasfas"] = 13 # adding new dict to my_dict
# print(my_dict)


# my_dict = {
#     "key_1": 1,
#     "key_2": 2,
#     "key_3": 3,
#     1: 2,
#     2.2: 2,
#     False: "asfasf",
#     (1, 2, 3): [1, 2, 3]
#     }

# for i in my_dict:
#     print("--->", i, my_dict[i]) # i shows keys
#
# for i in my_dict.keys():
#     print("--->", i)
#
# for i in my_dict.values():
#     print("--->", i)

# for i in my_dict.items():
#     print("==>", i) # i = key and value in tuple (кортедж)
#     print("key is ", i[0])
#     print("value is ", i[1])
#
# for key, value in my_dict.items():
#     print(key)
#     print(value)

# my_dict = {
#     "key_1": 1,
#     "key_2": 2,
#     "key_3": 3,
#     1: 2,
#     2.2: 2,
#     False: "asfasf"
# }

# print(my_dict[123])

# print(123 in my_dict.keys())
# print(my_dict.get(1))
# print(my_dict.get(123))
# print(my_dict.get(123, "asdsad")) # my_dict[123] if 123 in my_dict.keys() else "asdsad"

# my_dict.update({"a": "b", "c": "d"}) # add dict to dict
# print(my_dict)
#
# my_dict = {} # dict, not set
#
# my_dict[1] = 1
# print(my_dict)
#
# my_dict.pop(1) # delete by key
# print(my_dict)
#
# print(bool({}))
# print(bool({1:3}))
#
# my_dict = dict([(1, 2), (3, 4)])
# print(my_dict)
#
# my_dict = dict(a=1, b=2, c=3) # a, b, c = str
# print(my_dict)


# my_dict = {
#     "key_1": 1,
#     "key_2": 2,
#     "key_3": 3,
#     1: 2,
#     2.2: 2,
#     False: "asfasf"
# }
#
# res = my_dict.setdefault("key_", "Default") # if there is no such key - setdefault will create one with value
# print(res)
#
# print(my_dict)

my_dict = {
    "key_1": {
        "1": 1,
        "2": 2,
    }
}

print(my_dict["key_1"]["1"])

lst = list(my_dict.keys())
print(lst)
lst = list(my_dict.values())
print(lst)
lst = list(my_dict.items())
print(lst)



