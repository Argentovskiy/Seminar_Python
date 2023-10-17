# Задача №9. Общее обсуждение
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120
n=int(input("Введитн fibonacci:"))
a=1
b=0
i=1
fibonacci=0
count=0
result=0

while i<=n+1:
    print(fibonacci, end=" ")
    if fibonacci == n:
       result=i
       break
    
    fibonacci=a+b
    a=b
    b=fibonacci
    i+=1
if result==0:
     print("\n Нет такого числа")
else:
    print(f"\n Число {n} по счету на {result} месте")
