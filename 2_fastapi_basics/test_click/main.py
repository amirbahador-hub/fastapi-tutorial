import click

# pipenv --python 3.10
# pipenv shell
# pipenv install click
# pipenc install -d black

@click.command()
@click.option("--name", prompt="Please enter your name", help="This is greeting app \n please put your name after the name argument")
def hello(name):
    """
    Examples: \n
    python main.py --name Amirbahador \n
    python main.py \n 
    python main.py --help \n
    python main.py -h (did you mean help!)
    """
    click.echo(f"Hello {name}")

if __name__ == "__main__":
    hello()
