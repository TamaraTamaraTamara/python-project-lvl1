#!/usr/bin/env python

from ..games.welcome import welcome_user
from ..games.gameplay import gameplay
from ..games.even import rules
from ..games.even import check_even


def main():
    name = welcome_user()
    rules()
    gameplay(name, check_even)


if __name__ == '__main__':
    main()
