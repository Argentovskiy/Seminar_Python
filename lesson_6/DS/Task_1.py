def rangeForFiltr(list1, min_namb, max_namb):
    result=[]
    for i in range(len(list1)):
        if list1[i]>=min_namb and list1[i]<=max_namb:
            result.append(i)
            print(i)

    return result
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10
print(rangeForFiltr(list_1,min_number,max_number))