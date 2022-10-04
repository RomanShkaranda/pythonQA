# 2. Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44].
# Напишіть код, який видалить з нього всі числа, які менше 21 і більше 74.


my_list = [11, 77, 4, 22, 0, 56, 5, 44, 95, 7, 5, 87, 13, 45, 67, 44]
copy_my_list = my_list[:]

# for number in reversed(my_list):
#     print(number)
#     print(my_list)
#     if not 21 < number < 74:
#         my_list.remove(number)

for number in copy_my_list:
    if not 21 < number < 74:
        my_list.remove(number)

print(my_list)

