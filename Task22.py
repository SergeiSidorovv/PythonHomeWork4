# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество чисел во множестве n: "))
m = int(input("Введите количество чисел во множестве m: "))

list_n = [int(input("Введите число во множество n:")) for _ in range(n)]
list_m = [int(input("Введите число во множество m:")) for _ in range(m)]

print(list_n)
print(list_m)
print(set(list_n + list_m))
