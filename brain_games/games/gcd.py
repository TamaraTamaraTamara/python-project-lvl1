#!/usr/bin/env python

from random import randint
from .welcome import name


def rules():
    print('Find the greatest common divisor of given numbers.')


def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def ask_gcd():
    x = randint(1, 100)
    y = randint(1, 100)
    err_msg = " is wrong answer ;(. Correct answer was "
    question = str(x) + ' ' + str(y)
    print('Question: ' + question)
    answer = input('Your answer: ')
    if int(answer) == find_gcd(x, y):
        print('Correct!')
        return True
    else:
        print(answer + err_msg + str(find_gcd(x, y)))
        return False


def end_gcd():
    counter = 1
    result = True
    while counter < 4:
        result = ask_gcd()
        counter = counter + 1
        if result is True and counter == 4:
            print('Congratulations, {}!'.format(name))
        elif result is False:
            print("Let's try again, {}!".format(name))
            return False
