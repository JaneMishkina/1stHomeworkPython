# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число:   "))
res = 1
while res <= n:    
    print(res, end=' ')
    res *= 2