#!/usr/bin/env python

from random import randint
from ..gameplay import ask_question


def prime_game():
    x = randint(1, 100)
    ask_question(str(x))

    if x > 0:
        for i in range(2, x):
            if (x % i) == 0:
                return "no"
        else:
            return "yes"
