student_list = [{101:'ahmed', 102:'marwa', 103:'mostafa'}]
print(len(student_list))
print(student_list[0])
print(student_list[0][102])
student_list[0][102] = 'marwa mahmoud'
print(student_list)

print('---------------------')
student_list2 = {104:'ayman', 105:'ibrahim', 103:'mostafa'}
student_list.append(student_list2)
print(student_list)
print(student_list[1][105])