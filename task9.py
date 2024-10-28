# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
from random import randint
n = int(input())
m = [randint(0, 100) for i in range(n)]
ans = []
print(m)
k = 0
for i in range(n):
    for j in range(i+1, n):
        if m[i-k] == m[j-k]:
            m.pop(j-k)
            k += 1
print(m)