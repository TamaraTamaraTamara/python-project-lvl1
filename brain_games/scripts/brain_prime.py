#!/usr/bin/env python

from ..games.welcome import welcome_user
from ..games.prime import rules
from ..games.prime import end_prime


def main():
    name = welcome_user()
    rules()
    end_prime(name)


if __name__ == '__main__':
    main()
