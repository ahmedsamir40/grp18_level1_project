# program to go a specific a date
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()

print(today) #18-5-2024

print('----take this date variable to the first day of this month ') # 1-5-2023
first_day = today + relativedelta(day=1)
print(first_day)

print('take this date variable to the last of this month--- ') # 31-5-2023
last_day = today + relativedelta(day=31)
print(last_day)