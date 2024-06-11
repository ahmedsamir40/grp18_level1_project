# a program to get the date after 12 working dates from a date (ex .form today 18-5-2024 ) result 3-6-2024
from datetime import  datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
jump_days = 12
result_day = today
for i in range(jump_days):
    if result_day.date().weekday() == 3: # thursday
        result_day = result_day +relativedelta(days=3)

    elif result_day.date().weekday() == 4: # friday  ( check if today is friday)
        result_day =result_day + relativedelta(days=2)
    else:
        result_day = result_day + relativedelta(days=1)

print('result day = ', result_day)