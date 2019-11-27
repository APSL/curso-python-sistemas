#!/usr/bin/env python3

import click

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@cli.command()  # @cli, not @click!
def foo():
    """foo command does foo"""
    click.echo('Fooing...')

@cli.command()  # @cli, not @click!
def bar():
    """Bar command does bar"""
    click.echo('Baring...')

if __name__ == '__main__':
    cli()
