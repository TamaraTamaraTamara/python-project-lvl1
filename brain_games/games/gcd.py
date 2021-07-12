#!/usr/bin/env python

from random import randint

RULES_MSG = 'Find the greatest common divisor of given numbers.'


def game():
    x = randint(1, 100)
    y = randint(1, 100)
    question = str(x) + ' ' + str(y)

    while y != 0:
        x, y = y, x % y

    return question, str(x)
