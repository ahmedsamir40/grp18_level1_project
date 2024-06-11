emp_name = "ahmed samir"
emp_id = 100
emp_gross_salary = 7000
tax = 10

if emp_gross_salary >= 5000:
    tax = 10
else:
    tax = 0
emp_monthly_net_salary = emp_gross_salary - emp_gross_salary * tax / 100
print(' emp monthly net salary =',emp_monthly_net_salary)

emp_annual_net_salary = emp_monthly_net_salary * 12
print('emp annual net salary =',emp_annual_net_salary)
