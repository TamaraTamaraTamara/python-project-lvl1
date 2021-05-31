#!/usr/bin/env python

from ..games.welcome import welcome_user
from ..games.gameplay import gameplay
from ..games.calc import rules
from ..games.calc import calc


def main():
    name = welcome_user()
    rules()
    gameplay(name, calc)


if __name__ == '__main__':
    main()
