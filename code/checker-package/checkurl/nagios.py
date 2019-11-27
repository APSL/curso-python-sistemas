import sys
from collections import namedtuple

NagiosCode = namedtuple("NagiosCode", "name value")

OK = NagiosCode('OK', 0)
WARNING = NagiosCode('WARNING', 1)
CRITICAL = NagiosCode('CRITICAL', 2)
UNKNOWN = NagiosCode('UNKNOWN', 3)
DEPENDENT = NagiosCode('DEPENDENT', 4)

#OK = 'OK'
#WARNING = 'WARNING'
#CRITICAL = 'CRITICAL'
#UNKNOWN = 'UNKNOWN'
#DEPENDENT = 'DEPENDENT'

#NAGIOSCODES = {
#    OK: 0,
#    WARNING: 1,
#    CRITICAL: 2,
#    UNKNOWN: 3,
#    DEPENDENT: 4,
#}

def nagios_return(code, msg):
    """ prints the response message and exits the script with one of the defined exit codes"""
    print("{} : {}".format(code.name, msg))
    sys.exit(code.value)
    #print("{} : {}".format(code, msg))
    #sys.exit(NAGIOSCODES[code])