#!/usr/bin/env python

from ..games.welcome import welcome_user
from ..games.progression import rules
from ..games.progression import end_progression


def main():
    name = welcome_user()
    rules()
    end_progression(name)


if __name__ == '__main__':
    main()
