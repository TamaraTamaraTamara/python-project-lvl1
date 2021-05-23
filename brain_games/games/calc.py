#!/usr/bin/env python

import prompt
from random import choice, randint


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def rules():
    print('What is the result of the expression?')


def calc():
    global name
    x = randint(1, 100)
    y = randint(1, 100)
    list = ['+', '-', '*']
    symbol = choice(list)
    err_msg = " is wrong answer ;(. Correct answer was "
    question = str(x) + ' ' + str(symbol) + ' ' + str(y)
    if symbol == '+':
        correct_answer = x + y
    elif symbol == '-':
        correct_answer = x - y
    elif symbol == '*':
        correct_answer = x * y
    print('Question: ' + question)
    answer = input('Your answer: ')
    if int(answer) == correct_answer:
        print('Correct!')
        return True
    else:
        print(answer + err_msg + str(correct_answer))
        return False


def end_calc():
    global name
    counter = 1
    result = True
    while counter < 4:
        result = calc()
        counter = counter + 1
        if result is True and counter == 4:
            print('Congratulations, {}!'.format(name))
        elif result is False:
            print("Let's try again, {}!".format(name))
            return False
