#!/usr/bin/env python3

import click
from os.path import join, expanduser
import yaml

__VERSION__ = '0.0.1'

def get_config(ctx, param, configfile):
    """Reads config file, parses yaml, and saves config to ctx"""
    ctx.params['config'] = yaml.load(configfile.read(), Loader=yaml.FullLoader)

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f"Version {__VERSION__}")
    ctx.exit()

@click.option('-c', '--config-file',
        default=expanduser("~/.config/test.yml"), 
        help="Config file. Defaults to ~/.config/test.yml",
        type=click.File('r'), callback=get_config)
@click.option('-v', '--version', 
        is_flag=True, callback=print_version, 
        expose_value=False, is_eager=True)
@click.group()
def main(config_file, config):
    pass

@main.command()
@click.pass_context
def foo(ctx):
    """Does foo"""
    config = ctx.parent.params['config']
    click.echo("fooing with config:")
    click.echo(config)

@main.command()
@click.pass_context
def bar(ctx):
    """Does bar"""
    config = ctx.parent.params['config']
    click.echo("baring with config:")
    click.echo(config)

if __name__ == '__main__':
    main()