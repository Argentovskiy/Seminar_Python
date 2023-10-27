# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

# Пример

# На входе:


var1 = '5 5'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'
# На выходе:
# 3 5
# m1=[]
# m2=[]
# j=[]
# for i in var2.split():
#     m1.append(i)
 
# for i in var3:
#     m2.append(i)
# print(m1,m2)
mn=(set(var2.split())&set(var3.split()))
sortmn=[]
temp=0
print(mn)
for i in mn: 
    if (isinstance(i, (int, float, complex)) or i.isdigit()):
        sortmn.append(i)
for i in range(len(sortmn)):
    for j in range(len(sortmn)):
        if sortmn[j]>sortmn[i]:
            temp=sortmn[j]
            sortmn[j]=sortmn[i]
            sortmn[i]=temp
            j=0

print(sortmn)