# program to count fri or sat in a specific month
from datetime import datetime
from dateutil.relativedelta import relativedelta

# inputs
month = 7
year = 2024

# program

custom_date = datetime(year=year,month=month,day=1)  # 1/7/2024

end_date = custom_date + relativedelta(months=1)    # 1/8/2024
weekend_counter = 0
while custom_date < end_date:
    print(custom_date)
    # check for custom date if is is fri or sat
    if custom_date.date().weekday() in [4,5]:
        weekend_counter = weekend_counter + 1
    custom_date = custom_date + relativedelta(days=1)
print(weekend_counter)