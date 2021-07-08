#!/usr/bin/env python
import prompt

WELCOME_MSG = "Welcome to the Brain Games!"
ERR_MSG = " is wrong answer ;(. Correct answer was "


def engine(name):
    print(WELCOME_MSG)
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))

    print(name.RULES_MSG)

    counter = 1
    while counter < 4:
        question, answer = name.game()
        print('Question: ' + question)
        usr_answer = input('Your answer: ')
        counter += 1

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
