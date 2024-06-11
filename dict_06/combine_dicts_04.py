print('-----pogram to combine 2 dictionaries with plus keys---')

dict1 = {'a': 100,'b':150, 'c':100}
dict2 = {'a': 50,'c':100, 'd':150}


# loop each k , v
# loop over dict or dict 2
for key , value in dict2.items():
    # check for each key to be found in dict 1 or not found
    # if key found in dict 1 then plus the values of this key and put the result in dict 1
    # if key not found in dict 1 then add this key with value to dict
    if key in dict1:
        dict1[key] = dict1[key] + value     # dic1['a'] = 150
    else:
        dict1[key] = value                 # dict1['b'] = 150
print(dict1)
    