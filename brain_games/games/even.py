#!/usr/bin/env python

from random import randint

RULES_MSG = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    x = randint(1, 100)
    question = str(x)

    if x % 2 == 0:
        return question, 'yes'
    elif x % 2 != 0:
        return question, 'no'
