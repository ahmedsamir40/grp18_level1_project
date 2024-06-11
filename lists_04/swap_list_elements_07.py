print('--- swap the first element of the list ---')
numbers_list = [12, 35, 9,56,26]

var_temp = numbers_list[0]  # 12
numbers_list[0] = numbers_list[-1]   # [24,35,9,56,26]
numbers_list[-1] = var_temp
print(numbers_list)