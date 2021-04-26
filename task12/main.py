words, n = {}, []
file = open('input.txt', encoding='utf8')
for line in file:
    n.extend(line.split())
for i in n:
    words[i] = words.get(i, 0) + 1
a = max(sorted([i for i, k in words.items()]),
        key=lambda x: words[x])
print(a)
