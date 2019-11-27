import click

@click.command()
@click.argument('filename', required=True)
def touch(filename):
    """Print FILENAME."""
    click.echo(filename)

if __name__ == "__main__":
    touch()