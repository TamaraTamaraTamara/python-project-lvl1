#!/usr/bin/env python

from random import randint
from .welcome import name


def rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def check_prime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        else:
            return True


def ask_prime():
    x = randint(1, 100)
    print('Question: ' + str(x))
    answer = input('Your answer: ')
    if answer == 'yes':
        if check_prime(x) is True:
            print('Correct!')
            return True
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            return False
    elif answer == 'no':
        if check_prime(x) is False:
            print('Correct!')
            return True
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            return False
    else:
        return False


def end_prime():
    counter = 1
    result = True
    while counter < 4:
        result = ask_prime()
        counter = counter + 1
        if result is True and counter == 4:
            print('Congratulations, {}!'.format(name))
        elif result is False:
            print("Let's try again, {}!".format(name))
            return False
