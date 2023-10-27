# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# # Пользователь его не вводит

# user_list=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# result_set=set()
# for el in user_list:
#     result_set.add(el.values())
# print(result_set)


# import random

# n = int (10)
# list = [random.randint(-2,5) for i in range(n)] 
# print (list)
# count = 0
# for i in range (1,len(list)):
#     if (list[i]>list[i-1]):
#         count+=1
# print(count)

# 21:35
# for i in range (1, len(list)):
#     if (list[i]>list[i-1]):
#         count+=1

# user_num = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(user_num)):
#     if user_num[i] > user_num[i - 1]:
#         count += 1
        
# print(count)

# 21:38
# user_num = [0, -1, 5, 2, 3]
# count = 0
# for i in range(len(user_num)-1):
#     if user_num[i] < user_num[i + 1]:
#         count += 1
        
# print(count)