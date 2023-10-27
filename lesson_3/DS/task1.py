list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
k = 2

# Введите ваше решение ниже
result=0
for i in range(len(list_1)):
    if k==list_1[i]:
        result+=1
print(result)