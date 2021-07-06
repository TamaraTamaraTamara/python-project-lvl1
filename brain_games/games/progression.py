#!/usr/bin/env python

from random import randint

RULES_MSG = 'What number is missing in the progression?'


def game():
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

    return print_sequence, replaced_number
