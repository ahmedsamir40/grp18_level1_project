print("----program to get sum , average number is a list---")
number_list = [15, 16, 20, 3, 15, 20]



# loop [for i - for each ]
total = 0
for item in number_list:
    total = total + item

print('total= ',total)
average = total / len(number_list)
average = round(average,2)
print('average =',average)
