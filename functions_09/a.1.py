def add_numbers(x,y):
    result = x+y
    return result


# v_result = add_numbers(2,4)
v_result = add_numbers(x=2,y=4)
print(v_result)
print('------')


def subtract_numbers(x,y):
    result = x - y
    return result


# v_result = subtract_numbers(8,4)
v_result = subtract_numbers(x=8,y=4)
print(v_result)
print('------')


def multiply_numbers(x,y):
    result = x * y
    return result


# v_result = multiply_numbers(5,10)
v_result = multiply_numbers(x=5,y=10)
print(v_result)
print('-----')


def divide_numbers(x,y):
    if y == 0:
        print('invalid')
    else:
        result = (x / y)
        return result


# v_result = divide_numbers(10,0)
v_result = divide_numbers(x=10,y=0)
if v_result is not None:
    print(v_result)