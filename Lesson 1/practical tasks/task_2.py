"""
Задание 2.

В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.

Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
"""


a, b, c  = 20, 21, 22

print(a % 2 + a // 2 + b % 2 + b // 2 + c % 2 + c // 2)