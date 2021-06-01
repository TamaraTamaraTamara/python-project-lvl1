#!/usr/bin/env python

from ..games.welcome import welcome_user
from ..games.gameplay import gameplay
from ..games.progression import rules
from ..games.progression import ask_progression


def main():
    name = welcome_user()
    rules()
    gameplay(name, ask_progression)


if __name__ == '__main__':
    main()
