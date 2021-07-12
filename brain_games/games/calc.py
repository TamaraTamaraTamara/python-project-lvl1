#!/usr/bin/env python

from random import choice, randint

RULES_MSG = 'What is the result of the expression?'


def game():
    x = randint(1, 100)
    y = randint(1, 100)
    list = ['+', '-', '*']
    symbol = choice(list)

    question = str(x) + ' ' + str(symbol) + ' ' + str(y)

    if symbol == '+':
        return question, str(x + y)
    elif symbol == '-':
        return question, str(x - y)
    elif symbol == '*':
        return question, str(x * y)
