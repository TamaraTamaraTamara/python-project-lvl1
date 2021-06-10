#!/usr/bin/env python

from random import randint
from ..common.gameplay import ask_question
from ..common.gameplay import get_answer
from ..common.gameplay import check_answer


def even_game():
    x = randint(1, 100)
    ask_question(str(x))

    if x % 2 == 0:
        correct_answer = 'yes'
    elif x % 2 != 0:
        correct_answer = 'no'

    try:
        return check_answer(get_answer(), correct_answer)
    except ValueError:
        return False
