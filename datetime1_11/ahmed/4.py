from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
print(today)
print('take this date variable to  the first  day of  this month ')  # 1/5/2024


first_day = today + relativedelta(day=1)
print(first_day)

print('take this date variable to  the last  day of  this month ')  # 31/5/2024

last_day = today + relativedelta(day=31)
print(last_day)