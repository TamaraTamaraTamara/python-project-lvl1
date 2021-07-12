#!/usr/bin/env python
import prompt

WELCOME_MSG = "Welcome to the Brain Games!"
ERR_MSG = " is wrong answer ;(. Correct answer was "


def engine(get_question_and_answer):
    print(WELCOME_MSG)
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))

    print(get_question_and_answer.RULES_MSG)

    counter = 1
    number_of_tries = 4
    while counter < number_of_tries:
        question, answer = get_question_and_answer.game()
        print('Question: ' + question)
        user_answer = input('Your answer: ')

        if user_answer == answer:
            print('Correct!')
            counter += 1

        else:
            print('\'{0}\' {1} \'{2}\''.format(user_answer, ERR_MSG, answer))
            print("Let's try again, {}!".format(name))
            return

    print('Congratulations, {}!'.format(name))
