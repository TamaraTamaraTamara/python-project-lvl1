#!/usr/bin/env python

from ..common.gameplay import welcome_user
from ..common.gameplay import gameplay
from ..games.prime import prime_game

rules_msg = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    name = welcome_user()
    print(rules_msg)
    gameplay(name, prime_game)


if __name__ == '__main__':
    main()
