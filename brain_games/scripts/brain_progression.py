#!/usr/bin/env python


from ..games.progression import greet
from ..games.progression import welcome_user
from ..games.progression import rules
from ..games.progression import end_progression


def main():
    greet()
    welcome_user()
    rules()
    end_progression()


if __name__ == '__main__':
    main()
