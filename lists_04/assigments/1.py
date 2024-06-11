print('---get the sum , count of even numbers , odd numbers from a list ')
numbers_list = [15, 16, 20, 3, 9, 20]
total_even_numbers = 0
total_odd_numbers = 0
count_even_numbers = 0
count_odd_numbers = 0
for item in numbers_list:
    if item % 2 == 0:
        total_even_numbers = total_even_numbers + item
        count_even_numbers = count_even_numbers + 1
    else:
        total_odd_numbers = total_odd_numbers + item
        count_odd_numbers = count_odd_numbers +1
print(total_even_numbers, total_odd_numbers, count_odd_numbers, count_even_numbers )