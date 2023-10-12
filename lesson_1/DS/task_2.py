# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n=123
a=0
print(n)
a=a+n%10
print(a)

n=int(n/10)
print(n)
a=a+n%10
print(a)
n=int(n/10)
print(n)
a=a+n%10
print(a)