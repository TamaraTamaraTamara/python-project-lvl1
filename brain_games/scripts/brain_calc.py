#!/usr/bin/env python

from ..common.gameplay import welcome_user
from ..common.gameplay import gameplay
from ..games.calc import calc_game


rules_msg = 'What is the result of the expression?'


def main():
    name = welcome_user()
    print(rules_msg)
    gameplay(name, calc_game)


if __name__ == '__main__':
    main()
