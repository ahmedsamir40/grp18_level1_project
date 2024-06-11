print('-----main tuples operation ---------')


print('---- create and print tuple -----')
my_tuples =(101, 'ahmed samir', 8000.0, 'nasr city - cairo ')
print(type(my_tuples))


print('---------- access element in a tuple by index -------------')

print(my_tuples[3])
# my_tuples = 'maadi'   error
# print my_tuples

print('------------ un packing tuple ----- ')
person_id, person_name, person_salary, person_address = my_tuples
print(person_name,person_address)

print('------ Loop over Tuple -------')

for i in range(len(my_tuples)):
    print(my_tuples[i])
print('------')
for item in my_tuples:
    print(item)
