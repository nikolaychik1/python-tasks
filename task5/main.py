# Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в виде ЕГЭ,
# каждый из них оценивается целым числом от 0 до 100 баллов. При этом абитуриенты,
# набравшие менее 40 баллов (неудовлетворительную оценку) по любому экзамену из конкурса выбывают.
# Остальные абитуриенты участвуют в конкурсе по сумме баллов за три экзамена.
#
# В конкурсе участвует N человек, при этом количество мест равно K.
# Определите проходной балл, то есть такое количество баллов, что количество участников,
# набравших столько или больше баллов не превосходит K, а при добавлении к ним абитуриентов,
# набравших наибольшее количество баллов среди непринятых абитуриентов,
# общее число принятых абитуриентов станет больше K.
inputfile = open('input.txt', 'r', encoding='utf8')
number = int(inputfile.readline())
dict1 = []
for line in inputfile:
    newline = line.split()
    if int(newline[-1]) >= 40 and int(newline[-2]) >= 40 \
            and int(newline[-3]) >= 40:
        dict1.append(newline)
inputfile.close()
dict1.sort(key=lambda a: int(a[-1]) + int(a[-2]) + int(a[-3]))
dict1.reverse()
dict2 = []
for n in dict1:
    summ = int(n[-1]) + int(n[-2]) + int(n[-3])
    dict2.append(summ)


def konkurs(m, k, konk):
    if m <= k:
        return 0
    elif konk[k] == konk[0]:
        return 1
    for i in range(k, 0, -1):
        if konk[i] < konk[i - 1]:
            return konk[i - 1]


outputfile = open('output.txt', 'w', encoding='utf8')
print(konkurs(len(dict2), number, dict2), file=outputfile)
outputfile.close()
