print('--program to find element in list----')
number_list = [1, 6, 3, 5, 3, 4]
number = 4


is_found = False          # boolean   Flag

for i in range(len(number_list)):
    if number == number_list[i]:
        print(number,' is found at index = ', i)
        is_found = True

if not is_found:          # is_found == false
        print(number,' is not found in the list ')
