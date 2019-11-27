import click
from sh import ls

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def touch(filename):
    """Print FILENAME if the file exists."""
    click.echo(click.format_filename(filename))
    out = ls(filename, "-l")
    click.echo(out)

if __name__ == "__main__":
    touch()