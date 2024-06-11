# program to count fri to sat in specific month

from datetime import datetime
from dateutil.relativedelta import relativedelta

# inputs
m = 7
y = 2024

# program
custom_date = datetime(year=y, month=m, day=1) # 1-7-2024
print(custom_date)

end_date = custom_date + relativedelta(months=1)  # 1-8-2014
weekend_counter = 0
while custom_date < end_date:
    print(custom_date)
    # check for the custom date if it is fri or sat
    if custom_date.date().weekday() in [4,5]:  # fri =4, sat = 5
        weekend_counter = weekend_counter + 1
    custom_date = custom_date + relativedelta(days=1) # increase the date by a day every iteration
print('count of weekends = ', weekend_counter)
