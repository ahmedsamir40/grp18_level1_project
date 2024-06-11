print('-------------loop over elements of a list using for 1 index loop ---')
numbers_list = [14,20,5,16,10]
total = 0
for i in range(len(numbers_list)):
    print(i,numbers_list[i])
    total = total + numbers_list[i]
print(total)
print(sum(numbers_list))     # biltin function


print('------loop over elements of list using for each loop----')
total = 0
for item in numbers_list :
    print(item)  # number_list[i]
    total = total + item
print(total)
