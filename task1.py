# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами.
from random import randint
n = int(input())
m = [randint(0, 1000) for i in range(n)]
print(n)
print(m[-1])
print(m[::-1])
for i in range(len(m)):
    if m[i] % 10 == (m[i] // 10) % 10 == m[i] // 100:
        print('YES')
        break
else: print('NO')
print(m[1:n-1])