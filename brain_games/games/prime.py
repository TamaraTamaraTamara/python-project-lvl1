#!/usr/bin/env python

import prompt
from random import randint


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


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
    global name
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
    global name
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
