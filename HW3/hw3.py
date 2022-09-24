# 1. Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".
# 2. Написати цикл, який буде вимагати від користувача ввести слово, в якому є буква "о"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви о.


while True:
    word = input("Your word: ")
    if word.find("O") < 0 and word.find("o") < 0:
        print("Enter word with letter \"o\"")
    else:
        break

while True:
    sym = input("Symbol № ")
    try:
        sym = int(sym)
    except ValueError:
        print("Not a number, try again")
    else:
        break

result = word[int(sym) - 1]

print(f"The {sym} symbol in \"{word}\" is \"{result}\"")
