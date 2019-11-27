#!/usr/bin/env python3
import click

@click.command()
@click.option('--count', '-c', default=1, help='Number of greetings.')
@click.option('--name', '-n', prompt='Your name',
              help='The person to greet.')
@click.argument("foo")
def hello(count, name, foo):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
