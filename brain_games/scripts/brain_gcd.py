#!/usr/bin/env python


from ..games.gcd import greet
from ..games.gcd import welcome_user
from ..games.gcd import rules
from ..games.gcd import end_gcd


def main():
    greet()
    welcome_user()
    rules()
    end_gcd()


if __name__ == '__main__':
    main()
