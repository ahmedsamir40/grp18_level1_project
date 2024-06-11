print('--create a list of dates within a date range included---')
from datetime import datetime
from dateutil.relativedelta import relativedelta
start_range = datetime(2023,1,1)
end_range = datetime(2023,1,10)
date_list = []

while start_range <= end_range:
    date_list.append(start_range.date())
    start_range = start_range + relativedelta(days=1)


print(date_list)