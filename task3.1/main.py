def countsort(list11):
    sortedlist = [0] * 101
    for i in list11:
        sortedlist[i] += 1
    for i in range(101):
        print((str(i) + ' ') * sortedlist[i], end='')


list1 = [int(i) for i in input().split()]
countsort(list1)
