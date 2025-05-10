"""
Задание 2.

Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n.
"""
# 2, 4, 8, 10, 14

n = 15
e = 3
current = 1
summa = 0
while current <= n:
    if current % e != 0 and current % 2 == 0:
        summa += current
    current += 1
print(summa)
