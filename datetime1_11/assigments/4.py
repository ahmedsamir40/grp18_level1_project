# program to Count occurrences of a specific date in a list

from datetime import datetime

dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 8, 15),
    datetime(2023, 8, 15),
    datetime(2023, 5, 1)
]
given_date = datetime(2023, 8, 15)

count_occurrence = 0
for i in range(len(dates_list)):
    if given_date == dates_list[i]:
        count_occurrence = count_occurrence + 1

print(given_date,count_occurrence)