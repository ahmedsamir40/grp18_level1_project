numbers_list = [1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
unique_list = []
duplacate_list = []
for item in numbers_list:
    if item not in unique_list:
        unique_list.append(item)
    elif item not in duplacate_list:
        duplacate_list.append(item)

print(numbers_list)
print(unique_list)
print(duplacate_list)