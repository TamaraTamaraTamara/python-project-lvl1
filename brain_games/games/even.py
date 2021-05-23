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
    print('Answer "yes" if the number is even, otherwise answer "no".')


def check_even():
    x = randint(1, 100)
    global name
    print ('Question: ' + str(x))
    answer = input('Your answer: ')
    if x % 2 == 0 and answer == 'yes' or x % 2 != 0 and answer == 'no':
        print('Correct!')
        return True
    else:
        if answer == 'yes':
            print ("'yes' is wrong answer ;(. Correct answer was 'no'.")
            return False
        elif answer == 'no':
            print ("'no' is wrong answer ;(. Correct answer was 'yes'.")
            return False
        else: 
            return False


def end_even():
    global name
    counter = 1
    result = True
    while counter < 4:
        result = check_even()
        counter = counter + 1
        if result == True and counter == 4:
            print('Congratulations, {}!'.format(name))
        elif result == False:
            print("Let's try again, {}!".format(name))
            return False
        



