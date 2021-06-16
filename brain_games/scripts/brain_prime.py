#!/usr/bin/env python

from ..gameplay import welcome_user
from ..gameplay import gameplay
from brain_games.games.prime import prime_game

RULES_MSG = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    name = welcome_user()
    print(RULES_MSG)
    gameplay(name, prime_game)


if __name__ == '__main__':
    main()
