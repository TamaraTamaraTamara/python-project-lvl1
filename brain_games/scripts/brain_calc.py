#!/usr/bin/env python

from ..games.welcome import welcome_user
from ..games.calc import rules
from ..games.calc import end_calc


def main():
    welcome_user()
    rules()
    end_calc()


if __name__ == '__main__':
    main()
