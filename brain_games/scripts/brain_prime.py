#!/usr/bin/env python

from ..games.welcome import welcome_user
from ..games.gameplay import gameplay
from ..games.prime import rules
from ..games.prime import ask_prime


def main():
    name = welcome_user()
    rules()
    gameplay(name, ask_prime)


if __name__ == '__main__':
    main()
