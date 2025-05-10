"""
Задание 3.

Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********
"""

rows = 5
star = '*'
space = ' '
spaces = rows - 1
stars = 1
for _ in range(rows):
    print(spaces * space + star * stars + spaces * space)
    spaces -= 1
    stars += 2
