#!/usr/bin/env python
from brain_games.even import greet
from brain_games.even import welcome_user
from brain_games.even import rules
from brain_games.even import check_even
from brain_games.even import end_even


def main():
    greet()
    welcome_user()
    rules()
    end_even()


if __name__ == '__main__':
    main()