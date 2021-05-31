#!/usr/bin/env python

from ..games.welcome import welcome_user
from ..games.even import rules
from ..games.even import end_even


def main():
    name = welcome_user()
    rules()
    end_even(name)


if __name__ == '__main__':
    main()
