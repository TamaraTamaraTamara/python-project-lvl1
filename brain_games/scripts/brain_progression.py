#!/usr/bin/env python

from ..gameplay import welcome_user
from ..gameplay import gameplay
from brain_games.games.progression import progression_game

RULES_MSG = 'What number is missing in the progression?'


def main():
    name = welcome_user()
    print(RULES_MSG)
    gameplay(name, progression_game)


if __name__ == '__main__':
    main()
