# 1. Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд.
# 2. Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "sota": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною.
# Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"

# 1

text = "Preserved defective offending he daughters on or. Rejoiced prospect yet material servants out answered men admitted. Sportsmen certainty prevailed suspected am as. Add stairs admire all answer the nearer yet length. Advantages prosperous remarkably my inhabiting so reasonably be if. Too any appearance announcing impossible one. Out mrs means heart ham tears shall power every."
text = text.split()
list1 = []
vowel = ["a", "e", "i", "o", "u"]
vowel1 = []

for letters in vowel:
    for letters1 in vowel:
        res = letters1 + letters
        if res not in vowel1:
            vowel1.append(res)

for i in text:
    for a in vowel1:
        if a in i:
            list1.append(i)

print(len(list1))

# 2

my_dict = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "sota": 37.720,
    "rozetka": 38.003
}

min_number = 35.9
max_number = 37.339
markets = []

for money in my_dict.items():
    if min_number < money[1] < max_number:
        markets.append(money[0])

print("Min = ", min_number, "   ", "Max = ", max_number)
print("Match =", markets)


