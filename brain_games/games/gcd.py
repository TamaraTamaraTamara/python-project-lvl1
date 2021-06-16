#!/usr/bin/env python

from random import randint
from ..gameplay import ask_question


def gcd_game():
    x = randint(1, 100)
    y = randint(1, 100)
    ask_question(str(x) + ' ' + str(y))

    while y != 0:
        x, y = y, x % y

    return x
