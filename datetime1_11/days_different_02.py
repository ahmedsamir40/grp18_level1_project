# from datetime module import datetime class
from datetime import datetime

# from relativedelta module found  in dateutil pkg  import  relativedelta class
from dateutil.relativedelta import relativedelta

print('---GET the difference between 2 dates ')

print('1-get the difference  between 2 dates in days as a total ')

today = datetime.now()
custom_date = datetime(year=2019,month=3,day=10)   # 10-march-2024
different_in_days = today - custom_date
print(different_in_days)
print(different_in_days.days)

print('-----get the difference between 2 dates in years , month , days using  relativedelta module-----')
# create object different_in_parts from class relativedelta  using constructor  ()
different_in_part = relativedelta(today,custom_date)
print(different_in_part)
print(different_in_part.years,different_in_part.months,different_in_part.days)