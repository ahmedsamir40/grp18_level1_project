import random
print('--------- random game calculator----- ')
correct_answer = 0
wrong_answer = 0
for i in range (5):
    print('question nu.', i+1)
    first_number = random.randint (1,100)
    second_number = random.randint (1,100)



    print(first_number,' + ',second_number,'=')
    user_input = input()
    user_input = int(user_input)

    if user_input == first_number + second_number:
        print('correct answer')
        correct_answer = correct_answer +1
    else:
        print('wrong answer')
        wrong_answer = wrong_answer +1

    print('--------')
print('end of program')
print('correct answer=', correct_answer)
print('wrong answer =', wrong_answer)