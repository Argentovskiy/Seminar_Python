# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4
# перетекает из 2 в 2, 3 1, 4 0


# Введите ваше решение ниже
def sum(a,b):
    sum1=0
    if a==0:
        return b
    else:
        return sum(a-1,b+1)


a = 3
b = 4
print(sum(a, b))