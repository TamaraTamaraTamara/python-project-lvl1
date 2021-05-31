#!/usr/bin/env python

from ..games.welcome import welcome_user
from ..games.calc import rules
from ..games.calc import end_calc


def main():
    name = welcome_user()
    rules()
    end_calc(name)


if __name__ == '__main__':
    main()
