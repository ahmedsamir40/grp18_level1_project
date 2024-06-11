print('---program to merge 2 lists to create a new dictionary ---')

emp_ids_list = [101, 102, 103]
emp_names_list = ['ahmed','omar','sarah']

person_dict = {}
for i in range(len(emp_names_list)):
    person_dict[emp_ids_list[i]] = emp_names_list[i]

print(person_dict)