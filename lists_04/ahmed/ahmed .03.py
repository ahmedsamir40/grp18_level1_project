number_list = [15, -16, 20, -3, 0, 20]
total_pos, total_neg, count_pos, count_neg, count_zeros = 0, 0, 0, 0, 0


for item in number_list:

    if item > 0:
        total_pos = total_pos + item
        count_pos = count_pos + 1
    elif item < 0:
        total_neg = total_neg + item
        count_neg = count_neg + 1
    else:
        count_zeros = count_zeros + 1
print(total_pos, total_neg, count_pos,count_neg, count_zeros)
