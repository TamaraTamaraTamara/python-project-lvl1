#!/usr/bin/env python

from ..gameplay import welcome_user
from ..gameplay import gameplay
from brain_games.games.even import even_game

RULES_MSG = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    name = welcome_user()
    print(RULES_MSG)
    gameplay(name, even_game)


if __name__ == '__main__':
    main()
