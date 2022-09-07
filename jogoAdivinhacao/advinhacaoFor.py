print('Welcome to the guessing game!')

secret_number = 47

attempts = 3

for round_number in range(1, attempts + 1):
    print('round {} out of {}'.format(round_number, attempts))
    guess = int(input('Which is the secret number between 1 and 100? '))

    if (guess < 1 or guess > 100):
        print('The number must be between 1 and 100')
        continue

    if (guess == secret_number):
        print('correct answer')
        break
    else:
        print('wrong answer')
        if (guess > secret_number):
            print('your guess is higher then the number')
        else:
            print('your guess is lower then the number')
