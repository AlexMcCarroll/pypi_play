import click, emoji, os

@click.group()
def cli():
    pass

@cli.command()
def init():
    if not os.path.exists('tests'):
        os.makedirs('tests')
        os.makedirs('tests/tests')
        click.echo('    create  test/')
        click.echo('    create  test/test')
    else:
        click.echo('    exist   test/')
        click.echo('    exist   test/test')

@cli.command()
def about():
    click.echo('Made by Alex, Tom, Ricky, Hemesh (Feb 2018 Cohort - Makers Academy)')
