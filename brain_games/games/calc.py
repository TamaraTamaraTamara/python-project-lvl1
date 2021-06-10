#!/usr/bin/env python

from random import choice, randint
from ..common.gameplay import ask_question
from ..common.gameplay import get_answer
from ..common.gameplay import check_answer


def calc_game():
    x = randint(1, 100)
    y = randint(1, 100)
    list = ['+', '-', '*']
    symbol = choice(list)

    if symbol == '+':
        correct_answer = x + y
    elif symbol == '-':
        correct_answer = x - y
    elif symbol == '*':
        correct_answer = x * y

    ask_question(str(x) + ' ' + str(symbol) + ' ' + str(y))

    try:
        return check_answer(int(get_answer()), correct_answer)
    except ValueError:
        return False
