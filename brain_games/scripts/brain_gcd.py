#!/usr/bin/env python

from ..games.welcome import welcome_user
from ..games.gcd import rules
from ..games.gcd import end_gcd


def main():
    welcome_user()
    rules()
    end_gcd()


if __name__ == '__main__':
    main()
