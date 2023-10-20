# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8
import os
os.system("clear")
n=256

sum=1
for i in range(1,n):
    if sum<=n:
        print(sum)
        sum=sum*2
