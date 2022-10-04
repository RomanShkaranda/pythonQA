# 1. Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд.

text = "Preserved defective offending daughters on or. Rejoiced prospect yet material servants out answered men admitted. Sportsmen certainty prevailed suspected am as. Add stairs admire all answer the nearer yet length. Advantages prosperous remarkably my inhabiting so reasonably be if. Too any appearance announcing impossible one. Out mrs means heart ham tears shall power every."
vowel = ["a", "e", "i", "o", "u"]

text = text.lower()
text = text.split()
paircounter = 0

for word in text:
    list(word)
    print(list(word))
    counter = 0
    for letter in word:
        if letter in vowel:
            counter += 1
            if counter == 2:
                paircounter += 1
                break
        else:
            counter = 0

print(paircounter)

















print(text)
