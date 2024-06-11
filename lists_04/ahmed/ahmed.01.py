# Using Lists
print('---- 1. Creating, Printing List ---- ')
number_list = [10,11,12,13,14,15]
print(number_list)
print(type(number_list))

print('---- 2. adding element to list [ append function , insert function ] --- ')
number_list.append(17)
print(number_list)
number_list.insert(2,20)
print(number_list)

print('---- 3. Access element by index and change it -----')
print(number_list[4])
number_list[4] = number_list[4] + 5
print(number_list[4])

print('----- 4. count elements of list _ Len function : General Function -------')
print(len(number_list))
print('-------- 5. delete element from the list -- remove , pop functions -----')
number_list.remove(15)
number_list.pop(3)
number_list.pop()
print(number_list)

print('-------- 6. reverse list ----------')
number_list.reverse()
print(number_list)

print('------- 7. sort list -------------')
number_list.sort()
print(number_list)
number_list.sort(reverse=True)
print(number_list)
