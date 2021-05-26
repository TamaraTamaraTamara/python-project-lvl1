#!/usr/bin/env python

import prompt
from random import randint


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def rules():
    print('What number is missing in the progression?')


def ask_progression():
    start = randint(1, 50)
    step = randint(1, 10)
    seq_len = randint(5, 10)
    index_replacement = randint(0, seq_len - 1)
    sequence = list(range(start, start + step * seq_len, step))
    replaced_symbol = sequence[index_replacement]
    sequence[index_replacement] = ".."
    err_msg = " is wrong answer ;(. Correct answer was "

    # print('PROVERKA- start,step,seq_len,index_replacement,
    # replaced_symbol',start,step,seq_len,index_replacement,replaced_symbol)

    # print question

    print('Question: ', end='')
    for i in sequence:
        print(i, end=' ')
    print()
    # check answer
    answer = input('Your answer: ')
    if int(answer) == replaced_symbol:
        print('Correct!')
        return True
    else:
        print(answer + err_msg + str(replaced_symbol))
        return False


def end_progression():
    global name
    counter = 1
    result = True
    while counter < 4:
        result = ask_progression()
        counter = counter + 1
        if result is True and counter == 4:
            print('Congratulations, {}!'.format(name))
        elif result is False:
            print("Let's try again, {}!".format(name))
            return False
