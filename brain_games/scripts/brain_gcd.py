#!/usr/bin/env python

from ..games.welcome import welcome_user
from ..games.gcd import rules
from ..games.gcd import end_gcd


def main():
    name = welcome_user()
    rules()
    end_gcd(name)


if __name__ == '__main__':
    main()
