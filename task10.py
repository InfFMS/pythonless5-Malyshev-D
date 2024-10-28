# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N =3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90
from random import randint
from math import asin, pi
n = int(input())
a = [randint(0,10) for i in range(n)]
b = [randint(0,10) for i in range(n)]
print(a, b)
scal = 0
la = 0
lb = 0
for i in range(n):
    scal += a[i]*b[i]
    la += a[i]**2
    lb += b[i]**2
print(round(asin(scal / (la * lb)**0.5) * 180/pi))