# Задача 9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input: 5
# Output: 120

a = int(input("Введите число:"))
factorial=1
while a>1:
    factorial*=a
    a-=1
print(f"Факториал = {factorial}")