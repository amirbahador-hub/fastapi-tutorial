import click


@click.command()
@click.option("--name", prompt="insert your name")
@click.option("--option", default=1, help="The option of values")
def test(name, option):
    click.echo(f"name is {name} and option is {option}!")


if __name__ == "__main__":
    test()
