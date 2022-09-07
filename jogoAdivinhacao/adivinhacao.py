from statistics import correlation


print('Welcome to the guessing game!')

secret_number = 47

attempts = 3
round_number = 1
wrong_answer = True

while (round_number <= attempts and wrong_answer):
    print('round {} out of {}'.format(round_number, attempts))
    guess = int(input('Which is the secret number? '))

    if (guess == secret_number):
        print('correct answer')
        wrong_answer = False
    else:
        print('wrong answer')
        if (guess > secret_number):
            print('your guess is higher then the number')
        else:
            print('your guess is lower then the number')
    round_number += 1
