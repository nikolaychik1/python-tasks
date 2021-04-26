count = {}
res = []
words = [x.strip() for x in
         open('input.txt', 'r', encoding='utf-8').read().split()]
for word in words:
    count.setdefault(word, 0)
    res.append(count[word])
    count[word] += 1
print(*res)
