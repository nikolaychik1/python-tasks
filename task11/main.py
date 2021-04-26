# Вам дан словарь, состоящий из пар слов.
# Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Для одного данного слова определите его синоним.
i = int(input())
slovar = {}
for j in range(i):
    slova = input()
    slovo1 = slova.split()[0]
    slovo2 = slova.split()[1]
    slovar[slovo1] = slovo2
    slovar[slovo2] = slovo1
question = input()
print(slovar[question])
