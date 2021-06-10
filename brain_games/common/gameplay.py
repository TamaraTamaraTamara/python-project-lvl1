#!/usr/bin/env python
import prompt

welcome_msg = "Welcome to the Brain Games!"
err_msg = " is wrong answer ;(. Correct answer was "


def welcome_user():
    print(welcome_msg)
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def ask_question(gamename):
    print('Question: ' + str(gamename))


def get_answer():
    return input('Your answer: ')


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        try:
            user_part = '\'' + str(user_answer) + '\''
            correct_part = '\'' + str(correct_answer) + '\''
            print(user_part + err_msg + correct_part)
            return False
        except ValueError:
            print(user_answer + err_msg + correct_answer)
            return False


def gameplay(name, gamename):
    counter = 1
    result = True
    while counter < 4:
        result = gamename()
        counter = counter + 1
        if result is True and counter == 4:
            print('Congratulations, {}!'.format(name))
        elif result is False:
            print("Let's try again, {}!".format(name))
            return False
