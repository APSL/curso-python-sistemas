#!/usr/bin/env python3
import sys
import requests
import click
import sentry_sdk
from sentry_sdk import configure_scope, push_scope, capture_exception
from decouple import config

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
        # We capture exception in order to send an UNKNOWN to nagios.
        # but we send information to sentry, with warning level instead of critical
        with push_scope() as scope:
            scope.set_tag("tested-url", url)
            scope.level = 'warning'
            capture_exception(e)
        return("UNKNOWN",str(e))
    r = requests.get(url, timeout=1)

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
    sentry_dsn = config("SENTRY_DSN")
    sentry_sdk.init(sentry_dsn)


    click.echo(f"testing {url}")
    with configure_scope() as scope:
        scope.set_tag("my-tag", "my value")
        scope.user = {'id': 42, 'email': 'john.doe@example.com'}
    code, msg = test_stuff(url=url, crit=critical, warn=warning)
    nagios_return(code, msg)

if __name__ == '__main__':
    main()
