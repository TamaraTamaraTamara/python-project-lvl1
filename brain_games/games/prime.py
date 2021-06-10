#!/usr/bin/env python

from random import randint
from ..common.gameplay import ask_question
from ..common.gameplay import get_answer
from ..common.gameplay import check_answer


def check_prime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        else:
            return True


def prime_game():
    x = randint(1, 100)
    ask_question(str(x))

    if x > 0:
        for i in range(2, x):
            if (x % i) == 0:
                correct_answer = "no"
                break
        else:
            correct_answer = "yes"

    try:
        return check_answer(get_answer(), correct_answer)
    except ValueError:
        return False
