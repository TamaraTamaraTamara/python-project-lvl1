#!/usr/bin/env python

from ..common.gameplay import welcome_user
from ..common.gameplay import gameplay
from ..games.even import even_game

rules_msg = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    name = welcome_user()
    print(rules_msg)
    gameplay(name, even_game)


if __name__ == '__main__':
    main()
