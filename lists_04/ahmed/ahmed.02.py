print('------- for i loop ----------')
number_list = [10, 11, 12, 13, 14, 15]
total = 0
for i in range(len(number_list)):
    print(i, number_list[i])
    total = total + number_list[i]
print('sum = ',total)
print('sum = ',sum(number_list))

print('------------for each loop------------')
total = 0         # reset variable
for item in number_list:
    print(item)
    total = total + item
print('sum = ',total)
