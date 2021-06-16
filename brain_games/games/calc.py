#!/usr/bin/env python

from random import choice, randint
from ..gameplay import ask_question


def calc_game():
    x = randint(1, 100)
    y = randint(1, 100)
    list = ['+', '-', '*']
    symbol = choice(list)

    ask_question(str(x) + ' ' + str(symbol) + ' ' + str(y))

    if symbol == '+':
        return x + y
    elif symbol == '-':
        return x - y
    elif symbol == '*':
        return x * y
