#!/usr/bin/env python
import prompt

WELCOME_MSG = "Welcome to the Brain Games!"
ERR_MSG = " is wrong answer ;(. Correct answer was "


def welcome_user():
    print(WELCOME_MSG)
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def ask_question(gamename):
    print('Question: ' + str(gamename))


def get_answer():
    return input('Your answer: ')


def gameplay(name, gamename):
    counter = 1
    while counter < 4:
        answer = gamename()
        counter += 1
        usr_answer = get_answer()

        try:
            usr_answer = int(usr_answer)
        except ValueError:
            None

        if usr_answer == answer:
            print('Correct!')
            if counter == 4:
                print('Congratulations, {}!'.format(name))
        else:
            print('\'{0}\' {1} \'{2}\''.format(usr_answer, ERR_MSG, answer))
            print("Let's try again, {}!".format(name))
            break
