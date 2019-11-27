#!/usr/bin/env python3

import sys


NAGIOSCODES = {
    'OK': 0,
    'WARNING': 1,
    'CRITICAL': 2,
    'UNKNOWN': 3,
    'DEPENDENT': 4,
}


def nagios_return(code, msg):
    """ prints the response message
        and exits the script with one
        of the defined exit codes
        DOES NOT RETURN
    """
    print("{} : {}".format(code, msg))
    sys.exit(NAGIOSCODES[code])


def test_stuff(warn=10, crit=20):
    try:
        1/0 #example something fails
    except Exception as e:
        return("UNKNOWN",str(e))
    
    # test stuff
    return(OK, "all ok")

if __name__ == '__main__':
    code, msg = test_stuff(10, 20)
    nagios_return(code, msg)
