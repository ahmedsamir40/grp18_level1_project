import random
correct_answers = 0
wrong_answers = 0
for i in range (5):
    print('question n =', i+1)

    first_number = random.randint(1,100)
    second_number = 20
    print(first_number,'+', second_number,' = ')
    user_input = input()
    user_input = int (user_input)
    if user_input == first_number + second_number :
        print('corresct answers')
        correct_answers = correct_answers +1

    else:
        print('wrong answers')
        wrong_answers = wrong_answers +1
    print('-------------------')
print('end of program')
print('correct answers =  ',correct_answers)
print('wrong anwers = ',wrong_answers)