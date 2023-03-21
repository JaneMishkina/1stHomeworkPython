# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

# from random import randint

# list_random = [randint(1,11) for _ in range(10)]
# number_K = int(input("Input K: "))

# part_1 = list_random[:number_K]
# #print(part_1)
# part_2 = list_random[number_K:]
# #print(part_2)

# final_list = part_2 + part_1
# print(list_random)
# print(final_list)

lst = [1, 2, 3, 4, 5]
k = 2
for i in range(k):
    lst.insert(0, lst.pop())
print(lst)