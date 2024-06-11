import math      #call math module  //  to use pow() funtion

print('---------program to calculate area , perimetar of circle --------')
# input : pi / radius
# outpur : area / perimeter


radies = 7
pi = math.pi

perimeter = 2 * pi * radies
area = pi * math.pow(radies,2)
print('perimeter = ' , round(perimeter,2 ))
print('area = ', area)
