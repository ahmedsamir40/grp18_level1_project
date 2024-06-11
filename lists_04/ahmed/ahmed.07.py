numbers_list = [12, 35, 9, 56, 24]
var_tamp = numbers_list[0]
numbers_list[0] = numbers_list[-1]
numbers_list[-1] = var_tamp
print(numbers_list)