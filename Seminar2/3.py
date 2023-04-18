# Задача 3.Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

#формула Бернулли
from math import factorial as fc
from fractions import Fraction
def c (n, k, p, q): # сочетание
    return (fc(n) // (fc(k)*fc(n-k)))* p**k * q**(n-k)
n = int(input("Введите n: "))
k = int(input("Введите k: "))
p = float(input("Введите p: ")) #ввод дробного числа через точку (НЕ запятая)
q = float(input("Введите q: "))

print(c (n, k, p, q))

#Ответ: 0.06281178035144776 ≈ 6,3%
