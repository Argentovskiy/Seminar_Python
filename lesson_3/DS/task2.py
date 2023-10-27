# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.


list_1 = [1, 4, 3, 7, 8, 9, 2]
k = 10
min=0
for i in range(len(list_1)):
    for j in range(len(list_1)):
        if list_1[j]>list_1[i]:
            min=list_1[i]
            list_1[i]=list_1[j]
            list_1[j]=min
            j=1
if k>list_1[len(list_1)-1]:
    print(list_1[len(list_1)-1])
else:
    for i in range(len(list_1)):
        if list_1[i]>=k:
            if list_1[i]-k<=k-list_1[i-1]:
                print(list_1[i])
                break
            else:
                print(list_1[i-1])
                break