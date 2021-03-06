# В выборах Президента Российской Федерации побеждает кандидат,
# набравший свыше половины числа голосов избирателей. Если такого кандидата нет,
# то во второй тур выборов выходят два кандидата, набравших наибольшее число голосов.
#
# Формат ввода
#
# Каждая строка входного файла содержит имя кандидата,
# за которого отдал голос один избиратель. Известно, что общее число кандидатов не превосходит 20,
# но в отличии от предыдущих задач список кандидатов явно не задан.
# Читайте данные из файла input.txt с указанием кодировки utf8.
#
# Формат вывода
#
# Если есть кандидат, набравший более 50% голосов, программа должна вывести его имя.
# Если такого кандидата нет, программа должна вывести имя кандидата, занявшего первое место,
# затем имя кандидата, занявшего второе место. Выводите данные в файл output.txt с указанием кодировки utf8.
dict1 = {}
i = 0
j = 0
summ = 0
inputfile = open('input.txt', encoding='utf8')
for word in inputfile.read().split('\n'):
    dict1[word] = dict1.get(word, 0) + 1
list1 = sorted(dict1.items(), key=lambda p: p[1])
list1.reverse()
for word in list1:
    summ = summ + int(word[1])
with open('output.txt', 'w', encoding='utf-8') as fout:
    if int(list1[0][1]) > summ / 2:
        print(list1[0][0], file=fout)
    else:
        print(list1[0][0], file=fout)
        print(list1[1][0], file=fout)
