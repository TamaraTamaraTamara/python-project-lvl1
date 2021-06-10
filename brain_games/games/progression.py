#!/usr/bin/env python

from random import randint
from ..common.gameplay import ask_question
from ..common.gameplay import get_answer
from ..common.gameplay import check_answer


def progression_game():
    start = randint(1, 50)
    step = randint(1, 10)
    seq_len = randint(5, 10)
    index_replacement = randint(0, seq_len - 1)
    sequence = list(range(start, start + step * seq_len, step))
    replaced_number = sequence[index_replacement]
    sequence[index_replacement] = ".."
    print_sequence = ''

    for i in sequence:
        print_sequence += str(i) + ' '

    ask_question(print_sequence)

    try:
        return check_answer(int(get_answer()), replaced_number)
    except ValueError:
        return False
