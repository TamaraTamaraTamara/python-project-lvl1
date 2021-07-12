#!/usr/bin/env python

from random import randint

RULES_MSG = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    x = randint(1, 100)
    question = str(x)

    if x > 0:
        for i in range(2, x):
            if (x % i) == 0:
                return question, str("no")
        else:
            return question, str("yes")
