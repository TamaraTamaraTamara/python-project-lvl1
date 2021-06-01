#!/usr/bin/env python

from ..games.welcome import welcome_user
from ..games.gameplay import gameplay
from ..games.gcd import rules
from ..games.gcd import ask_gcd


def main():
    name = welcome_user()
    rules()
    gameplay(name, ask_gcd)


if __name__ == '__main__':
    main()
