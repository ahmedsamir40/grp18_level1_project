# program to write list into file

cities_list = ['Cairo','Alex','Mansura','Luxor']

with open('C:\\MY_FILES\\write_cities.txt','w') as f:
    for i in range(len(cities_list)):
        if i == len(cities_list) - 1:   # here the last city
            f.write(cities_list[i])
        else:
            f.write(cities_list[i] + '\n')
