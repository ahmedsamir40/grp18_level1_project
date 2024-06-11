print('----program to calculate pos . neg numvers sum and count ----')
numbers_list = [15, -16, 20, -3, 0, 20]
total_pos = 0
total_neg = 0
count_pos = 0
count_neg = 0
count_zero = 0
for item in numbers_list:
    if item > 0:
        total_pos = total_pos + item
        count_pos = count_pos + 1
    elif item < 0:
        total_neg = total_neg + item
        count_neg = count_neg + 1
    else:
        count_zero = count_zero + 1

print(total_pos, count_pos, total_neg, count_neg, count_zero)


