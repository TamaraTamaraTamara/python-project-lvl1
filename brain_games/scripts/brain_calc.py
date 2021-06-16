#!/usr/bin/env python

from ..gameplay import welcome_user
from ..gameplay import gameplay
from brain_games.games.calc import calc_game


RULES_MSG = 'What is the result of the expression?'


def main():
    name = welcome_user()
    print(RULES_MSG)
    gameplay(name, calc_game)


if __name__ == '__main__':
    main()
