#!/usr/bin/env python


from ..games.prime import greet
from ..games.prime import welcome_user
from ..games.prime import rules
from ..games.prime import end_prime


def main():
    greet()
    welcome_user()
    rules()
    end_prime()


if __name__ == '__main__':
    main()
