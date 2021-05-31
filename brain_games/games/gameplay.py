#!/usr/bin/env python

def gameplay(name, gamename):
    counter = 1
    result = True
    while counter < 4:
        result = gamename()
        counter = counter + 1
        if result is True and counter == 4:
            print('Congratulations, {}!'.format(name))
        elif result is False:
            print("Let's try again, {}!".format(name))
            return False
