# Задача 2. О случайной непрерывной равномерно распределенной величине B известно, 
# что ее дисперсия равна 0.2. 
# Можно ли найти правую границу величины B и ее среднее значение зная, 
# что левая граница равна 0.5? Если да, найдите ее.

a = 0.5
D = 0.2

import math
b = a + math.sqrt(12*D)

print(f"Правая граница = {b}")
print(f"Среднее значение = {(a+b)/2}")

