person_age = input('please inter your age')
person_age = int (person_age)
print(person_age)
print(type(person_age))

if person_age >= 16:
    print('you are a man')
elif person_age >=11:
    print('you are a boy')
elif person_age >= 0:
    print('you are a child')
else:
    print('invalid age')
