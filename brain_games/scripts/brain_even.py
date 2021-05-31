#!/usr/bin/env python

from ..games.welcome import welcome_user
from ..games.even import rules
from ..games.even import end_even


def main():
    name2 = welcome_user()
    rules()
    end_even(name2)


if __name__ == '__main__':
    main()
