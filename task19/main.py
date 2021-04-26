# Реализуйте класс Matrix. Он должен содержать:
#
#  Конструктор от списка списков. Гарантируется, что списки состоят из чисел,
#  не пусты и все имеют одинаковый размер. Конструктор должен копировать содержимое списка списков,
#  т. е. при изменении списков, от которых была сконструирована матрица, содержимое матрицы изменяться не должно.
#  Метод __str__, переводящий матрицу в строку.
#  При этом элементы внутри одной строки должны быть разделены знаками табуляции,
#  а строки  —  переносами строк.
#  После каждой строки не должно быть символа табуляции и в конце не должно быть переноса строки.
#  Метод size без аргументов, возвращающий кортеж вида (число строк, число столбцов).
#  Пример теста с участием этого метода есть в следующей задаче этой недели.
from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, list1):
        self.list1 = deepcopy(list1)

    def __str__(self):
        rows = []
        for row in self.list1:
            rows.append('\t'.join(map(str, row)))
        return '\n'.join(rows)

    def size(self):
        return len(self.list1), len(self.list1[0])


exec(stdin.read())
