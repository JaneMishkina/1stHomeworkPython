# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума
#  и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

n = int(input("Введите количество элементов в списке: "))
amin = int(input("Введите минимальное значение для поиска: "))
amax = int(input("Введите максимальное значение для поиска: "))

from random import randint
list_1 = [randint(1, 20) for i in range(n)]
print(list_1)

# list_2 = []
# for i in range (len(list_1)):
#     if amin <= list_1[i] <= amax:
#        list_2.append(i)
# print(list_2)

list_2 = [i for i in range(len(list_1)) if amin <= list_1[i] <= amax]
print(list_2)

# a = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# k = int(input("Начало диапазона индексов:"))
# t = int(input("Начало диапазона индексов:"))
# print([i for i,j in enumerate(a) if k < j < t])