# program checks if a specific falls between two provided dates
from  datetime import datetime
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
given_date = datetime(2023, 6, 15)

if start_date <= given_date <= end_date:
    print("the given date is falls between the start date and end date")
else:
    print("the given date is not falls between the start date and end date")