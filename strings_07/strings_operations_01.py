# show strings functions
print('---- Create and print string ----')
emp_name = 'Ahmed Samir'
print(emp_name)
print(type(emp_name))

print('-------- upper(), lower() functions -------------')
upper_emp_name = emp_name.upper()
lower_emp_name = emp_name.lower()
print(emp_name)         # Ahmed samir
print(upper_emp_name)   # AHMED SAMIR
print(lower_emp_name)   # ahmed samir

print('------ isupper(), islower(), isalpha() , isalnum(),  isdigit()  functions --- True , False --')
print(upper_emp_name.isupper())
print(lower_emp_name.islower())
print(emp_name.isalpha())
emp_code = '101'
print(emp_name.isalpha())
print(emp_code.isdigit())
emp_code = '101abc'
print(emp_code.isalnum())

print('-------------- endsWith() function -----------------')
file_name = 'egypt.PDF'
file_name = file_name.lower()
if file_name.endswith('pdf'):
    print('is a book')
elif file_name.endswith('mp3') or file_name.endswith('wave'):
    print('it is song')
else:
    print('unknown type')

print('-------------- startswith() function ---------')
emp_mobile = '01123456789'
if emp_mobile.startswith('011'):
    print('it is etisalat')
elif emp_mobile.startswith('010'):
    print('it is vodafone')
else:
    print('unknown mobile ')

print('------ in membership ----to find word in string ----------')
emp_cv = 'iam a programmer , iam interest in python java c++'
if 'python' in emp_cv and 'java' in emp_cv:
    print('it is wanted emp')
else:
    print('it is not the wanted emp')


print('-------------- count function -----------')

emp_cv = 'iam a programmer , iam interest in python c++, iam a  professional in python'

print('python keyword occurs times ', emp_cv.count('python'))

print('---------- index(),  replace() functions |  slicing---------------')

emp_email = 'ahmed.samir.mohamed@gmail.com'
print(emp_email.index('@'))
user_name = emp_email[0:emp_email.index('@')]    #'@'
print('user name ', user_name)
domain_name = emp_email[emp_email.index('@') + 1:]
print('domain name ', domain_name)

# change  username ,replace with space
user_real_name = user_name.replace('.',' ',1)
print(' user real name = ',user_real_name)

print('--------------- Looping :  Loop over letters of string -----------------------')
for letter in emp_email:
    print(letter)
print('------for i index loop----')
for i in range(len(emp_email)):
    print(emp_email[i])

print('-----------split() function to split words  of string into list of words ---  ')
my_courses = 'java python oracle linux network'
courses_list = my_courses.split()
print(courses_list)
for course in courses_list:
    print(course)

print('------ return the list back to string using join() function --------')
courses_list.reverse()
new_courses = ' '.join(courses_list)
print(new_courses)
print('---------- strip(), title(), swapcase(), find(), rfind() Self study   -------------------')
student_name = '  marwan  '
print(student_name)
student_name = student_name.strip()
print(student_name)

student_name = student_name.title()
print(student_name)

student_name = student_name.swapcase()
print(student_name)

my_courses = 'java python oracle linux python network'
print(my_courses.find('python'))      # first occurrence
print(my_courses.rfind('python'))     # last occurence