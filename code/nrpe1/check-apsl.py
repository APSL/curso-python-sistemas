#!/usr/bin/env python3
import sys
import requests

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
        r = requests.get("https://www.apsl.net/")
    except Exception as e:
        return("UNKNOWN",str(e))

    if r.elapsed.total_seconds() > crit:
        return("CRITICAL", "CRIT: elapsed time = {}".format(r.elapsed.total_seconds()))
    
    # test stuff
    return(OK, "all ok")

if __name__ == '__main__':
    code, msg = test_stuff(10, 0.1)
    nagios_return(code, msg)
