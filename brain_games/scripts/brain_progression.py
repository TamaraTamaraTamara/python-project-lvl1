#!/usr/bin/env python

from ..common.gameplay import welcome_user
from ..common.gameplay import gameplay
from ..games.progression import progression_game

rules_msg = 'What number is missing in the progression?'


def main():
    name = welcome_user()
    print(rules_msg)
    gameplay(name, progression_game)


if __name__ == '__main__':
    main()
