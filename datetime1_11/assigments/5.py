# program Check if all dates in a list are in the same month
from datetime import datetime

dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 12, 15),
    datetime(2023, 12, 15),
    datetime(2023, 12, 1)
]
same_month = dates_list[0].month
#print(same_month)
same_flag = True
for date in dates_list:
    if same_month != date.month:
        same_flag = False
        break
if same_flag == True:
        print('all dates in a list are in the same month ',same_month)

else:
    print('all dates are not in the same month')