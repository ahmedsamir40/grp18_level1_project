print('--program to show list of dictionaries----')

student_list = [{101:'ahmed',102: 'marwa', 103:'mostafa'}]
print(len(student_list))  #1

print(student_list[0])  # {101:'ahmed',102: 'marwa', 103:'mostafa'}
print(student_list[0][102]) # marwa

#marwa > marwa mahmoud
student_list[0][102] = 'marwa mahmoud'
print(student_list)


print('-------------')
student_dict2 = {104: 'ayman', 105: 'ibrahim'}
student_list.append(student_dict2)
print(student_list)

print(student_list[1][105]) # ibrahim


