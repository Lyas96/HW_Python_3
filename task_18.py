# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5
n = int(input("Введите количество элементов в массиве: "))
print(n)
massive = list()
for i in range(1, (n + 1)):
    massive.append(i)
print(*massive)
x = int(input("Введите число Х: "))
print(x)
min_num = (x - massive[0])
index = 0
for i in range(1, len(massive)):
  count = (x - massive[i])
  if count < min_num:
     min_num = count
     index = i
print(massive[i])