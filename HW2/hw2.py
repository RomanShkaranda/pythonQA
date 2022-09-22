# Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
#
# Попросіть користувача ввести свсвій вік (можно використати константу або input()).
# - якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# - якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
# - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
#
# P.S. На екран має бути виведено лише одне повідомлення! Макож подумайте над варіантами, коли введені невірні дані


userInput = input("Твій вік: ")
inputInt = int(userInput)

if not userInput.isdigit(): # суто перевірка чи число
    print("Не смішно!")
elif inputInt > 120: # загуглив що найстарішій людині на зараз 116 років, округлив до 120
    print("Введіть коректні дані")
elif inputInt < 7:
    print("Де твої батьки?")
elif inputInt < 16:
    print("Це фільм для дорослих!")
elif inputInt > 65:
    print("Покажіть пенсійне посвідчення!")
elif '7' in userInput:
    print("Вам сьогодні пощастить!")
else:
    print("А білетів вже немає!")








