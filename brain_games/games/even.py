#!/usr/bin/env python

from random import randint
from ..gameplay import ask_question


def even_game():
    x = randint(1, 100)
    ask_question(str(x))

    if x % 2 == 0:
        return 'yes'
    elif x % 2 != 0:
        return 'no'
