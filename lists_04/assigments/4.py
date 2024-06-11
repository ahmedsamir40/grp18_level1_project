numbers_list = [1, 6, 3, 6, 3, 6]
number = 6
count_number = 0

for item in numbers_list:
    if item == number:
        count_number = count_number + 1
        print('number appear in the list',count_number)
     else:
        print('number is not appear in list')