#!/usr/bin/env python3
import sys
import requests
import click

NAGIOSCODES = {
    'OK': 0,
    'WARNING': 1,
    'CRITICAL': 2,
    'UNKNOWN': 3,
    'DEPENDENT': 4,
}

def nagios_return(code, msg):
    """ prints the response message and exits the script with one of the defined exit codes
        DOES NOT RETURN
    """
    print("{} : {}".format(code, msg))
    sys.exit(NAGIOSCODES[code])

def test_stuff(url, warn=10, crit=20):
    try:
        r = requests.get(url, timeout=1)
    except Exception as e:
        return("UNKNOWN",str(e))

    if r.status_code >= 400:
        return("CRITICAL", f"code {r.status_code}")

    elapsed = r.elapsed.total_seconds()

    if r.elapsed.total_seconds() > crit:
        return("CRITICAL", "Elapsed time = {}".format(elapsed))
    if r.elapsed.total_seconds() > warn:
        return("WARNING", "Elapsed time = {}".format(elapsed))
    
    # test stuff
    return("OK", f"elapsed: {elapsed} {r.status_code}")

@click.command()
@click.argument("url", default="https://google.es/")
@click.option("--critical", "-c", type=click.FLOAT, default=1.0, help="critical threshold")
@click.option("--warning", "-w", type=click.FLOAT, default=0.01, help="critical threshold")
def main(url, critical, warning):
    click.echo(f"testing {url}")
    code, msg = test_stuff(url=url, crit=critical, warn=warning)
    nagios_return(code, msg)

if __name__ == '__main__':
    main()
