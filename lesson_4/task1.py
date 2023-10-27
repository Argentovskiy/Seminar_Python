input_list = "a a a b c a a d c d d"
user_list = input_list.split()

result_list = []

for i in range(len(user_list)):
    tmp = user_list[:i].count(user_list[i])
    if tmp >= 1:
        result_list.append(f'{user_list[i]}_{tmp}')
    else:
        result_list.append(user_list[i])

print(input_list)
print(" ".join(result_list))