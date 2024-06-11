def add_numbers(*numbers_tubles):
    """
    this function used to get the total from all parameters
    :ramp numbers_tuples:  variable parameter length you can odd any numbers of parameters here
    :return: total from all parameters
    """
    total = 0
    for item in numbers_tubles:
        total = total + item
    return total


#main program
print(add_numbers(5,6,8,10,15,17,16,12,20,1))