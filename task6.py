# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]
from random import randint
n = int(input())
m = [randint(0, 100) for i in range(n)]
a = []
for i in range(n//2-1, -1, -1):
    a.append(m[i])
for i in range(n-1, n//2-1, -1):
    a.append(m[i])
print(a)