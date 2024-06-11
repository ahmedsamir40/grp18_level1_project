# employee basic data
employee_id = 101                # int data type
employee_name = 'ahmed amr'           # string data type
employee_salary = 7000.55             # float data type
employee_job = 'python developer'       # string data type
print('-------- concat string to string')
print(employee_name + ' works as' + employee_job)


print(' --------- concat string to int ----------')
print(' --------- concat data type from int to string--- [ casting]--')
print(employee_name + ' his id = ' + str(employee_id))

print(' ---------- concat string to float------')
print('---- convert from float to int ----- [ casting]---')
print(employee_name + ' takes salary =  ' + str(employee_salary))
print('--------convert from float to int  ---------- [ casting] ')
print(employee_salary)
print(type(employee_salary))
print('----')
new_salary = int(employee_salary)
print(new_salary)
print(type(new_salary))




