import random

def filte_list(arr1, arr2):
    resArr=[]
    for i in arr1:
        if i not in arr2:
            resArr.append(i)
    return resArr

def creat_random_list(numbers):
    return [random.randint(-10,10) for i in range(numbers+1)]
number1 = int(input("Введите количесво элементов первого массива: "))
number2 = int(input("Введите количесво элементов второго массива: "))
int_arr1=creat_random_list(number1)
int_arr2=creat_random_list(number2)

print(filte_list(int_arr1, int_arr2))
