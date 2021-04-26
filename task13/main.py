# Дан текст. Выведите все слова,
# встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте,
# а при одинаковой частоте появления — в лексикографическом порядке.
fIn = open('input.txt')
Dict1 = {}
for word in fIn.read().split():
    Dict1[word] = Dict1.get(word, 0) + 1
myList = sorted(Dict1.items())
myList.sort(key=lambda x: x[1], reverse=True)


for word in myList:
    print(word[0], sep='\n')
