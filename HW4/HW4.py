# 1. Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Зауважте, що lst1 не є статичним і може формуватися динамічно.
# 2. Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44].
# Напишіть код, який видалить з нього всі числа, які менше 21 і більше 74.
# 3. Є стрінг з певним текстом (можна скористатися input або константою).
# Напишіть код, який визначить кількість слів в цьому тексті, які закінчуються на 'о'.

# 1
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

for listItem in lst1:
    if type(listItem) == str:
        lst2.append(listItem)

print(lst2)

# 2
lst = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]

for i in lst:
    if i < 21:
        lst.pop(lst.index(i))
for a in lst:
    if a > 74:
        lst.pop(lst.index(a))

print(lst)

# 3
text = "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"
splited = text.split()
res = []

for i in splited:
    if i.endswith("o"):
        res.append(i)

print(len(res))




