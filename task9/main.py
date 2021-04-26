# Каждый из N школьников некоторой школы знает Mᵢ языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
#
# Формат ввода
#
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mᵢ, после каждого из чисел идет Mᵢ строк, содержащих названия языков,
# которые знает i-й школьник. Длина названий языков не превышает 1000 символов,
# количество различных языков не более 1000. 1≤N≤1000, 1≤Mᵢ≤500.
N = int(input())
list1 = []
language = []
for i in range(N):
    nn = int(input())
    pp = set()
    for j in range(nn):
        word = str(input())
        pp.add(word)
    language.append(pp)
setitog = language[0]
setitog1 = language[0]
for i in range(len(language)):
    setitog = setitog | language[i]
    setitog1 = setitog1 & language[i]
print(len(setitog1))
print(*setitog1, sep="\n")
print(len(setitog))
print(*setitog, sep='\n')
