#!/usr/bin/env python

from random import randint
from ..common.gameplay import ask_question
from ..common.gameplay import get_answer
from ..common.gameplay import check_answer


def gcd_game():
    x = randint(1, 100)
    y = randint(1, 100)
    ask_question(str(x) + ' ' + str(y))

    while y != 0:
        x, y = y, x % y

    try:
        return check_answer(int(get_answer()), x)
    except ValueError:
        return False
