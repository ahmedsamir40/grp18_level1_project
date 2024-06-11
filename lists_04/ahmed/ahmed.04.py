my_nested_list = [
                  [100, 'samir', 5000.0],
                  [101, 'ahmed', 4000.0]
                 ]
print(len(my_nested_list))
print(my_nested_list)
print(my_nested_list[0])
print(my_nested_list[1])
print(my_nested_list[1][1])
print(my_nested_list[0][2])
my_nested_list.append([102, 'mohamed', 3000])
print(my_nested_list)
print(my_nested_list[2][1])

new_nested_list = [
                  [100, 'samir', 5000.0,['cairo', 'nasrcity', 123456]],
                  [101, 'ahmed', 4000.0,['cairo', 'maadi', 123456789]]
                  ]
print(new_nested_list[0][3][1])
print(new_nested_list[1][3][2])
numbers_list = [16, 5, 20, 13, 2, 14, 30, 20, 70, 20]
print(numbers_list[:5])