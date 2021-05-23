#!/usr/bin/env python
from ..games.even import greet
from ..games.even import welcome_user
from ..games.even import rules
from ..games.even import end_even


def main():
    greet()
    welcome_user()
    rules()
    end_even()


if __name__ == '__main__':
    main()
