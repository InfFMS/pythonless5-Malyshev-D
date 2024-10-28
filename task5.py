# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
n = int(input())
m = [int(input()) for i in range(n)]
k = 0
for i in range(n):
    if m[i] == max(m):
        k += 1
print(k)