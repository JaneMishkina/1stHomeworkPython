# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

import random

list_random = [random.randint(1,11) for _ in range(10)]
print(list_random)
set_random = set(list_random)

print(set_random)
print(len(set_random))

# mass = input().split()
# new_mass = []
# for i in mass:
#     if i not in new_mass:
#         new_mass.append(i)
# count = len(new_mass)
# print(count)