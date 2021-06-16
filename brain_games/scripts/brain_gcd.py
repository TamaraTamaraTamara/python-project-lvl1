#!/usr/bin/env python

from ..gameplay import welcome_user
from ..gameplay import gameplay
from brain_games.games.gcd import gcd_game

RULES_MSG = 'Find the greatest common divisor of given numbers.'


def main():
    name = welcome_user()
    print(RULES_MSG)
    gameplay(name, gcd_game)


if __name__ == '__main__':
    main()
