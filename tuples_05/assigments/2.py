

company_employees = [
                (101, 'ahmed essam', 10000.0, ' cairo '),
                (102, 'ebrahim ahmed', 9000.0, ' cairo '),
                (103, 'adham ali', 5000.0, '  cairo '),
                (104, 'islam hassan', 7000.0, ' cairo ')

]
total = 0
for item in company_employees:
    total = total + item[2]
print(total)
