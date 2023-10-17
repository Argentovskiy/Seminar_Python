# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9
import random
import os
os.system("cls")

# N=int(input("Введите число арбузов "))
# max=0
# min=999

# for i in range(N):
#     mass=random.randint(1,10)
#     print(mass, end=' ')
#     if mass <=min:
#         min=mass
#     if mass>=max:
#         max=mass
# print("\n самый легкий арбуз: ", min)
# print("Самый тяжелый арбуз: ", max)


n=int(input("Введите число арбузов "))
mass_list=[]
for _ in range(n):
    mass_list.append(random.randint(1,25))
min_=mass_list[0]
max_=mass_list[0]
for i in mass_list:
    if i<=min_:
        min_=i
    if i>=max_:
        max_=i
print("\n самый легкий арбуз: ", min_)
print("Самый тяжелый арбуз: ", max_)

print('*',min(mass_list), max(mass_list))