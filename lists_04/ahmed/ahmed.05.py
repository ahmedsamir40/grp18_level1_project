numbers_list = [15, 16, 20, 3, 15, 20]
total = 0
for item in numbers_list:
    total = total + item
print(total)

average = total / len(numbers_list)
average = round(average, 2)
print(average)