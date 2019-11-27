#!/usr/bin/env python3

import click
from checkurl import __VERSION__
from checkurl.checker import testurl
from checkurl.nagios import  nagios_return


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f"Version {__VERSION__}")
    ctx.exit()

@click.command()
@click.option('-v', '--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
@click.option('-w', '--warning', help="WARNING threshold for alarm", default=0.6, type=click.FLOAT)
@click.option('-c', '--critical', help="CRITICAL threshold for alarm", default=2.0, type=click.FLOAT)
@click.argument('url', required=True)
def cli(url, warning, critical):
    """Checks URL as NRPE plugin"""
    code, msg = testurl(url, warning, critical)
    nagios_return(code, msg)


if __name__ == '__main__':
    cli()
