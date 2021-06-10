#!/usr/bin/env python

from ..common.gameplay import welcome_user
from ..common.gameplay import gameplay
from ..games.gcd import gcd_game

rules_msg = 'Find the greatest common divisor of given numbers.'


def main():
    name = welcome_user()
    print(rules_msg)
    gameplay(name, gcd_game)


if __name__ == '__main__':
    main()
