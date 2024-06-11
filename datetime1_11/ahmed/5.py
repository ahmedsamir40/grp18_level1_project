# program to show the nearest sunday
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()  # 18-52024
print('---find the nearst sunday from today--')  # 19/5/2024 (sun)
nearst_sunday = today + relativedelta(weekday=calendar.SUNDAY)
print(nearst_sunday)

print('----find the nearst 2nd sunday from today ----')
nearst_2n_sunday = today+relativedelta(weekday=calendar.SUNDAY,weeks=1)
print(nearst_2n_sunday)

print('---find the first sunday from the beginning of the current month--') # 5-5-2024
first_sunday_current_month= today + relativedelta(weekday=calendar.SUNDAY,day=1)
print(first_sunday_current_month)

print('---find the first sunday from the beginning of the next month--')  # 2-6-2024
first_sunday_next_month= today + relativedelta(weekday=calendar.SUNDAY,months=1,day=1)
print(first_sunday_next_month)

print('---find the first sunday from the beginning of the current year--')  # 7-1-2024
first_sunday_current_year= today + relativedelta(weekday=calendar.SUNDAY,month=1,day=1)
print(first_sunday_current_year)
print('---find the first sunday from the beginning of the next year--')  # 5-1-2025

first_sunday_next_year= today + relativedelta(weekday=calendar.SUNDAY,years=1,month=1,day=1)
print(first_sunday_next_year)
